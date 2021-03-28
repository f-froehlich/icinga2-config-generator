from icinga2confgen.Checks.HariSekhonNagiosPlugins.CheckYum import CheckYum
from icinga2confgen.Commands.HariSekhonNagiosPlugins.YumCommand import YumCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckYum(BaseCheckTest):

    def get_instance_class(self):
        return CheckYum

    def get_command_class(self):
        return YumCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('yum'),
            ServiceGroup.create('updates'),
        ]
