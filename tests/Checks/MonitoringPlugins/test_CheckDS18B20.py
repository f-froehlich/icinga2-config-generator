from icinga2confgen.Checks.MonitoringPlugins.CheckDS18B20 import CheckDS18B20
from icinga2confgen.Commands.MonitoringPlugins.DS18B20Command import DS18B20Command
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckDS18B20(BaseCheckTest):

    def get_instance_class(self):
        return CheckDS18B20

    def get_command_class(self):
        return DS18B20Command

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('temperature'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_device('device')
        return instance
