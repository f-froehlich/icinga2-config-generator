from icinga2confgen.Checks.NagiosPlugins.CheckUsers import CheckUsers
from icinga2confgen.Commands.NagiosPlugins.UsersCommand import UsersCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckUsers(BaseCheckTest):

    def get_instance_class(self):
        return CheckUsers

    def get_command_class(self):
        return UsersCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('user')
        ]
