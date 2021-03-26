from icinga2confgen.Checks.NagiosPlugins.CheckFileAge import CheckFileAge
from icinga2confgen.Commands.NagiosPlugins.FileAgeCommand import FileAgeCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckFileAge(BaseCheckTest):

    def get_instance_class(self):
        return CheckFileAge

    def get_command_class(self):
        return FileAgeCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('file_age'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_file('file')
        instance.set_warning_seconds(60)
        instance.set_critical_seconds(600)
        return instance
