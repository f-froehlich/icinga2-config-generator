import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.PowerNet_MIB.CheckBatteryPacksAttached import \
    CheckBatteryPacksAttached
from icinga2confgen.Commands.MonitoringPlugins.SNMP.PowerNet_MIB.BatteryPacksAttachedCommand import \
    BatteryPacksAttachedCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckBatteryPacksAttached(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckBatteryPacksAttached

    def get_command_class(self):
        return BatteryPacksAttachedCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ups'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_count(22)
        return instance

    def test_get_right_count(self):
        instance = self.create_instance()
        instance.set_count(23)

        assert 23 == instance.get_count()

    def test_raise_exception_on_missing_count(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'You have to set the number of attached battery packs!' == str(excinfo.value)
