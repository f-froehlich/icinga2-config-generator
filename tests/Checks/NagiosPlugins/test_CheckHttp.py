from icinga2confgen.Checks.NagiosPlugins.CheckHttp import CheckHttp
from icinga2confgen.Commands.NagiosPlugins.HttpCommand import HttpCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckHttp(BaseCheckTest):

    def get_instance_class(self):
        return CheckHttp

    def get_command_class(self):
        return HttpCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('webserver'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_vhost('host')
        return instance
