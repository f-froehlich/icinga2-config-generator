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
usage $0 -f FILE | -d DIR [ -i ]

	-f FILE
		Path to file
	-d DIR
		Path to dir
	-i
	  Invert (ok if not exist, critical if exist)
_EOT_
	exit 255
}

# Parse the input options
while getopts ":d:f:ih" opt; do
  case $opt in
    f)
      FILE=$OPTARG
      ;;
    d)
      DIR=$OPTARG
      ;;
    i)
      INVERT=1
      ;;
    h)
      usage ;;
  esac
done

if [[ -z $FILE ]]; then

  if [[ -z $DIR ]]; then
	  echo "UNKNOWN - File or dir is missing"
	  usage
	  exit 3
  fi

  # check dir
  if [[ -d $DIR ]]; then
    if [[ -n $INVERT ]]; then
      echo "CRITICAL - DIR $DIR exist but it souldn't!"
      exit 2
    fi

    echo "OK - Dir $DIR exist"
    exit 0
  fi

  if [[ -n $INVERT ]]; then
    echo "OK - Dir $DIR dos not exist and it souldn't"
    exit 2
  fi
  echo "CRITICAL - Dir $DIR dos not exist but it sould!"
  exit 2
fi


# check file
if [[ -f $FILE ]]; then
  if [[ -n $INVERT ]]; then
    echo "CRITICAL - File $FILE exist but it souldn't!"
    exit 2
  fi

  echo "OK - File $FILE exist"
  exit 0
fi

if [[ -n $INVERT ]]; then
  echo "OK - File $FILE dos not exist and it souldn't"
  exit 2
fi
echo "CRITICAL - File $FILE dos not exist but it sould!"
exit 2