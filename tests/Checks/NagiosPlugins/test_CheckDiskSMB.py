from icinga2confgen.Checks.NagiosPlugins.CheckDiskSMB import CheckDiskSMB
from icinga2confgen.Commands.NagiosPlugins.DiskSMBCommand import DiskSMBCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDiskSMB(BaseCheckTest):

    def get_instance_class(self):
        return CheckDiskSMB

    def get_command_class(self):
        return DiskSMBCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('disk'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_share('share')
        instance.set_ip('ip')
        instance.set_user('user')
        instance.set_password('password')
        return instance
