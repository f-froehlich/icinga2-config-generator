from icinga2confgen.Commands.MonitoringPlugins.Webserver.Apache2.ProxyRequestsCommand import ProxyRequestsCommand
from tests.BaseCommandTest import BaseCommandTest


class TestProxyRequestsCommand(BaseCommandTest):

    def get_instance_class(self):
        return ProxyRequestsCommand
