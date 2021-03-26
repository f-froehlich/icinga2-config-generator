from icinga2confgen.Commands.NagiosPlugins.SSMTPCommand import SSMTPCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSSMTPCommand(BaseCommandTest):

    def get_instance_class(self):
        return SSMTPCommand
