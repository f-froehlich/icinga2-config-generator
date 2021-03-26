from icinga2confgen.Checks.MonitoringPlugins.CheckPathExists import CheckPathExists
from icinga2confgen.Commands.MonitoringPlugins.PathExistsCommand import PathExistsCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckPathExists(BaseCheckTest):

    def get_instance_class(self):
        return CheckPathExists

    def get_command_class(self):
        return PathExistsCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('path_exists'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_file('file')
        return instance
