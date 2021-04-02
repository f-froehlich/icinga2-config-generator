import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.Synology.CheckServiceRunning import CheckServiceRunning
from icinga2confgen.Commands.MonitoringPlugins.SNMP.Synology.ServiceRunningCommand import ServiceRunningCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckServiceRunning(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckServiceRunning

    def get_command_class(self):
        return ServiceRunningCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.add_service('service')
        return instance

    def test_validate_raise_exception_on_missing_service(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        instance.set_host('host')
        instance.set_username('user')
        instance.set_password('pwd')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

    def test_set_services(self):
        instance = self.create_instance()
        services = ['service1', 'service2']
        instance.set_services(services)

        assert services == instance.get_services()

    def test_remove_services(self):
        instance = self.create_instance()
        services = ['service1', 'service2']
        instance.set_services(services)

        assert services == instance.get_services()
        instance.remove_service('service1')
        assert 1 == len(instance.get_services())
        assert 'service2' in instance.get_services()

    def test_add_service(self):
        instance = BaseCheckSNMPTest.create_instance(self)

        assert 0 == len(instance.get_services())
        instance.add_service('service1')
        assert 1 == len(instance.get_services())
        assert 'service1' in instance.get_services()
        instance.add_service('service2')
        assert 2 == len(instance.get_services())
        assert 'service1' in instance.get_services()
        assert 'service2' in instance.get_services()
