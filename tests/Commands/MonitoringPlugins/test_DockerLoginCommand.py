from icinga2confgen.Commands.MonitoringPlugins.DockerLoginCommand import DockerLoginCommand
from tests.BaseCommandTest import BaseCommandTest


class TestDockerLoginCommand(BaseCommandTest):

    def get_instance_class(self):
        return DockerLoginCommand
