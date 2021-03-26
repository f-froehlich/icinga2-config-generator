from icinga2confgen.Checks.NagiosPlugins.CheckNTPTime import CheckNTPTime
from icinga2confgen.Commands.NagiosPlugins.NTPTimeCommand import NTPTimeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckNTPTime(BaseCheckTest):

    def get_instance_class(self):
        return CheckNTPTime

    def get_command_class(self):
        return NTPTimeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ntp'),
            ServiceGroup.create('network'),
        ]
