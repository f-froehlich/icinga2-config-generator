from icinga2confgen.Commands.MonitoringPlugins.Git.GithubLatestReleaseCommand import GithubLatestReleaseCommand
from tests.BaseCommandTest import BaseCommandTest


class TestSPFCommand(BaseCommandTest):

    def get_instance_class(self):
        return GithubLatestReleaseCommand
