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

from icinga2confgen.ValueChecker import ValueChecker
from icinga2confgen.ValueMapper import ValueMapper


class NotificationFunctions:

    def __init__(self):
        self.__email = []
        self.__phone = []
        self.__pager = []
        self.__telegram = []

    def add_email(self, email):
        ValueChecker.is_string(email)
        if email not in self.__email:
            self.__email.append(email)
        return self

    def remove_email(self, email):
        ValueChecker.is_string(email)
        self.__email.remove(email)
        return self

    def get_email(self):
        return self.__email

    def add_telegram_id(self, telegram_id):
        ValueChecker.is_number(telegram_id)
        if telegram_id not in self.__telegram:
            self.__telegram.append(telegram_id)
        return self

    def remove_telegram_id(self, telegram_id):
        ValueChecker.is_number(telegram_id)
        self.__telegram.remove(telegram_id)
        return self

    def get_telegram_id(self):
        return self.__telegram

    def add_pager(self, pager):
        ValueChecker.is_string(pager)
        if pager not in self.__pager:
            self.__pager.append(pager)
        return self

    def remove_pager(self, pager):
        ValueChecker.is_string(pager)
        self.__pager.remove(pager)
        return self

    def get_pager(self):
        return self.__pager

    def add_phone(self, phone):
        ValueChecker.is_string(phone)
        if phone not in self.__phone:
            self.__phone.append(phone)
        return self

    def get_phone(self):
        return self.__phone

    def remove_phone(self, phone):
        ValueChecker.is_string(phone)
        self.__phone.remove(phone)
        return self

    def get_config(self):
        config = ValueMapper.parse_var('vars.email_addresses', self.__email)
        config += ValueMapper.parse_var('pager', self.__pager)
        config += ValueMapper.parse_var('vars.phone', self.__phone)

        return config
