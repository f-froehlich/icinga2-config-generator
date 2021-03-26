from icinga2confgen.Commands.NagiosPlugins.FlexlmCommand import FlexlmCommand
from tests.BaseCommandTest import BaseCommandTest


class TestFlexlmCommand(BaseCommandTest):

    def get_instance_class(self):
        return FlexlmCommand
