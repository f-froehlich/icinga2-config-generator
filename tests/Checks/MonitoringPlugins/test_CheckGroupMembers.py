from icinga2confgen.Checks.MonitoringPlugins.CheckGroupMembers import CheckGroupMembers
from icinga2confgen.Commands.MonitoringPlugins.GroupMembersCommand import GroupMembersCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckGroupMembers(BaseCheckTest):

    def get_instance_class(self):
        return CheckGroupMembers

    def get_command_class(self):
        return GroupMembersCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('security'),
            ServiceGroup.create('group_members'),
        ]
