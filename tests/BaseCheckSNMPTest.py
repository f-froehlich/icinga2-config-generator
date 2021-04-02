import pytest

from tests.BaseCheckTest import BaseCheckTest


class BaseCheckSNMPTest(BaseCheckTest):

    def get_default_check_timeout(self) -> int:
        return 31

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_username('user')
        instance.set_password('pwd')
        return instance

    def test_get_right_username(self):
        instance = self.get_instance_class().create('instance')
        instance.set_username('username')

        assert 'username' == instance.get_username()

    def test_get_right_password(self):
        instance = self.get_instance_class().create('instance')
        instance.set_password('password')

        assert 'password' == instance.get_password()

    def test_get_right_host(self):
        instance = self.get_instance_class().create('instance')
        instance.set_host('host')

        assert 'host' == instance.get_host()

    def test_get_right_timeout(self):
        instance = self.get_instance_class().create('instance')
        instance.set_timeout(55)

        assert 55 == instance.get_timeout()
        assert 56 == instance.get_check_timeout()

    def test_validate_raise_exception_on_missing_host(self):
        instance = BaseCheckTest.create_instance(self)
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Host' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_username(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Username' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_password(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        instance.set_username('username')
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Password' in str(excinfo.value)
