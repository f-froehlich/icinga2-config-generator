from icinga2confgen.Commands.MonitoringPlugins.CiphersCommand import CiphersCommand
from tests.BaseNMAPCommandTest import BaseNMAPCommandTest


class TestCiphersCommand(BaseNMAPCommandTest):

    def get_instance_class(self):
        return CiphersCommand
