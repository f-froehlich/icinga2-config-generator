import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.UCD_DISKIO_MIB.CheckLoad import CheckLoad
from icinga2confgen.Commands.MonitoringPlugins.SNMP.UCD_DISKIO_MIB.LoadCommand import LoadCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckLoad(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckLoad

    def get_command_class(self):
        return LoadCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('disk'),
            ServiceGroup.create('system_health'),
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

    def test_get_right_disk(self):
        instance = self.create_instance()
        instance.set_disks(57)

        assert 57 == instance.get_disks()

    def test_get_right_warning(self):
        instance = self.create_instance()
        assert None is instance.get_warning()
        instance.set_warning(44, 67, 77)

        assert 44 == instance.get_warning()[0]
        assert 67 == instance.get_warning()[1]
        assert 77 == instance.get_warning()[2]

    def test_get_right_critical(self):
        instance = self.create_instance()
        assert None is instance.get_critical()
        instance.set_critical(55, 75, 112)

        assert 55 == instance.get_critical()[0]
        assert 75 == instance.get_critical()[1]
        assert 112 == instance.get_critical()[2]
