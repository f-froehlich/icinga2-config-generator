from icinga2confgen.Commands.MonitoringPlugins.PageContentCommand import PageContentCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPageContentCommand(BaseCommandTest):

    def get_instance_class(self):
        return PageContentCommand
