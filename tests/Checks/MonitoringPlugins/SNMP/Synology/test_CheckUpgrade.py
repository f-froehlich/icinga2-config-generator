from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckUpgrade import CheckUpgrade
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.UpgradeCommand import UpgradeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckUpgrade(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckUpgrade

    def get_command_class(self):
        return UpgradeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('updates'),
            ServiceGroup.create('snmp')
        ]
