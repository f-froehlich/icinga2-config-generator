from icinga2confgen.Commands.MonitoringPlugins.UFWStatusCommand import UFWStatusCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUFWStatusCommand(BaseCommandTest):

    def get_instance_class(self):
        return UFWStatusCommand
