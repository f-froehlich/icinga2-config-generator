import pytest

from icinga2confgen.Commands.Command import Command
from icinga2confgen.ConfigBuilder import ConfigBuilder
from tests.BaseTest import BaseTest


class BaseCommandTest(BaseTest):

    def test_can_get_instance_from_config_builder(self):
        instance = self.create_instance()
        assert instance == ConfigBuilder.get_command('instance')

    def test_instance_exist_in_config_builder_instances(self):
        instance = self.create_instance()
        assert instance in ConfigBuilder.get_instance('commands')

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
        command = Command('instance')
        ConfigBuilder.add_command('instance', command)

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            self.create_instance()

    def test_id(self):
        instance = self.create_instance()
        assert 'instance' == instance.get_id()

    def test_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_arguments(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_arguments().replace('  ', ''), 'arguments.txt')

    def test_config_local(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config_local(), 'config.txt')

    def test_config_local_negate(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config_local_negate().replace('  ', ''), 'config.txt')

    def test_config_ssh(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config_ssh(), 'config.txt')

    def test_config_ssh_negate(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config_ssh_negate().replace('  ', ''), 'config.txt')

    def test_command_definition(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command_definition(), 'command_definition.txt')

    def test_command(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command().replace('  ', ''), 'command.txt')

    def test_config_builder_output(self, snapshot):
        self.create_instance()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')
