import pytest

from icinga2confgen.Checks.ClaudioKuenzler.CheckStorcenter import CheckStorcenter
from icinga2confgen.Commands.ClaudioKuenzler.StorcenterCommand import StorcenterCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckStorcenter(BaseCheckTest):

    def get_instance_class(self):
        return CheckStorcenter

    def get_command_class(self):
        return StorcenterCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('storcenter'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('password')
        instance.set_type('disk')
        return instance

    def test_get_right_host(self):
        instance = self.create_instance()
        instance.set_host('host')

        assert 'host' == instance.get_host()

    def test_get_right_user(self):
        instance = self.create_instance()
        instance.set_user('user')

        assert 'user' == instance.get_user()

    def test_get_right_warning(self):
        instance = self.create_instance()
        instance.set_warning(33)

        assert 33 == instance.get_warning()

    def test_get_right_critical(self):
        instance = self.create_instance()
        instance.set_critical(33)

        assert 33 == instance.get_critical()

    def test_get_right_password(self):
        instance = self.create_instance()
        instance.set_password('password')

        assert 'password' == instance.get_password()

    def test_get_type(self):
        instance = self.create_instance()

        instance.set_type('disk')
        assert 'disk' == instance.get_type()

        instance.set_type('raid')
        assert 'raid' == instance.get_type()

        instance.set_type('cpu')
        assert 'cpu' == instance.get_type()

        instance.set_type('mem')
        assert 'mem' == instance.get_type()

        instance.set_type('info')
        assert 'info' == instance.get_type()

    def test_raise_exception_on_invalid_type(self):
        instance = self.get_instance_class().create('instance')

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.set_type('invalid')

    def test_validate_raise_exception_if_host_not_set(self):
        instance = BaseCheckTest.create_instance(self)

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'Host' in str(excinfo.value)

    def test_validate_raise_exception_if_user_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('Host')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'User' in str(excinfo.value)

    def test_validate_raise_exception_if_password_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('Host')
        instance.set_user('User')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'Password' in str(excinfo.value)

    def test_validate_raise_exception_if_type_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('Host')
        instance.set_user('User')
        instance.set_password('Password')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'Type' in str(excinfo.value)
