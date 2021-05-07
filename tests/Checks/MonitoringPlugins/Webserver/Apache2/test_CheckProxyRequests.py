from icinga2confgen.Checks.MonitoringPlugins.Webserver.Apache2.CheckProxyRequests import CheckProxyRequests
from icinga2confgen.Commands.MonitoringPlugins.Webserver.Apache2.ProxyRequestsCommand import ProxyRequestsCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckProxyRequests(BaseCheckTest):

    def get_instance_class(self):
        return CheckProxyRequests

    def get_command_class(self):
        return ProxyRequestsCommand

    def get_default_check_interval(self) -> str:
        return '24h'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('webserver'),
            ServiceGroup.create('security'),
        ]


    def test_add_allow(self):
        instance = self.create_instance()

        assert 0 == len(instance.get_allow())

        instance.add_allow('foo')
        assert 1 == len(instance.get_allow())
        assert 'foo' in instance.get_allow()

        instance.add_allow('foo')
        assert 1 == len(instance.get_allow())
        assert 'foo' in instance.get_allow()

        instance.remove_allow('bar')
        assert 1 == len(instance.get_allow())
        assert 'foo' in instance.get_allow()

        instance.remove_allow('foo')
        assert 0 == len(instance.get_allow())

        allow = ['foo', 'bar']
        instance.set_allow(allow)
        assert allow == instance.get_allow()

