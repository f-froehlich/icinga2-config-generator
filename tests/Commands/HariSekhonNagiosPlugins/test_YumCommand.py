from icinga2confgen.Commands.HariSekhonNagiosPlugins.YumCommand import YumCommand
from tests.BaseCommandTest import BaseCommandTest


class TestYumCommand(BaseCommandTest):

    def get_instance_class(self):
        return YumCommand
