from icinga2confgen.Commands.MonitoringPlugins.PageContentCommand import PageContentCommand
from icinga2confgen.Commands.MonitoringPlugins.SecurityObserver.MozillaObservatoryCommand import \
    MozillaObservatoryCommand
from tests.BaseCommandTest import BaseCommandTest


class TestPageContentCommand(BaseCommandTest):

    def get_instance_class(self):
        return MozillaObservatoryCommand
