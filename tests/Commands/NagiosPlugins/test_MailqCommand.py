from icinga2confgen.Commands.NagiosPlugins.MailqCommand import MailqCommand
from tests.BaseCommandTest import BaseCommandTest


class TestMailqCommand(BaseCommandTest):

    def get_instance_class(self):
        return MailqCommand
