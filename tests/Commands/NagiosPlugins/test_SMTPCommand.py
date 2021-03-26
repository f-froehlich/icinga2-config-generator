from icinga2confgen.Commands.NagiosPlugins.SMTPCommand import SMTPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSMTPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SMTPCommand
