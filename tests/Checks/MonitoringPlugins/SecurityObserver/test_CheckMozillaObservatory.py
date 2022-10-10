from icinga2confgen.Checks.MonitoringPlugins.SecurityObserver.CheckMozillaObservatory import CheckMozillaObservatory
from icinga2confgen.Commands.MonitoringPlugins.SecurityObserver.MozillaObservatoryCommand import \
    MozillaObservatoryCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckMozillaObservatory(BaseCheckTest):

    def get_instance_class(self):
        return CheckMozillaObservatory

    def get_command_class(self):
        return MozillaObservatoryCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('webserver'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('domain')
        return instance
