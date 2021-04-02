from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.UpgradeCommand import UpgradeCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUpgradeCommand(BaseCommandTest):

    def get_instance_class(self):
        return UpgradeCommand
