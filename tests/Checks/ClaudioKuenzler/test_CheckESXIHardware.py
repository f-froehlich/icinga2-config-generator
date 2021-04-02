import pytest

from icinga2confgen.Checks.ClaudioKuenzler.CheckESXIHardware import CheckESXIHardware
from icinga2confgen.Commands.ClaudioKuenzler.ESXIHardwareCommand import ESXIHardwareCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckESXIHardware(BaseCheckTest):

    def get_instance_class(self):
        return CheckESXIHardware

    def get_command_class(self):
        return ESXIHardwareCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('esxi_hardware'),
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        instance.set_user('user')
        instance.set_password('password')
        return instance

    def test_get_right_host(self):
        instance = self.create_instance()
        instance.set_host('host')

        assert 'host' == instance.get_host()

    def test_get_right_regex(self):
        instance = self.create_instance()
        instance.set_regex(True)

        assert True is instance.get_regex()

    def test_get_right_nopower(self):
        instance = self.create_instance()
        instance.set_nopower(True)

        assert True is instance.get_nopower()

    def test_get_right_nointrusion(self):
        instance = self.create_instance()
        instance.set_nointrusion(True)

        assert True is instance.get_nointrusion()

    def test_get_right_nolcd(self):
        instance = self.create_instance()
        instance.set_nolcd(True)

        assert True is instance.get_nolcd()

    def test_get_right_nofan(self):
        instance = self.create_instance()
        instance.set_nofan(True)

        assert True is instance.get_nofan()

    def test_get_right_notemp(self):
        instance = self.create_instance()
        instance.set_notemp(True)

        assert True is instance.get_notemp()

    def test_get_right_nocurrent(self):
        instance = self.create_instance()
        instance.set_nocurrent(True)

        assert True is instance.get_nocurrent()

    def test_get_right_novolts(self):
        instance = self.create_instance()
        instance.set_novolts(True)

        assert True is instance.get_novolts()

    def test_get_right_perfdata(self):
        instance = self.create_instance()
        instance.set_perfdata(True)

        assert True is instance.get_perfdata()

    def test_get_right_html(self):
        instance = self.create_instance()
        instance.set_html('html')

        assert 'html' == instance.get_html()

    def test_get_right_port(self):
        instance = self.create_instance()
        instance.set_port(44)

        assert 44 == instance.get_port()

    def test_get_right_ignore(self):
        instance = self.create_instance()
        instance.set_ignore('ignore')

        assert 'ignore' == instance.get_ignore()

    def test_get_right_ssl_proto(self):
        instance = self.create_instance()

        instance.set_sslproto('SSLv2')
        assert 'SSLv2' == instance.get_sslproto()

        instance.set_sslproto('SSLv3')
        assert 'SSLv3' == instance.get_sslproto()

        instance.set_sslproto('TLSv1.0')
        assert 'TLSv1.0' == instance.get_sslproto()

        instance.set_sslproto('TLSv1.1')
        assert 'TLSv1.1' == instance.get_sslproto()

        instance.set_sslproto('TLSv1.2')
        assert 'TLSv1.2' == instance.get_sslproto()

        instance.set_sslproto('TLSv1.3')
        assert 'TLSv1.3' == instance.get_sslproto()

    def test_create_raise_exception_on_invalid_proto(self):
        instance = self.get_instance_class().create('instance')

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.set_sslproto('invalid')

    def test_get_right_vendor(self):
        instance = self.create_instance()
        instance.set_vendor('vendor')

        assert 'vendor' == instance.get_vendor()

    def test_get_right_password(self):
        instance = self.create_instance()
        instance.set_password('password')

        assert 'password' == instance.get_password()

    def test_get_right_user(self):
        instance = self.create_instance()
        instance.set_user('user')

        assert 'user' == instance.get_user()

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
