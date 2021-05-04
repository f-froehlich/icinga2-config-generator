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
        instance = self.create_instance()
        instance.set_username('username')

        assert 'username' == instance.get_username()

    def test_get_right_password(self):
        instance = self.create_instance()
        instance.set_password('password')

        assert 'password' == instance.get_password()

    def test_get_right_community(self):
        instance = self.create_instance()
        instance.set_community('community')

        assert 'community' == instance.get_community()

    def test_get_right_version(self):
        instance = self.create_instance()

        assert '3' is instance.get_version()

        instance.set_version('2c')
        assert '2c' == instance.get_version()

        instance.set_version('1')
        assert '1' == instance.get_version()

        instance.set_version('3')
        assert '3' == instance.get_version()

    def test_get_right_host(self):
        instance = self.create_instance()
        instance.set_host('host')

        assert 'host' == instance.get_host()

    def test_get_right_timeout(self):
        instance = self.create_instance()
        instance.set_timeout(55)

        assert 55 == instance.get_timeout()
        assert 56 == instance.get_check_timeout()

    def test_validate_raise_exception_on_missing_host(self):
        instance = BaseCheckTest.create_instance(self)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Host' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_username(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Username' in str(excinfo.value)

    def test_validate_raise_exception_on_missing_password(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host('host')
        instance.set_username('username')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Password' in str(excinfo.value)

    def test_validate_not_raise_exception_for_missing_host_and_password_on_version_1(self):
        instance = self.create_instance()
        instance.set_version('1')
        instance.set_host('host')
        instance.validate()

    def test_validate_raise_exception_on_community(self):
        instance = self.create_instance()
        instance.set_version('2c')
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()

        assert 'Community' in str(excinfo.value)

    def test_raise_exception_on_invalid_version(self):
        instance = BaseCheckTest.create_instance(self)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.set_version('invalid')

        assert 'Version' in str(excinfo.value)
