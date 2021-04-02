from unittest import mock

import pytest

from icinga2confgen.Commands.MonitoringPlugins.NmapCommand import NmapCommand
from icinga2confgen.ConfigBuilder import ConfigBuilder


class TestNMAPCommand:

    @pytest.fixture(autouse=True)
    def configure(self):
        yield
        ConfigBuilder.reset()

    def get_command_mock(self):
        return 'get_command_mock'

    def __snapshot_match(self, snapshot, instance):
        with mock.patch.object(NmapCommand, 'get_command', new=self.get_command_mock):
            snapshot.assert_match(instance.get_arguments().replace('  ', ''), 'arguments.txt')
            snapshot.assert_match(instance.get_command_definition().replace('  ', ''), 'command_definitions.txt')
            snapshot.assert_match(instance.get_config_local().replace('  ', ''), 'config_local.txt')
            snapshot.assert_match(instance.get_config_local_negate().replace('  ', ''), 'config_local_negate.txt')
            snapshot.assert_match(instance.get_config_ssh().replace('  ', ''), 'config_ssh.txt')
            snapshot.assert_match(instance.get_config_ssh_negate().replace('  ', ''), 'config_ssh_negate.txt')
            snapshot.assert_match(instance.get_config().replace('  ', ''), 'config.txt')

    def test_create_raise_exception(self):
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            NmapCommand.create('instance')

        assert 'NmapCommand' in str(excinfo.value)

    def test_default_config(self, snapshot):
        instance = NmapCommand('instance', 'command_name')
        self.__snapshot_match(snapshot, instance)

    def test_single_host(self, snapshot):
        instance = NmapCommand('instance', 'command_name', single_host=False)
        self.__snapshot_match(snapshot, instance)

    def test_scan_udp(self, snapshot):
        instance = NmapCommand('instance', 'command_name', scan_udp=False)
        self.__snapshot_match(snapshot, instance)

    def test_scan_tcp(self, snapshot):
        instance = NmapCommand('instance', 'command_name', scan_tcp=False)
        self.__snapshot_match(snapshot, instance)

    def test_n(self, snapshot):
        instance = NmapCommand('instance', 'command_name', n=False)
        self.__snapshot_match(snapshot, instance)

    def test_R(self, snapshot):
        instance = NmapCommand('instance', 'command_name', R=False)
        self.__snapshot_match(snapshot, instance)

    def test_system_dns(self, snapshot):
        instance = NmapCommand('instance', 'command_name', system_dns=False)
        self.__snapshot_match(snapshot, instance)

    def test_traceroute(self, snapshot):
        instance = NmapCommand('instance', 'command_name', traceroute=False)
        self.__snapshot_match(snapshot, instance)

    def test_F(self, snapshot):
        instance = NmapCommand('instance', 'command_name', F=False)
        self.__snapshot_match(snapshot, instance)

    def test_r(self, snapshot):
        instance = NmapCommand('instance', 'command_name', r=False)
        self.__snapshot_match(snapshot, instance)

    def test_sV(self, snapshot):
        instance = NmapCommand('instance', 'command_name', sV=False)
        self.__snapshot_match(snapshot, instance)

    def test_version_light(self, snapshot):
        instance = NmapCommand('instance', 'command_name', version_light=False)
        self.__snapshot_match(snapshot, instance)

    def test_version_all(self, snapshot):
        instance = NmapCommand('instance', 'command_name', version_all=False)
        self.__snapshot_match(snapshot, instance)

    def test_version_trace(self, snapshot):
        instance = NmapCommand('instance', 'command_name', version_trace=False)
        self.__snapshot_match(snapshot, instance)

    def test_sC(self, snapshot):
        instance = NmapCommand('instance', 'command_name', sC=False)
        self.__snapshot_match(snapshot, instance)

    def test_script_trace(self, snapshot):
        instance = NmapCommand('instance', 'command_name', script_trace=False)
        self.__snapshot_match(snapshot, instance)

    def test_O(self, snapshot):
        instance = NmapCommand('instance', 'command_name', O=False)
        self.__snapshot_match(snapshot, instance)

    def test_osscan_guess(self, snapshot):
        instance = NmapCommand('instance', 'command_name', osscan_guess=False)
        self.__snapshot_match(snapshot, instance)

    def test_badsum(self, snapshot):
        instance = NmapCommand('instance', 'command_name', badsum=False)
        self.__snapshot_match(snapshot, instance)

    def test_ipv6(self, snapshot):
        instance = NmapCommand('instance', 'command_name', ipv6=False)
        self.__snapshot_match(snapshot, instance)

    def test_A(self, snapshot):
        instance = NmapCommand('instance', 'command_name', A=False)
        self.__snapshot_match(snapshot, instance)

    def test_send_eth(self, snapshot):
        instance = NmapCommand('instance', 'command_name', send_eth=False)
        self.__snapshot_match(snapshot, instance)

    def test_send_ip(self, snapshot):
        instance = NmapCommand('instance', 'command_name', send_ip=False)
        self.__snapshot_match(snapshot, instance)

    def test_privileged(self, snapshot):
        instance = NmapCommand('instance', 'command_name', privileged=False)
        self.__snapshot_match(snapshot, instance)

    def test_Pn(self, snapshot):
        instance = NmapCommand('instance', 'command_name', Pn=False)
        self.__snapshot_match(snapshot, instance)

    def test_unprivileged(self, snapshot):
        instance = NmapCommand('instance', 'command_name', unprivileged=False)
        self.__snapshot_match(snapshot, instance)
