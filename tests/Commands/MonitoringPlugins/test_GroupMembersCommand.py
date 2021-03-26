from icinga2confgen.Commands.MonitoringPlugins.GroupMembersCommand import GroupMembersCommand
from tests.BaseCommandTest import BaseCommandTest


class TestGroupMembersCommand(BaseCommandTest):

    def get_instance_class(self):
        return GroupMembersCommand
