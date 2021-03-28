from icinga2confgen.Checks.MonitoringPlugins.CheckExistingUsers import CheckExistingUsers
from icinga2confgen.Commands.MonitoringPlugins.ExistingUsersCommand import ExistingUsersCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckExistingUsers(BaseCheckTest):

    def get_instance_class(self):
        return CheckExistingUsers

    def get_command_class(self):
        return ExistingUsersCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('security'),
            ServiceGroup.create('existing_user'),
        ]
