import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckSMART import CheckSMART
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.SMARTCommand import SMARTCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckSMART(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckSMART

    def get_command_class(self):
        return SMARTCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('disk'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_disk(5)
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
        instance.set_disk(23)

        assert 23 == instance.get_disk()
