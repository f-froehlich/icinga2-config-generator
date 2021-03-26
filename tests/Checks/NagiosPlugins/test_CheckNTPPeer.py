from icinga2confgen.Checks.NagiosPlugins.CheckNTPPeer import CheckNTPPeer
from icinga2confgen.Commands.NagiosPlugins.NTPPeerCommand import NTPPeerCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckNTPPeer(BaseCheckTest):

    def get_instance_class(self):
        return CheckNTPPeer

    def get_command_class(self):
        return NTPPeerCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('ntp'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_ntp_server('ntp_server')
        return instance
