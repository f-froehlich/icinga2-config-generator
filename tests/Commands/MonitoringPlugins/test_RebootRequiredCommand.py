from icinga2confgen.Commands.MonitoringPlugins.RebootRequiredCommand import RebootRequiredCommand
from tests.BaseCommandTest import BaseCommandTest


class TestRebootRequiredCommand(BaseCommandTest):

    def get_instance_class(self):
        return RebootRequiredCommand
