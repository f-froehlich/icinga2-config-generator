from abc import abstractmethod

import pytest

from icinga2confgen.Checks.Check import Check
from icinga2confgen.ConfigBuilder import ConfigBuilder
from tests.BaseTest import BaseTest


class BaseCheckTest(BaseTest):

    @abstractmethod
    def get_instance_class(self):
        raise NotImplementedError()

    @abstractmethod
    def get_command_class(self):
        raise NotImplementedError()

    @abstractmethod
    def get_default_service_groups(self):
        raise NotImplementedError()

    def create_instance(self, force=False):
        return self.get_instance_class().create('instance', force_create=force)

    def test_get_right_command_instance(self):
        instance = self.create_instance()
        commands = ConfigBuilder.get_instance('commands')

        assert len(commands) == 1

        command_instance = commands[0]
        assert instance.get_command_name() in command_instance.get_id()
        assert isinstance(command_instance, self.get_command_class())

    def test_only_create_command_instance_once(self):
        instance = self.create_instance()
        instance2 = self.get_instance_class().create('instance2')
        commands = ConfigBuilder.get_instance('commands')

        assert len(commands) == 1

        command_instance = commands[0]
        assert instance.get_command_name() in command_instance.get_id()
        assert instance2.get_command_name() in command_instance.get_id()
        assert isinstance(command_instance, self.get_command_class())

    def test_can_get_instance_from_config_builder(self):
        instance = self.create_instance()
        assert instance == ConfigBuilder.get_check('instance')

    def test_instance_exist_in_config_builder_instances(self):
        instance = self.create_instance()
        assert instance in ConfigBuilder.get_instance('checks')

    def test_create_always_return_same_instance_if_id_equals(self):
        instance1 = self.create_instance()
        instance2 = self.create_instance()
        assert instance1 == instance2

    def test_create_raise_exception_if_force_create_same_id(self):
        self.create_instance(True)
        with pytest.raises(Exception) as excinfo:
            self.create_instance(True)

    def test_create_raise_exception_if_id_not_from_same_instance(self):
        command = Check('instance', 'class_name', 'command_name')
        ConfigBuilder.add_check('instance', command)

        with pytest.raises(Exception) as excinfo:
            self.create_instance()

    def test_id(self):
        instance = self.create_instance()
        assert 'instance' == instance.get_id()

    def test_validate_always_no_exception_on_valid_instances(self):
        instance = self.create_instance()
        instance.validate()

    @pytest.mark.parametrize(("check_type"), [
        ('ssh'),
        ('local'),
    ])
    def test_can_set_check_type(self, check_type):
        instance = self.create_instance()
        instance.set_check_type(check_type)
        assert check_type == instance.get_check_type()

    def test_cant_set_invalidcheck_type(self):
        instance = self.create_instance()
        with pytest.raises(Exception) as excinfo:
            instance.set_check_type('invalid')

    def test_default_service_groups(self):
        instance = self.create_instance()
        assert len(self.get_default_service_groups()) == len(instance.get_service_groups())

        for sg in self.get_default_service_groups():
            assert sg in instance.get_service_groups()
        for sg in instance.get_service_groups():
            assert sg in self.get_default_service_groups()

    def test_dont_add_same_service_group(self):
        instance = self.create_instance()
        assert len(self.get_default_service_groups()) == len(instance.get_service_groups())

        for sg in self.get_default_service_groups():
            instance.add_service_group(sg)
            instance.add_service_group(sg.get_id())

        assert len(self.get_default_service_groups()) == len(instance.get_service_groups())

        for sg in self.get_default_service_groups():
            assert sg in instance.get_service_groups()
        for sg in instance.get_service_groups():
            assert sg in self.get_default_service_groups()

    def test_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_config(), 'config.txt')

    def test_command_name(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command_name(), 'command_name.txt')

    def test_group_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_group_config(), 'group_config.txt')

    def test_custom_property_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_custom_property_config(), 'custom_property_config.txt')

    def test_property_default_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_property_default_config(), 'property_default_config.txt')

    def test_custom_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_custom_config(), 'custom_config.txt')

    def test_get_custom_definitions(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(str(instance.get_custom_definitions()), 'custom_definitions.txt')

    # def test_arguments(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_arguments(), 'arguments.txt')
    #
    # def test_config_local(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_config_local(), 'config.txt')
    #
    # def test_config_local_negate(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_config_local_negate(), 'config.txt')
    #
    # def test_config_ssh(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_config_ssh(), 'config.txt')
    #
    # def test_config_ssh_negate(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_config_ssh_negate(), 'config.txt')
    #
    # def test_command_definition(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_command_definition(), 'command_definition.txt')
    #
    # def test_command(self, snapshot):
    #     instance = self.create_instance()
    #     snapshot.assert_match(instance.get_command(), 'command.txt')

    def test_config_builder_output(self, snapshot):
        self.create_instance()
        snapshot.assert_match(ConfigBuilder.get_config_as_string(), 'config.txt')
