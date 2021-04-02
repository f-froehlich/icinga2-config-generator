import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckDiskTemperature import CheckDiskTemperature
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.DiskTemperatureCommand import DiskTemperatureCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckDiskTemperature(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckDiskTemperature

    def get_command_class(self):
        return DiskTemperatureCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('disk'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_disks(22)
        return instance

    def test_validate_raise_exception_on_missing_disks(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        instance.set_host('host')
        instance.set_username('user')
        instance.set_password('pwd')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

    def test_get_right_disks(self):
        instance = self.create_instance()
        instance.set_disks(5)

        assert 5 == instance.get_disks()

    def test_get_right_warning(self):
        instance = self.create_instance()
        instance.set_warning(44)

        assert 44 == instance.get_warning()

    def test_get_right_critical(self):
        instance = self.create_instance()
        instance.set_critical(55)

        assert 55 == instance.get_critical()
