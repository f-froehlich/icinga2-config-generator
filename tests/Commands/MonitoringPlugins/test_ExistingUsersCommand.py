from icinga2confgen.Commands.MonitoringPlugins.ExistingUsersCommand import ExistingUsersCommand
from tests.BaseCommandTest import BaseCommandTest


class TestExistingUsersCommand(BaseCommandTest):

    def get_instance_class(self):
        return ExistingUsersCommand
