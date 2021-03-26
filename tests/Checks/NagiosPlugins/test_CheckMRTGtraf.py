from icinga2confgen.Checks.NagiosPlugins.CheckMRTGtraf import CheckMRTGtraf
from icinga2confgen.Commands.NagiosPlugins.MRTGtrafCommand import MRTGtrafCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckMRTGtraf(BaseCheckTest):

    def get_instance_class(self):
        return CheckMRTGtraf

    def get_command_class(self):
        return MRTGtrafCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('mrt_gtraf'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_warning('30')
        instance.set_critical('40')
        instance.set_file('file')
        instance.set_aggregation('aggregation')
        return instance
