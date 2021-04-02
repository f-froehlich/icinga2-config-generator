from abc import abstractmethod

import pytest

from icinga2confgen.Checks.Check import Check
from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Servers.Zone import Zone
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

    def get_default_check_timeout(self) -> int:
        return 30

    def get_default_check_interval(self) -> str:
        return '1m'

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
        self.validate_snapshot = False
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
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            self.create_instance(True)

    def test_create_raise_exception_if_id_not_from_same_instance(self):
        command = Check('instance', 'class_name', 'command_name')
        ConfigBuilder.add_check('instance', command)

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            self.create_instance()

    def test_id(self):
        instance = self.create_instance()
        assert 'instance' == instance.get_id()

    def test_negate(self):
        instance = self.create_instance()
        instance.use_negation(True)
        assert instance.is_using_negation()

    def test_negate_substitute(self):
        instance = self.create_instance()
        instance.use_negation_substitute(True)
        assert instance.is_using_negation_substitute()

    def test_negate_status_ok(self):
        instance = self.create_instance()
        instance.set_ok_status('OK')
        assert 'OK' == instance.get_ok_status()

    def test_negate_status_unknown(self):
        instance = self.create_instance()
        instance.set_unknown_status('UNKNOWN')
        assert 'UNKNOWN' == instance.get_unknown_status()

    def test_negate_status_critical(self):
        instance = self.create_instance()
        instance.set_critical_status('CRITICAL')
        assert 'CRITICAL' == instance.get_critical_status()

    def test_negate_status_warning(self):
        instance = self.create_instance()
        instance.set_warning_status('WARNING')
        assert 'WARNING' == instance.get_warning_status()

    def test_negate_timeout(self):
        instance = self.create_instance()
        instance.set_negation_timeout(467)
        assert 467 == instance.get_negation_timeout()

    def test_check_negation_status_raise_exception_if_not_allowed(self):
        instance = self.create_instance()
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.check_negation_status('foo')

    def test_check_negation_status_allow_non_values(self):
        instance = self.create_instance()
        assert instance == instance.check_negation_status(None)

    def test_check_negation_status_allow_OK(self):
        instance = self.create_instance()
        assert instance == instance.check_negation_status('OK')

    def test_check_negation_status_allow_WARNING(self):
        instance = self.create_instance()
        assert instance == instance.check_negation_status('WARNING')

    def test_check_negation_status_allow_CRITICAL(self):
        instance = self.create_instance()
        assert instance == instance.check_negation_status('CRITICAL')

    def test_check_negation_status_allow_UNKNOWN(self):
        instance = self.create_instance()
        assert instance == instance.check_negation_status('UNKNOWN')

    def test_max_check_attempts(self):
        instance = self.create_instance()
        assert 3 == instance.get_max_check_attempts()
        instance.set_max_check_attempts(6)
        assert 6 == instance.get_max_check_attempts()

    def test_generated(self):
        instance = self.create_instance()
        assert not instance.is_generated()
        instance.set_generated(True)
        assert instance.is_generated()

    def test_check_timeout(self):
        instance = self.create_instance()
        assert self.get_default_check_timeout() == instance.get_check_timeout()
        instance.set_check_timeout(679)
        assert 679 == instance.get_check_timeout()

    def test_check_interval(self):
        instance = self.create_instance()
        assert self.get_default_check_interval() == instance.get_check_interval()
        instance.set_check_interval('225m')
        assert '225m' == instance.get_check_interval()

    def test_retry_interval(self):
        instance = self.create_instance()
        assert '15s' == instance.get_retry_interval()
        instance.set_retry_interval('225m')
        assert '225m' == instance.get_retry_interval()

    def test_enable_perfdata(self):
        instance = self.create_instance()
        assert instance.get_enable_perfdata()
        instance.set_enable_perfdata(False)
        assert not instance.get_enable_perfdata()

    def test_default_zone(self):
        instance = self.create_instance()
        assert None is instance.get_zone()
        zone = Zone.create('foo_zone')
        instance.set_zone(zone)
        assert zone == instance.get_zone()

    def test_set_zone(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_zone()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'zone-default.txt')
        zone = Zone.create('foo_zone')
        instance.set_zone(zone)
        assert zone == instance.get_zone()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'zone-foo.txt')
        zone2 = Zone.create('bar_zone')
        instance.set_zone(zone2.get_id())
        assert zone2 == instance.get_zone()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'zone-bar.txt')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.set_zone('invalid')

        assert 'Zone does not exist yet!' == str(excinfo.value)
        assert zone2 == instance.get_zone()

    def test_set_endpoint(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_endpoint()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no-endpoint.txt')
        instance.set_endpoint('endpoint')
        assert 'endpoint' == instance.get_endpoint()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'endpoint.txt')

    def test_display_name(self):
        instance = self.create_instance()
        instance.set_display_name('foo bar')
        assert 'foo bar' == instance.get_display_name()

    def test_validate_always_no_exception_on_valid_instances(self):
        instance = self.create_instance()
        instance.validate()

    @pytest.mark.parametrize(("check_type"), ['ssh', 'local'])
    def test_can_set_check_type(self, check_type):
        instance = self.create_instance()
        instance.set_check_type(check_type)
        assert check_type == instance.get_check_type()

    def test_cant_set_invalidcheck_type(self):
        instance = self.create_instance()
        self.validate_snapshot = False
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
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_config_negate(self, snapshot):
        instance = self.create_instance()
        instance.use_negation(True)
        instance.use_negation_substitute(True)
        instance.set_ok_status('OK')
        instance.set_warning_status('WARNING')
        instance.set_unknown_status('CRITICAL')
        instance.set_unknown_status('UNKNOWN')
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_config_negate_without_enable(self, snapshot):
        instance = self.create_instance()
        instance.use_negation_substitute(True)
        instance.set_ok_status('OK')
        instance.set_warning_status('WARNING')
        instance.set_unknown_status('CRITICAL')
        instance.set_unknown_status('UNKNOWN')
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_command_name(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_command_name().replace('  ', ''), 'command_name.txt')

    def test_group_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_group_config().replace('  ', ''), 'group_config.txt')

    def test_custom_property_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_custom_property_config().replace('  ', ''), 'custom_property_config.txt')

    def test_property_default_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_property_default_config().replace('  ', ''), 'property_default_config.txt')

    def test_custom_config(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_custom_config().replace('  ', ''), 'custom_config.txt')

    def test_get_custom_definitions(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(str(instance.get_custom_definitions()).replace('  ', ''), 'custom_definitions.txt')

    def test_config_builder_output(self, snapshot):
        self.create_instance()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')
