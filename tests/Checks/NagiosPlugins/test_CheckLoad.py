from icinga2confgen.Checks.NagiosPlugins.CheckLoad import CheckLoad
from icinga2confgen.Commands.NagiosPlugins.LoadCommand import LoadCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckLoad(BaseCheckTest):

    def get_instance_class(self):
        return CheckLoad

    def get_command_class(self):
        return LoadCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('system_health'),
            ServiceGroup.create('load'),
        ]
