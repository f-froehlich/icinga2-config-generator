from abc import abstractmethod

import pytest

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Notification.NotificationCommand import NotificationCommand
from tests.BaseTest import BaseTest


class BaseNotificationCommandTest(BaseTest):

    @abstractmethod
    def get_script_dir(self):
        raise NotImplementedError()

    @abstractmethod
    def get_command_executable_service(self):
        raise NotImplementedError()

    @abstractmethod
    def get_command_executable_host(self):
        raise NotImplementedError()

    def test_can_get_instance_from_config_builder(self):
        instance = self.create_instance()
        assert instance == ConfigBuilder.get_notification_command('instance')

    def test_have_correct_script_dir(self):
        instance = self.create_instance()
        assert self.get_script_dir() == instance.get_script_dir()

    def test_have_correct_command_executable_service(self):
        instance = self.create_instance()
        assert self.get_command_executable_service() == instance.get_command_executable_service()

    def test_have_correct_command_executable_host(self):
        instance = self.create_instance()
        assert self.get_command_executable_host() == instance.get_command_executable_host()

    def test_instance_exist_in_config_builder_instances(self):
        instance = self.create_instance()
        assert instance in ConfigBuilder.get_instance('notification_commands')

    def test_create_always_return_same_instance_if_id_equals(self):
        instance1 = self.create_instance()
        instance2 = self.create_instance()
        assert instance1 == instance2

    def test_create_raise_exception_if_force_create_same_id(self):
        self.create_instance(True)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            self.create_instance(True)

    def test_create_raise_exception_if_id_not_from_same_instance(self):
        command = NotificationCommand('instance')
        ConfigBuilder.add_notification_command('instance', command)

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            self.create_instance(True)

    def test_id(self):
        instance = self.create_instance()
        assert 'instance' == instance.get_id()

    def test_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_arguments_host(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_arguments_host().replace('  ', ''), 'arguments_host.txt')

    def test_arguments_service(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_arguments_service().replace('  ', ''), 'arguments_service.txt')

    def test_get_command_definition_host(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command_definition_host().replace('  ', ''), 'command_definition_host.txt')

    def test_get_command_definition_service(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command_definition_service().replace('  ', ''),
                              'command_definition_service.txt')

    def test_get_default_arguments_host(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_default_arguments_host().replace('  ', ''),
                              'default_arguments_host.txt')

    def test_get_default_arguments_service(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_default_arguments_service().replace('  ', ''),
                              'default_arguments_service.txt')

    def test_get_default_vars_host(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_default_vars_host().replace('  ', ''),
                              'default_vars_host.txt')
    def test_get_default_vars_service(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_default_vars_service().replace('  ', ''),
                              'default_vars_service.txt')

    def test_config_builder_output(self, snapshot):
        self.create_instance()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')
