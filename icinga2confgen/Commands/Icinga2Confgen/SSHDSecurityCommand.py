#!/usr/bin/python3
# -*- coding: utf-8

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

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.ValueChecker import ValueChecker


class SSHDSecurityCommand(Command):

    def __init__(self, id):
        Command.__init__(self, id)

    @staticmethod
    def create(id, force_create=False):
        ValueChecker.validate_id(id)
        command = None if force_create else ConfigBuilder.get_command(id)
        if None is command:
            command = SSHDSecurityCommand(id)
            ConfigBuilder.add_command(id, command)

        return command

    def get_command(self):
        return 'check_sshd_security.py'

    def get_arguments(self):
        config = """{
    "-r" = {
      value = "$command_sshd_security_permit_root_login$"
      set_if = {{ macro("$command_sshd_security_permit_root_login$") != false }}
    }
    "-k" = {
      value = "$command_sshd_security_public_key_auth$"
      set_if = {{ macro("$command_sshd_security_public_key_auth$") != false }}
    }
    "-P" = {
      value = "$command_sshd_security_password_auth$"
      set_if = {{ macro("$command_sshd_security_password_auth$") != false }}
    }
    "--permit-empty-passwords" = {
      value = "$command_sshd_security_permit_empty_passwords$"
      set_if = {{ macro("$command_sshd_security_permit_empty_passwords$") != false }}
    }
    "--fingerprint-hash" = {
      value = "$command_sshd_security_fingerprint_hash$"
      set_if = {{ macro("$command_sshd_security_fingerprint_hash$") != false }}
    }
    "--port" = {
      value = "$command_sshd_security_port$"
      set_if = {{ macro("$command_sshd_security_port$") != false }}
    }
    "--challenge-response-authentication" = {
      value = "$command_sshd_security_challenge_response_authentication$"
      set_if = {{ macro("$command_sshd_security_challenge_response_authentication$") != false }}
    }
    "--config" = {
      value = "$command_sshd_security_config$"
      set_if = {{ macro("$command_sshd_security_config$") != false }}
      repeat_key = true
    }
  }
"""
        return config
