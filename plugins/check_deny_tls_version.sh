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
usage $0 -p PROTOCOL -d DOMAIN [-a ADDRESS]

	-p 1.0 | 1.1 | 1.2 | 1.3
		specify the protocol to check
	-d DOMAIN
		domain to check
	-a ADDRESS
		optional, set static ip for domain and skip DNS resolution
_EOT_
	exit 255
}

# Parse the input options
while getopts ":p:d:a:h:" opt; do
  case $opt in
    p)
      PROTOCOL=$OPTARG
      ;;
    d)
      DOMAIN=$OPTARG
      ;;
    a)
      ADDRESS=$OPTARG
      ;;
    h)
      usage ;;
  esac
done

# Check if dig is available at all - fail hard if not
pathToCurl=$( which curl )
if [[ ! -e $pathToCurl ]]; then
	echo "No executable of curl found, cannot proceed without curl. Sorry!"
	exit 1
fi

# Check if we got a protocol to validate - fail hard if not
if [[ -z $PROTOCOL ]]; then
	echo "Missing protocol to test - please provide a tls protocol via the -p parameter."
	usage
	exit 3
fi
PROTOCOL=$(echo $PROTOCOL | sed -e 's/\(.*\)/\L\1/' | sed 's/tls//g' )
COMMAND="$pathToCurl --tlsv$PROTOCOL --tls-max $PROTOCOL -o /dev/null https://$DOMAIN "

if [[ ! -z "$ADDRESS" ]]; then
  COMMAND="$COMMAND --resolve $DOMAIN:443:$ADDRESS "
fi

OUTPUT=$($COMMAND 2>&1)
REFUSED=$(echo "$OUTPUT" | grep "Connection refused")
ERROR=$(echo "$OUTPUT" | grep "error")

if [[ ! -z "$REFUSED" ]]; then
   echo "WARNING: Can't connect to Server"
   exit 1
elif [[ -z "$ERROR" ]]; then
  echo "CRITICAL: TLSv$PROTOCOL is allowed by Server but it shouldn't"
  exit 2
else
  echo "OK: TLSv$PROTOCOL is not allowed by Server and it shouldn't"
  exit 0
fi
