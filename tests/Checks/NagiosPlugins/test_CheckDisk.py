from icinga2confgen.Checks.NagiosPlugins.CheckDisk import CheckDisk
from icinga2confgen.Commands.NagiosPlugins.DiskCommand import DiskCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDisk(BaseCheckTest):

    def get_instance_class(self):
        return CheckDisk

    def get_command_class(self):
        return DiskCommand

    def get_default_check_interval(self) -> str:
        return '30m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('disk'),
        ]
