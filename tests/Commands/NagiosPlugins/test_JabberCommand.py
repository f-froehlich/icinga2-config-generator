from icinga2confgen.Commands.NagiosPlugins.JabberCommand import JabberCommand
from tests.BaseCommandTest import BaseCommandTest


class TestJabberCommand(BaseCommandTest):

    def get_instance_class(self):
        return JabberCommand
