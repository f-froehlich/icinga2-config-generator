from icinga2confgen.Checks.NagiosPlugins.CheckProcs import CheckProcs
from icinga2confgen.Commands.NagiosPlugins.ProcsCommand import ProcsCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckProcs(BaseCheckTest):

    def get_instance_class(self):
        return CheckProcs

    def get_command_class(self):
        return ProcsCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('procs'),
            ServiceGroup.create('system_health'),
        ]
