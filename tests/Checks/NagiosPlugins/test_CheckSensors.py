from icinga2confgen.Checks.NagiosPlugins.CheckSensors import CheckSensors
from icinga2confgen.Commands.NagiosPlugins.SensorsCommand import SensorsCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSensors(BaseCheckTest):

    def get_instance_class(self):
        return CheckSensors

    def get_command_class(self):
        return SensorsCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('sensors'),
            ServiceGroup.create('system_health'),
        ]
