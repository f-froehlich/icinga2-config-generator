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
from icinga2confgen.Checks.Check import Check
from icinga2confgen.Commands.MonitoringPlugins.SecurityObserver.MozillaObservatoryCommand import \
    MozillaObservatoryCommand
from icinga2confgen.Helpers.Webrequest import Webrequest
from icinga2confgen.Commands.MonitoringPlugins.PageContentCommand import PageContentCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from icinga2confgen.ValueChecker import ValueChecker


class CheckMozillaObservatory(Webrequest):

    def __init__(self, id: str):
        Webrequest.__init__(self, id, 'CheckMozillaObservatory', 'mozilla_observatory', 'monitoring_plugins')
        self.__ignore_hidden = False
        self.__ignore_rescan = False
        self.__warning_score = -1
        self.__warning_grade = 'B'
        self.__critical_score = -10
        self.__critical_grade = 'C'
        self.__config = []
        self.__host = None
        self._allowed_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E+',
                                 'E', 'E-', 'F+', 'F', 'F-']

        self.set_ssl(True)

    def set_ignore_hidden(self, ignore_hidden):
        ValueChecker.is_bool(ignore_hidden)

        self.__ignore_hidden = ignore_hidden
        return self

    def get_ignore_hidden(self):
        return self.__ignore_hidden

    def set_ignore_rescan(self, ignore_rescan):
        ValueChecker.is_bool(ignore_rescan)

        self.__ignore_rescan = ignore_rescan
        return self

    def get_ignore_rescan(self):
        return self.__ignore_rescan

    def set_warning_score(self, warning_score):
        ValueChecker.is_number(warning_score)
        self.__warning_score = warning_score

        return self

    def get_warning_score(self):
        return self.__warning_score

    def set_warning_grade(self, warning_grade):
        ValueChecker.is_string(warning_grade)
        if warning_grade not in self._allowed_grades:
            raise Exception("Grade dos not exist. Choose from " + ', '.join(self._allowed_grades))
        self.__warning_grade = warning_grade

        return self

    def get_warning_grade(self):
        return self.__warning_grade

    def set_critical_score(self, critical_score):
        ValueChecker.is_number(critical_score)
        self.__critical_score = critical_score

        return self

    def get_critical_score(self):
        return self.__critical_score

    def set_critical_grade(self, critical_grade):
        ValueChecker.is_string(critical_grade)
        if critical_grade not in self._allowed_grades:
            raise Exception("Grade dos not exist. Choose from " + ', '.join(self._allowed_grades))
        self.__critical_grade = critical_grade

        return self

    def get_critical_grade(self):
        return self.__critical_grade

    def add_config(self, name, warning, critical):
        ValueChecker.is_string(name)
        if '-' == warning and '-' != critical:
            raise Exception('If warning is set to - you have to set critical also to - to ignore the test')
        elif '-' != warning and '-' == critical:
            raise Exception('If critical is set to - you have to set warning also to - to ignore the test')
        elif not '-' == warning == critical:
            ValueChecker.is_number(warning)
            ValueChecker.is_number(critical)
        self.__config.append(f"{name}:{warning}:{critical}")

        return self

    def remove_config(self, name):
        ValueChecker.is_string(name)
        configs = []
        for config in self.__config:
            if not config.startswith(name):
                configs.append(config)
        self.__config = configs
        return self

    def set_host(self, host):
        ValueChecker.is_string(host)
        self.__host = host

        return self

    def get_host(self):
        return self.__host

    @staticmethod
    def create(id: str, force_create: bool = False):
        ValueChecker.validate_id(id)
        check = None if force_create else ConfigBuilder.get_check(id)
        if None is check:
            check = CheckMozillaObservatory(id)
            ConfigBuilder.add_check(id, check)
        elif not isinstance(check, CheckMozillaObservatory):
            raise Exception('Id must be for an instance of CheckMozillaObservatory but other instance is returned')

        if None is ConfigBuilder.get_command('monitoring_plugins_mozilla_observatory'):
            MozillaObservatoryCommand.create('monitoring_plugins_mozilla_observatory')

        return check

    def validate(self):
        Webrequest.validate(self)
        if None is self.__host:
            raise Exception('You have to specify a host for ' + self.get_id())

    def get_config(self) -> str:
        return Webrequest.get_config(self)

    def get_custom_config(self) -> str:
        # config = ValueMapper.parse_var('vars.allowed_ports', self.__allowed_ports)
        config = Webrequest.get_custom_config(self)

        return config
