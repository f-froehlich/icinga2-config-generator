from icinga2confgen.Checks.NagiosPlugins.CheckSWAP import CheckSWAP
from icinga2confgen.Commands.NagiosPlugins.SWAPCommand import SWAPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSWAP(BaseCheckTest):

    def get_instance_class(self):
        return CheckSWAP

    def get_command_class(self):
        return SWAPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('swap'),
            ServiceGroup.create('system_health'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_warning(30)
        instance.set_critical(40)
        return instance
