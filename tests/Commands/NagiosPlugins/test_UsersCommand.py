from icinga2confgen.Commands.NagiosPlugins.UsersCommand import UsersCommand
from tests.BaseCommandTest import BaseCommandTest


class TestUsersCommand(BaseCommandTest):

    def get_instance_class(self):
        return UsersCommand
