from icinga2confgen.Commands.MatteocortiPlugins.CheckSSLCertCommand import CheckSSLCertCommand
from tests.BaseCommandTest import BaseCommandTest


class TestCheckSSLCertCommand(BaseCommandTest):

    def get_instance_class(self):
        return CheckSSLCertCommand
