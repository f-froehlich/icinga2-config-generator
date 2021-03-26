from icinga2confgen.Checks.MonitoringPlugins.CheckPageContent import CheckPageContent
from icinga2confgen.Commands.MonitoringPlugins.PageContentCommand import PageContentCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckPageContent(BaseCheckTest):

    def get_instance_class(self):
        return CheckPageContent

    def get_command_class(self):
        return PageContentCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('webserver'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_domain('domain')
        return instance
