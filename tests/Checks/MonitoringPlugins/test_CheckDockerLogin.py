from icinga2confgen.Checks.MonitoringPlugins.CheckDockerLogin import CheckDockerLogin
from icinga2confgen.Commands.MonitoringPlugins.DockerLoginCommand import DockerLoginCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDockerLogin(BaseCheckTest):

    def get_instance_class(self):
        return CheckDockerLogin

    def get_command_class(self):
        return DockerLoginCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('docker'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_address('host')
        instance.set_port('8888')
        instance.set_user('user')
        instance.set_credentials('pwd')
        return instance
