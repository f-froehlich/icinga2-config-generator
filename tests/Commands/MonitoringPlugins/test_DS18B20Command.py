from icinga2confgen.Commands.MonitoringPlugins.DS18B20Command import DS18B20Command
from tests.BaseCommandTest import BaseCommandTest


class TestDS18B20Command(BaseCommandTest):

    def get_instance_class(self):
        return DS18B20Command
