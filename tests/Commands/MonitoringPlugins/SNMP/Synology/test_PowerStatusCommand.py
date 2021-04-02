from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.PowerStatusCommand import PowerStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPowerStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return PowerStatusCommand
