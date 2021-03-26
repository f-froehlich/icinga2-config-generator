from icinga2confgen.Checks.NagiosPlugins.CheckDHCP import CheckDHCP
from icinga2confgen.Commands.NagiosPlugins.DHCPCommand import DHCPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDHCP(BaseCheckTest):

    def get_instance_class(self):
        return CheckDHCP

    def get_command_class(self):
        return DHCPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('dhcp'),
            ServiceGroup.create('network'),
        ]
