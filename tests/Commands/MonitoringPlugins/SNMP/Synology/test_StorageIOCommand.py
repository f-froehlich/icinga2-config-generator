from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.StorageIOCommand import StorageIOCommand
from tests.BaseCommandTest import BaseCommandTest


class TestStorageIOCommand(BaseCommandTest):

    def get_instance_class(self):
        return StorageIOCommand
