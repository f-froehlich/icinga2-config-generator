from icinga2confgen.Commands.MonitoringPlugins.PathExistsCommand import PathExistsCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPathExistsCommand(BaseCommandTest):

    def get_instance_class(self):
        return PathExistsCommand
