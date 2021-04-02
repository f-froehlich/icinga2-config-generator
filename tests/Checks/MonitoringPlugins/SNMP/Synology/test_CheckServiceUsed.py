import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckServiceUsed import CheckServiceUsed
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceUsedCommand import ServiceUsedCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckServiceUsed(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckServiceUsed

    def get_command_class(self):
        return ServiceUsedCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_service('service')
        instance.set_warning(33)
        instance.set_critical(88)
        return instance

    def test_validate_raise_exception_on_missing_service(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'service' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_warning(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        instance.set_service('service')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'warning' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_critical(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        instance.set_service('service')
        instance.set_warning(44)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'critical' in str(excinfo.value)

    def test_get_right_service(self):
        instance = self.create_instance()
        instance.set_service('service')

        assert 'service' == instance.get_service()

    def test_get_right_warning(self):
        instance = self.create_instance()
        instance.set_warning(44)

        assert 44 == instance.get_warning()

    def test_get_right_critical(self):
        instance = self.create_instance()
        instance.set_critical(55)

        assert 55 == instance.get_critical()
