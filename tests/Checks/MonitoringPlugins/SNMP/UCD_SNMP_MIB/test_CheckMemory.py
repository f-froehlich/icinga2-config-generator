import pytest

from icinga2confgen.Checks.MonitoringPlugins.SNMP.UCD_SNMP_MIB.CheckMemory import CheckMemory
from icinga2confgen.Commands.MonitoringPlugins.SNMP.UCD_SNMP_MIB.MemoryCommand import MemoryCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckSNMPTest import BaseCheckSNMPTest


class TestCheckMemory(BaseCheckSNMPTest):

    def get_instance_class(self):
        return CheckMemory

    def get_command_class(self):
        return MemoryCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('memory'),
            ServiceGroup.create('system_health'),
            ServiceGroup.create('snmp')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckSNMPTest.create_instance(self, force)
        instance.set_memory(22)
        return instance

    def test_validate_raise_exception_on_missing_memory(self):
        instance = BaseCheckSNMPTest.create_instance(self)
        instance.set_host('host')
        instance.set_username('user')
        instance.set_password('pwd')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

    def test_get_right_memory(self):
        instance = self.create_instance()
        instance.set_memory(976)

        assert 976 == instance.get_memory()

    def test_get_right_warning_total(self):
        instance = self.create_instance()
        instance.set_warning_total(44)

        assert 44 == instance.get_warning_total()

    def test_get_right_critical_total(self):
        instance = self.create_instance()
        instance.set_critical_total(55)

        assert 55 == instance.get_critical_total()

    def test_get_right_ignore_total(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_total()

        instance.set_ignore_total(True)
        assert instance.get_ignore_total()

        instance.set_ignore_total(False)
        assert not instance.get_ignore_total()

    def test_get_right_warning_swap(self):
        instance = self.create_instance()
        instance.set_warning_swap(44)

        assert 44 == instance.get_warning_swap()

    def test_get_right_critical_swap(self):
        instance = self.create_instance()
        instance.set_critical_swap(55)

        assert 55 == instance.get_critical_swap()

    def test_get_right_ignore_swap(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_swap()

        instance.set_ignore_swap(True)
        assert instance.get_ignore_swap()

        instance.set_ignore_swap(False)
        assert not instance.get_ignore_swap()

    def test_get_right_warning_swap_txt(self):
        instance = self.create_instance()
        instance.set_warning_swap_txt(44)

        assert 44 == instance.get_warning_swap_txt()

    def test_get_right_critical_swap_txt(self):
        instance = self.create_instance()
        instance.set_critical_swap_txt(55)

        assert 55 == instance.get_critical_swap_txt()

    def test_get_right_ignore_swap_txt(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_swap_txt()

        instance.set_ignore_swap_txt(True)
        assert instance.get_ignore_swap_txt()

        instance.set_ignore_swap_txt(False)
        assert not instance.get_ignore_swap_txt()

    def test_get_right_warning_real(self):
        instance = self.create_instance()
        instance.set_warning_real(44)

        assert 44 == instance.get_warning_real()

    def test_get_right_critical_real(self):
        instance = self.create_instance()
        instance.set_critical_real(55)

        assert 55 == instance.get_critical_real()

    def test_get_right_ignore_real(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_real()

        instance.set_ignore_real(True)
        assert instance.get_ignore_real()

        instance.set_ignore_real(False)
        assert not instance.get_ignore_real()

    def test_get_right_warning_real_txt(self):
        instance = self.create_instance()
        instance.set_warning_real_txt(44)

        assert 44 == instance.get_warning_real_txt()

    def test_get_right_critical_real_txt(self):
        instance = self.create_instance()
        instance.set_critical_real_txt(55)

        assert 55 == instance.get_critical_real_txt()

    def test_get_right_ignore_real_txt(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_real_txt()

        instance.set_ignore_real_txt(True)
        assert instance.get_ignore_real_txt()

        instance.set_ignore_real_txt(False)
        assert not instance.get_ignore_real_txt()

    def test_get_right_warning_shared(self):
        instance = self.create_instance()
        instance.set_warning_shared(44)

        assert 44 == instance.get_warning_shared()

    def test_get_right_critical_shared(self):
        instance = self.create_instance()
        instance.set_critical_shared(55)

        assert 55 == instance.get_critical_shared()

    def test_get_right_ignore_shared(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_shared()

        instance.set_ignore_shared(True)
        assert instance.get_ignore_shared()

        instance.set_ignore_shared(False)
        assert not instance.get_ignore_shared()

    def test_get_right_warning_buffer(self):
        instance = self.create_instance()
        instance.set_warning_buffer(44)

        assert 44 == instance.get_warning_buffer()

    def test_get_right_critical_buffer(self):
        instance = self.create_instance()
        instance.set_critical_buffer(55)

        assert 55 == instance.get_critical_buffer()

    def test_get_right_ignore_buffer(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_buffer()

        instance.set_ignore_buffer(True)
        assert instance.get_ignore_buffer()

        instance.set_ignore_buffer(False)
        assert not instance.get_ignore_buffer()

    def test_get_right_warning_cache(self):
        instance = self.create_instance()
        instance.set_warning_cache(44)

        assert 44 == instance.get_warning_cache()

    def test_get_right_critical_cache(self):
        instance = self.create_instance()
        instance.set_critical_cache(55)

        assert 55 == instance.get_critical_cache()

    def test_get_right_ignore_cache(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_cache()

        instance.set_ignore_cache(True)
        assert instance.get_ignore_cache()

        instance.set_ignore_cache(False)
        assert not instance.get_ignore_cache()

    def test_get_right_warning_min_swap(self):
        instance = self.create_instance()
        instance.set_warning_min_swap(44)

        assert 44 == instance.get_warning_min_swap()

    def test_get_right_critical_min_swap(self):
        instance = self.create_instance()
        instance.set_critical_min_swap(55)

        assert 55 == instance.get_critical_min_swap()

    def test_get_right_ignore_min_swap(self):
        instance = self.create_instance()
        assert None is instance.get_ignore_min_swap()

        instance.set_ignore_min_swap(True)
        assert instance.get_ignore_min_swap()

        instance.set_ignore_min_swap(False)
        assert not instance.get_ignore_min_swap()
