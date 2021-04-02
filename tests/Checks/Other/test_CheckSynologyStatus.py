import pytest

from icinga2confgen.Checks.Other.CheckSynologyStatus import CheckSynologyStatus
from icinga2confgen.Commands.Other.SynologyStatusCommand import SynologyStatusCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSynologyStatus(BaseCheckTest):

    def get_instance_class(self):
        return CheckSynologyStatus

    def get_command_class(self):
        return SynologyStatusCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('synology')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('pwd')
        return instance

    def test_get_right_user(self):
        instance = self.create_instance()

        instance.set_user('user')
        assert 'user' == instance.get_user()

    def test_get_right_host(self):
        instance = self.create_instance()

        instance.set_host('host')
        assert 'host' == instance.get_host()

    def test_get_right_warning_temp(self):
        instance = self.create_instance()

        instance.set_warning_temp(55)
        assert 55 == instance.get_warning_temp()

    def test_get_right_critical_temp(self):
        instance = self.create_instance()

        instance.set_critical_temp(55)
        assert 55 == instance.get_critical_temp()

    def test_get_right_warning_storage(self):
        instance = self.create_instance()

        instance.set_warning_storage(55)
        assert 55 == instance.get_warning_storage()

    def test_get_right_critical_storage(self):
        instance = self.create_instance()

        instance.set_critical_storage(55)
        assert 55 == instance.get_critical_storage()

    def test_get_right_password(self):
        instance = self.create_instance()

        instance.set_password('password')
        assert 'password' == instance.get_password()

    def test_get_right_v2(self):
        instance = self.create_instance()

        instance.set_v2(True)
        assert instance.get_v2()

        instance.set_v2(False)
        assert not instance.get_v2()

    def test_get_right_ups(self):
        instance = self.create_instance()

        instance.set_ups(True)
        assert instance.get_ups()

        instance.set_ups(False)
        assert not instance.get_ups()

    def test_get_right_ignore_update(self):
        instance = self.create_instance()

        instance.set_ignore_update(True)
        assert instance.get_ignore_update()

        instance.set_ignore_update(False)
        assert not instance.get_ignore_update()

    def test_validate_raise_exception_if_host_not_set(self):
        instance = BaseCheckTest.create_instance(self)

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'Host' in str(excinfo.value)

    def test_validate_raise_exception_if_user_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        instance.set_v2(False)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'User' in str(excinfo.value)

    def test_validate_raise_exception_if_password_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        instance.set_v2(False)
        instance.set_user('user')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'Password' in str(excinfo.value)
