from icinga2confgen.Checks.NagiosPlugins.CheckSNMP import CheckSNMP
from icinga2confgen.Commands.NagiosPlugins.SNMPCommand import SNMPCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSNMP(BaseCheckTest):

    def get_instance_class(self):
        return CheckSNMP

    def get_command_class(self):
        return SNMPCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('snmp'),
            ServiceGroup.create('network'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_oids('oid')
        return instance
