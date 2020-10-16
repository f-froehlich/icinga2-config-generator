#!/usr/bin/env bash
#  Icinga2 configuration generator
#
#  Icinga2 configuration file generator for hosts, commands, checks, ... in python
#
#  Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> https://icinga2.confgen.org
#
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  For all license terms see README.md and LICENSE Files in root directory of this Project.

usage() {
	cat - >&2 << _EOT_
usage $0 -a DOMAIN | IP -p PORT -u USER -c CREDENTIALS [ -s ]

	-p PORT
		specify the port of host
	-a DOMAIN | IP
		domain or address of host
	-u USER
		User for sign in
	-c CREDENIALS
	  Password for sign in
  -s
    Execute as sudo
_EOT_
	exit 255
}

# Parse the input options
while getopts ":p:u:a:c:" opt; do
  case $opt in
    p)
      PORT=$OPTARG
      ;;
    u)
      USER=$OPTARG
      ;;
    a)
      ADDRESS=$OPTARG
      ;;
    c)
      PASSWORD=$OPTARG
      ;;
  esac
done
while getopts "sh" opt; do
  case $opt in
    s)
      AS_SUDO=1
      ;;
    h)
      usage ;;
  esac
done

pathToDocker=$( which docker )
if [[ ! -e $pathToDocker ]]; then
	echo "No executable of docker found, cannot proceed without docker. Sorry!"
	exit 1
fi

if [[ -z $PORT ]]; then
	echo "Port is missing"
	usage
	exit 3
fi
if [[ -z $ADDRESS ]]; then
	echo "Address is missing"
	usage
	exit 3
fi
if [[ -z $USER ]]; then
	echo "User is missing"
	usage
	exit 3
fi
if [[ -z $PASSWORD ]]; then
	echo "Password is missing"
	usage
	exit 3
fi


COMMAND="$pathToDocker login -u $USER -p $PASSWORD $ADDRESS:$PORT "
if [[ -z $AS_SUDO ]]; then
	COMMAND="sudo $COMMAND"
fi

OUTPUT=$($COMMAND 2>&1)

SUCCESS=$(echo "$OUTPUT" | grep "Login Succeeded" | wc -l )
DAEMON_CONFIG_ERROR=$(echo "$OUTPUT" | grep "server gave HTTP response to HTTPS client" | wc -l )
TIMEOUT=$(echo "$OUTPUT" | grep "imeout" | wc -l )
ACCESS_DENID=$(echo "$OUTPUT" | grep "authentication required" | wc -l )


if (($SUCCESS==1)); then
  echo "OK - Login Succeeded on $ADDRESS:$PORT"
  exit 0
fi
if (($DAEMON_CONFIG_ERROR==1)); then
  echo "UNKNOWN - server gave HTTP response to HTTPS client, check /etc/docker/daemon.json for insecure registries $ADDRESS:$PORT"
  exit 3
fi
if (($TIMEOUT==1)); then
  echo "WARNING - Timout during sign in to docker registry on $ADDRESS:$PORT"
  exit 1
fi
if (($ACCESS_DENID==1)); then
  echo "CRITICAL - can't sign in to docker registry on $ADDRESS:$PORT"
  exit 2
fi

echo "CRITICAL - $OUTPUT"
exit 2