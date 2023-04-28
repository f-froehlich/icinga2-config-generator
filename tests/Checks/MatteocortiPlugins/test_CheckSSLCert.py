import pytest

from icinga2confgen.Checks.MatteocortiPlugins.CheckSSLCert import CheckSSLCert
from icinga2confgen.Commands.MatteocortiPlugins.CheckSSLCertCommand import CheckSSLCertCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckSSLCert(BaseCheckTest):

    def get_instance_class(self):
        return CheckSSLCert

    def get_command_class(self):
        return CheckSSLCertCommand

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('security'),
            ServiceGroup.create('webserver'),
            ServiceGroup.create('tls'),
            ServiceGroup.create('certificate_check')
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_host('host')
        return instance



    def test_validate_raise_exception_if_host_and_file_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'You need to set host or file' == str(excinfo.value)

    def test_validate_raise_exception_if_host_and_file_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_host("host") \
            .set_file("file")
        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'You need to set host or file but you set both' == str(excinfo.value)

    def test_verbose_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_verbose()

    def test_verbose_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_verbose()
        instance.set_verbose(True)
        assert True is instance.get_verbose()
        instance.set_verbose(False)
        assert False is instance.get_verbose()

    def test_verbose_true(self, snapshot):
        instance = self.create_instance()
        instance.set_verbose(True)
        assert True is instance.get_verbose()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'verbose-false.txt')

    def test_verbose_false(self, snapshot):
        instance = self.create_instance()
        instance.set_verbose(False)
        assert False is instance.get_verbose()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'verbose-false.txt')

    def test_terse_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_terse()

    def test_terse_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_terse()
        instance.set_terse(True)
        assert True is instance.get_terse()
        instance.set_terse(False)
        assert False is instance.get_terse()

    def test_terse_true(self, snapshot):
        instance = self.create_instance()
        instance.set_terse(True)
        assert True is instance.get_terse()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'terse-false.txt')

    def test_terse_false(self, snapshot):
        instance = self.create_instance()
        instance.set_terse(False)
        assert False is instance.get_terse()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'terse-false.txt')

    def test_tls1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_tls1()

    def test_tls1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_tls1()
        instance.set_tls1(True)
        assert True is instance.get_tls1()
        instance.set_tls1(False)
        assert False is instance.get_tls1()

    def test_tls1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1(True)
        assert True is instance.get_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1-false.txt')

    def test_tls1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1(False)
        assert False is instance.get_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1-false.txt')

    def test_tls1_1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_1()

    def test_tls1_1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_1()
        instance.set_tls1_1(True)
        assert True is instance.get_tls1_1()
        instance.set_tls1_1(False)
        assert False is instance.get_tls1_1()

    def test_tls1_1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_1(True)
        assert True is instance.get_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_1-false.txt')

    def test_tls1_1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_1(False)
        assert False is instance.get_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_1-false.txt')

    def test_tls1_2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_2()

    def test_tls1_2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_2()
        instance.set_tls1_2(True)
        assert True is instance.get_tls1_2()
        instance.set_tls1_2(False)
        assert False is instance.get_tls1_2()

    def test_tls1_2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_2(True)
        assert True is instance.get_tls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_2-false.txt')

    def test_tls1_2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_2(False)
        assert False is instance.get_tls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_2-false.txt')

    def test_tls1_3_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_3()

    def test_tls1_3_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_tls1_3()
        instance.set_tls1_3(True)
        assert True is instance.get_tls1_3()
        instance.set_tls1_3(False)
        assert False is instance.get_tls1_3()

    def test_tls1_3_true(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_3(True)
        assert True is instance.get_tls1_3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_3-false.txt')

    def test_tls1_3_false(self, snapshot):
        instance = self.create_instance()
        instance.set_tls1_3(False)
        assert False is instance.get_tls1_3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'tls1_3-false.txt')

    def test_ssl2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ssl2()

    def test_ssl2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ssl2()
        instance.set_ssl2(True)
        assert True is instance.get_ssl2()
        instance.set_ssl2(False)
        assert False is instance.get_ssl2()

    def test_ssl2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ssl2(True)
        assert True is instance.get_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ssl2-false.txt')

    def test_ssl2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ssl2(False)
        assert False is instance.get_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ssl2-false.txt')

    def test_ssl3_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ssl3()

    def test_ssl3_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ssl3()
        instance.set_ssl3(True)
        assert True is instance.get_ssl3()
        instance.set_ssl3(False)
        assert False is instance.get_ssl3()

    def test_ssl3_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ssl3(True)
        assert True is instance.get_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ssl3-false.txt')

    def test_ssl3_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ssl3(False)
        assert False is instance.get_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ssl3-false.txt')

    def test_selfsigned_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_selfsigned()

    def test_selfsigned_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_selfsigned()
        instance.set_selfsigned(True)
        assert True is instance.get_selfsigned()
        instance.set_selfsigned(False)
        assert False is instance.get_selfsigned()

    def test_selfsigned_true(self, snapshot):
        instance = self.create_instance()
        instance.set_selfsigned(True)
        assert True is instance.get_selfsigned()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'selfsigned-false.txt')

    def test_selfsigned_false(self, snapshot):
        instance = self.create_instance()
        instance.set_selfsigned(False)
        assert False is instance.get_selfsigned()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'selfsigned-false.txt')

    def test_rsa_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_rsa()

    def test_rsa_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_rsa()
        instance.set_rsa(True)
        assert True is instance.get_rsa()
        instance.set_rsa(False)
        assert False is instance.get_rsa()

    def test_rsa_true(self, snapshot):
        instance = self.create_instance()
        instance.set_rsa(True)
        assert True is instance.get_rsa()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rsa-false.txt')

    def test_rsa_false(self, snapshot):
        instance = self.create_instance()
        instance.set_rsa(False)
        assert False is instance.get_rsa()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rsa-false.txt')

    def test_require_purpose_critical_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_purpose_critical()

    def test_require_purpose_critical_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_purpose_critical()
        instance.set_require_purpose_critical(True)
        assert True is instance.get_require_purpose_critical()
        instance.set_require_purpose_critical(False)
        assert False is instance.get_require_purpose_critical()

    def test_require_purpose_critical_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_purpose_critical(True)
        assert True is instance.get_require_purpose_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose_critical-false.txt')

    def test_require_purpose_critical_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_purpose_critical(False)
        assert False is instance.get_require_purpose_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose_critical-false.txt')

    def test_require_no_ssl2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_ssl2()

    def test_require_no_ssl2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_ssl2()
        instance.set_require_no_ssl2(True)
        assert True is instance.get_require_no_ssl2()
        instance.set_require_no_ssl2(False)
        assert False is instance.get_require_no_ssl2()

    def test_require_no_ssl2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_ssl2(True)
        assert True is instance.get_require_no_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_ssl2-false.txt')

    def test_require_no_ssl2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_ssl2(False)
        assert False is instance.get_require_no_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_ssl2-false.txt')

    def test_require_no_ssl3_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_ssl3()

    def test_require_no_ssl3_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_ssl3()
        instance.set_require_no_ssl3(True)
        assert True is instance.get_require_no_ssl3()
        instance.set_require_no_ssl3(False)
        assert False is instance.get_require_no_ssl3()

    def test_require_no_ssl3_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_ssl3(True)
        assert True is instance.get_require_no_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_ssl3-false.txt')

    def test_require_no_ssl3_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_ssl3(False)
        assert False is instance.get_require_no_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_ssl3-false.txt')

    def test_require_no_tls1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_tls1()

    def test_require_no_tls1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_tls1()
        instance.set_require_no_tls1(True)
        assert True is instance.get_require_no_tls1()
        instance.set_require_no_tls1(False)
        assert False is instance.get_require_no_tls1()

    def test_require_no_tls1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_tls1(True)
        assert True is instance.get_require_no_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_tls1-false.txt')

    def test_require_no_tls1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_tls1(False)
        assert False is instance.get_require_no_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_tls1-false.txt')

    def test_require_no_tls1_1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_tls1_1()

    def test_require_no_tls1_1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_no_tls1_1()
        instance.set_require_no_tls1_1(True)
        assert True is instance.get_require_no_tls1_1()
        instance.set_require_no_tls1_1(False)
        assert False is instance.get_require_no_tls1_1()

    def test_require_no_tls1_1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_tls1_1(True)
        assert True is instance.get_require_no_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_tls1_1-false.txt')

    def test_require_no_tls1_1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_no_tls1_1(False)
        assert False is instance.get_require_no_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_tls1_1-false.txt')

    def test_require_ocsp_stapling_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_require_ocsp_stapling()

    def test_require_ocsp_stapling_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_require_ocsp_stapling()
        instance.set_require_ocsp_stapling(True)
        assert True is instance.get_require_ocsp_stapling()
        instance.set_require_ocsp_stapling(False)
        assert False is instance.get_require_ocsp_stapling()

    def test_require_ocsp_stapling_true(self, snapshot):
        instance = self.create_instance()
        instance.set_require_ocsp_stapling(True)
        assert True is instance.get_require_ocsp_stapling()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_ocsp_stapling-false.txt')

    def test_require_ocsp_stapling_false(self, snapshot):
        instance = self.create_instance()
        instance.set_require_ocsp_stapling(False)
        assert False is instance.get_require_ocsp_stapling()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_ocsp_stapling-false.txt')

    def test_no_perf_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_perf()

    def test_no_perf_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_perf()
        instance.set_no_perf(True)
        assert True is instance.get_no_perf()
        instance.set_no_perf(False)
        assert False is instance.get_no_perf()

    def test_no_perf_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_perf(True)
        assert True is instance.get_no_perf()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_perf-false.txt')

    def test_no_perf_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_perf(False)
        assert False is instance.get_no_perf()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_perf-false.txt')

    def test_no_proxy_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy()

    def test_no_proxy_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy()
        instance.set_no_proxy(True)
        assert True is instance.get_no_proxy()
        instance.set_no_proxy(False)
        assert False is instance.get_no_proxy()

    def test_no_proxy_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy(True)
        assert True is instance.get_no_proxy()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy-false.txt')

    def test_no_proxy_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy(False)
        assert False is instance.get_no_proxy()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy-false.txt')

    def test_no_proxy_curl_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy_curl()

    def test_no_proxy_curl_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy_curl()
        instance.set_no_proxy_curl(True)
        assert True is instance.get_no_proxy_curl()
        instance.set_no_proxy_curl(False)
        assert False is instance.get_no_proxy_curl()

    def test_no_proxy_curl_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy_curl(True)
        assert True is instance.get_no_proxy_curl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy_curl-false.txt')

    def test_no_proxy_curl_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy_curl(False)
        assert False is instance.get_no_proxy_curl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy_curl-false.txt')

    def test_no_proxy_s_client_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy_s_client()

    def test_no_proxy_s_client_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_proxy_s_client()
        instance.set_no_proxy_s_client(True)
        assert True is instance.get_no_proxy_s_client()
        instance.set_no_proxy_s_client(False)
        assert False is instance.get_no_proxy_s_client()

    def test_no_proxy_s_client_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy_s_client(True)
        assert True is instance.get_no_proxy_s_client()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy_s_client-false.txt')

    def test_no_proxy_s_client_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_proxy_s_client(False)
        assert False is instance.get_no_proxy_s_client()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_proxy_s_client-false.txt')

    def test_no_ssl2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_ssl2()

    def test_no_ssl2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_ssl2()
        instance.set_no_ssl2(True)
        assert True is instance.get_no_ssl2()
        instance.set_no_ssl2(False)
        assert False is instance.get_no_ssl2()

    def test_no_ssl2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_ssl2(True)
        assert True is instance.get_no_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_ssl2-false.txt')

    def test_no_ssl2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_ssl2(False)
        assert False is instance.get_no_ssl2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_ssl2-false.txt')

    def test_no_ssl3_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_ssl3()

    def test_no_ssl3_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_ssl3()
        instance.set_no_ssl3(True)
        assert True is instance.get_no_ssl3()
        instance.set_no_ssl3(False)
        assert False is instance.get_no_ssl3()

    def test_no_ssl3_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_ssl3(True)
        assert True is instance.get_no_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_ssl3-false.txt')

    def test_no_ssl3_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_ssl3(False)
        assert False is instance.get_no_ssl3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_ssl3-false.txt')

    def test_no_tls1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1()

    def test_no_tls1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1()
        instance.set_no_tls1(True)
        assert True is instance.get_no_tls1()
        instance.set_no_tls1(False)
        assert False is instance.get_no_tls1()

    def test_no_tls1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1(True)
        assert True is instance.get_no_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1-false.txt')

    def test_no_tls1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1(False)
        assert False is instance.get_no_tls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1-false.txt')

    def test_no_tls1_1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_1()

    def test_no_tls1_1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_1()
        instance.set_no_tls1_1(True)
        assert True is instance.get_no_tls1_1()
        instance.set_no_tls1_1(False)
        assert False is instance.get_no_tls1_1()

    def test_no_tls1_1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_1(True)
        assert True is instance.get_no_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_1-false.txt')

    def test_no_tls1_1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_1(False)
        assert False is instance.get_no_tls1_1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_1-false.txt')

    def test_no_tls1_2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_2()

    def test_no_tls1_2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_2()
        instance.set_no_tls1_2(True)
        assert True is instance.get_no_tls1_2()
        instance.set_no_tls1_2(False)
        assert False is instance.get_no_tls1_2()

    def test_no_tls1_2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_2(True)
        assert True is instance.get_no_tls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_2-false.txt')

    def test_no_tls1_2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_2(False)
        assert False is instance.get_no_tls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_2-false.txt')

    def test_no_tls1_3_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_3()

    def test_no_tls1_3_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_no_tls1_3()
        instance.set_no_tls1_3(True)
        assert True is instance.get_no_tls1_3()
        instance.set_no_tls1_3(False)
        assert False is instance.get_no_tls1_3()

    def test_no_tls1_3_true(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_3(True)
        assert True is instance.get_no_tls1_3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_3-false.txt')

    def test_no_tls1_3_false(self, snapshot):
        instance = self.create_instance()
        instance.set_no_tls1_3(False)
        assert False is instance.get_no_tls1_3()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'no_tls1_3-false.txt')

    def test_info_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_info()

    def test_info_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_info()
        instance.set_info(True)
        assert True is instance.get_info()
        instance.set_info(False)
        assert False is instance.get_info()

    def test_info_true(self, snapshot):
        instance = self.create_instance()
        instance.set_info(True)
        assert True is instance.get_info()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'info-false.txt')

    def test_info_false(self, snapshot):
        instance = self.create_instance()
        instance.set_info(False)
        assert False is instance.get_info()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'info-false.txt')

    def test_init_host_cache_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_init_host_cache()

    def test_init_host_cache_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_init_host_cache()
        instance.set_init_host_cache(True)
        assert True is instance.get_init_host_cache()
        instance.set_init_host_cache(False)
        assert False is instance.get_init_host_cache()

    def test_init_host_cache_true(self, snapshot):
        instance = self.create_instance()
        instance.set_init_host_cache(True)
        assert True is instance.get_init_host_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'init_host_cache-false.txt')

    def test_init_host_cache_false(self, snapshot):
        instance = self.create_instance()
        instance.set_init_host_cache(False)
        assert False is instance.get_init_host_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'init_host_cache-false.txt')

    def test_ignore_altnames_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_altnames()

    def test_ignore_altnames_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_altnames()
        instance.set_ignore_altnames(True)
        assert True is instance.get_ignore_altnames()
        instance.set_ignore_altnames(False)
        assert False is instance.get_ignore_altnames()

    def test_ignore_altnames_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_altnames(True)
        assert True is instance.get_ignore_altnames()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_altnames-false.txt')

    def test_ignore_altnames_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_altnames(False)
        assert False is instance.get_ignore_altnames()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_altnames-false.txt')

    def test_ignore_connection_problems_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_connection_problems()

    def test_ignore_connection_problems_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_connection_problems()
        instance.set_ignore_connection_problems(True)
        assert True is instance.get_ignore_connection_problems()
        instance.set_ignore_connection_problems(False)
        assert False is instance.get_ignore_connection_problems()

    def test_ignore_connection_problems_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_connection_problems(True)
        assert True is instance.get_ignore_connection_problems()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_connection_problems-false.txt')

    def test_ignore_connection_problems_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_connection_problems(False)
        assert False is instance.get_ignore_connection_problems()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_connection_problems-false.txt')

    def test_ignore_exp_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_exp()

    def test_ignore_exp_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_exp()
        instance.set_ignore_exp(True)
        assert True is instance.get_ignore_exp()
        instance.set_ignore_exp(False)
        assert False is instance.get_ignore_exp()

    def test_ignore_exp_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_exp(True)
        assert True is instance.get_ignore_exp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_exp-false.txt')

    def test_ignore_exp_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_exp(False)
        assert False is instance.get_ignore_exp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_exp-false.txt')

    def test_ignore_http_headers_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_http_headers()

    def test_ignore_http_headers_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_http_headers()
        instance.set_ignore_http_headers(True)
        assert True is instance.get_ignore_http_headers()
        instance.set_ignore_http_headers(False)
        assert False is instance.get_ignore_http_headers()

    def test_ignore_http_headers_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_http_headers(True)
        assert True is instance.get_ignore_http_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_http_headers-false.txt')

    def test_ignore_http_headers_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_http_headers(False)
        assert False is instance.get_ignore_http_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_http_headers-false.txt')

    def test_ignore_incomplete_chain_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_incomplete_chain()

    def test_ignore_incomplete_chain_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_incomplete_chain()
        instance.set_ignore_incomplete_chain(True)
        assert True is instance.get_ignore_incomplete_chain()
        instance.set_ignore_incomplete_chain(False)
        assert False is instance.get_ignore_incomplete_chain()

    def test_ignore_incomplete_chain_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_incomplete_chain(True)
        assert True is instance.get_ignore_incomplete_chain()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_incomplete_chain-false.txt')

    def test_ignore_incomplete_chain_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_incomplete_chain(False)
        assert False is instance.get_ignore_incomplete_chain()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_incomplete_chain-false.txt')

    def test_ignore_host_cn_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_host_cn()

    def test_ignore_host_cn_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_host_cn()
        instance.set_ignore_host_cn(True)
        assert True is instance.get_ignore_host_cn()
        instance.set_ignore_host_cn(False)
        assert False is instance.get_ignore_host_cn()

    def test_ignore_host_cn_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_host_cn(True)
        assert True is instance.get_ignore_host_cn()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_host_cn-false.txt')

    def test_ignore_host_cn_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_host_cn(False)
        assert False is instance.get_ignore_host_cn()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_host_cn-false.txt')

    def test_ignore_maximum_validity_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_maximum_validity()

    def test_ignore_maximum_validity_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_maximum_validity()
        instance.set_ignore_maximum_validity(True)
        assert True is instance.get_ignore_maximum_validity()
        instance.set_ignore_maximum_validity(False)
        assert False is instance.get_ignore_maximum_validity()

    def test_ignore_maximum_validity_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_maximum_validity(True)
        assert True is instance.get_ignore_maximum_validity()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_maximum_validity-false.txt')

    def test_ignore_maximum_validity_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_maximum_validity(False)
        assert False is instance.get_ignore_maximum_validity()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_maximum_validity-false.txt')

    def test_ignore_ocsp_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp()

    def test_ignore_ocsp_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp()
        instance.set_ignore_ocsp(True)
        assert True is instance.get_ignore_ocsp()
        instance.set_ignore_ocsp(False)
        assert False is instance.get_ignore_ocsp()

    def test_ignore_ocsp_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp(True)
        assert True is instance.get_ignore_ocsp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp-false.txt')

    def test_ignore_ocsp_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp(False)
        assert False is instance.get_ignore_ocsp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp-false.txt')

    def test_ignore_ocsp_errors_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp_errors()

    def test_ignore_ocsp_errors_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp_errors()
        instance.set_ignore_ocsp_errors(True)
        assert True is instance.get_ignore_ocsp_errors()
        instance.set_ignore_ocsp_errors(False)
        assert False is instance.get_ignore_ocsp_errors()

    def test_ignore_ocsp_errors_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp_errors(True)
        assert True is instance.get_ignore_ocsp_errors()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp_errors-false.txt')

    def test_ignore_ocsp_errors_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp_errors(False)
        assert False is instance.get_ignore_ocsp_errors()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp_errors-false.txt')

    def test_ignore_ocsp_timeout_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp_timeout()

    def test_ignore_ocsp_timeout_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ocsp_timeout()
        instance.set_ignore_ocsp_timeout(True)
        assert True is instance.get_ignore_ocsp_timeout()
        instance.set_ignore_ocsp_timeout(False)
        assert False is instance.get_ignore_ocsp_timeout()

    def test_ignore_ocsp_timeout_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp_timeout(True)
        assert True is instance.get_ignore_ocsp_timeout()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp_timeout-false.txt')

    def test_ignore_ocsp_timeout_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ocsp_timeout(False)
        assert False is instance.get_ignore_ocsp_timeout()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ocsp_timeout-false.txt')

    def test_ignore_sct_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_sct()

    def test_ignore_sct_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_sct()
        instance.set_ignore_sct(True)
        assert True is instance.get_ignore_sct()
        instance.set_ignore_sct(False)
        assert False is instance.get_ignore_sct()

    def test_ignore_sct_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_sct(True)
        assert True is instance.get_ignore_sct()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_sct-false.txt')

    def test_ignore_sct_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_sct(False)
        assert False is instance.get_ignore_sct()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_sct-false.txt')

    def test_ignore_sig_alg_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_sig_alg()

    def test_ignore_sig_alg_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_sig_alg()
        instance.set_ignore_sig_alg(True)
        assert True is instance.get_ignore_sig_alg()
        instance.set_ignore_sig_alg(False)
        assert False is instance.get_ignore_sig_alg()

    def test_ignore_sig_alg_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_sig_alg(True)
        assert True is instance.get_ignore_sig_alg()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_sig_alg-false.txt')

    def test_ignore_sig_alg_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_sig_alg(False)
        assert False is instance.get_ignore_sig_alg()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_sig_alg-false.txt')

    def test_ignore_ssl_labs_cache_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ssl_labs_cache()

    def test_ignore_ssl_labs_cache_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ssl_labs_cache()
        instance.set_ignore_ssl_labs_cache(True)
        assert True is instance.get_ignore_ssl_labs_cache()
        instance.set_ignore_ssl_labs_cache(False)
        assert False is instance.get_ignore_ssl_labs_cache()

    def test_ignore_ssl_labs_cache_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ssl_labs_cache(True)
        assert True is instance.get_ignore_ssl_labs_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ssl_labs_cache-false.txt')

    def test_ignore_ssl_labs_cache_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ssl_labs_cache(False)
        assert False is instance.get_ignore_ssl_labs_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ssl_labs_cache-false.txt')

    def test_ignore_ssl_labs_errors_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ssl_labs_errors()

    def test_ignore_ssl_labs_errors_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_ssl_labs_errors()
        instance.set_ignore_ssl_labs_errors(True)
        assert True is instance.get_ignore_ssl_labs_errors()
        instance.set_ignore_ssl_labs_errors(False)
        assert False is instance.get_ignore_ssl_labs_errors()

    def test_ignore_ssl_labs_errors_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ssl_labs_errors(True)
        assert True is instance.get_ignore_ssl_labs_errors()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ssl_labs_errors-false.txt')

    def test_ignore_ssl_labs_errors_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_ssl_labs_errors(False)
        assert False is instance.get_ignore_ssl_labs_errors()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_ssl_labs_errors-false.txt')

    def test_ignore_tls_renegotiation_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_tls_renegotiation()

    def test_ignore_tls_renegotiation_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ignore_tls_renegotiation()
        instance.set_ignore_tls_renegotiation(True)
        assert True is instance.get_ignore_tls_renegotiation()
        instance.set_ignore_tls_renegotiation(False)
        assert False is instance.get_ignore_tls_renegotiation()

    def test_ignore_tls_renegotiation_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_tls_renegotiation(True)
        assert True is instance.get_ignore_tls_renegotiation()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_tls_renegotiation-false.txt')

    def test_ignore_tls_renegotiation_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ignore_tls_renegotiation(False)
        assert False is instance.get_ignore_tls_renegotiation()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ignore_tls_renegotiation-false.txt')

    def test_http_use_get_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_http_use_get()

    def test_http_use_get_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_http_use_get()
        instance.set_http_use_get(True)
        assert True is instance.get_http_use_get()
        instance.set_http_use_get(False)
        assert False is instance.get_http_use_get()

    def test_http_use_get_true(self, snapshot):
        instance = self.create_instance()
        instance.set_http_use_get(True)
        assert True is instance.get_http_use_get()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'http_use_get-false.txt')

    def test_http_use_get_false(self, snapshot):
        instance = self.create_instance()
        instance.set_http_use_get(False)
        assert False is instance.get_http_use_get()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'http_use_get-false.txt')

    def test_first_element_only_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_first_element_only()

    def test_first_element_only_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_first_element_only()
        instance.set_first_element_only(True)
        assert True is instance.get_first_element_only()
        instance.set_first_element_only(False)
        assert False is instance.get_first_element_only()

    def test_first_element_only_true(self, snapshot):
        instance = self.create_instance()
        instance.set_first_element_only(True)
        assert True is instance.get_first_element_only()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'first_element_only-false.txt')

    def test_first_element_only_false(self, snapshot):
        instance = self.create_instance()
        instance.set_first_element_only(False)
        assert False is instance.get_first_element_only()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'first_element_only-false.txt')

    def test_force_dconv_date_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_force_dconv_date()

    def test_force_dconv_date_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_force_dconv_date()
        instance.set_force_dconv_date(True)
        assert True is instance.get_force_dconv_date()
        instance.set_force_dconv_date(False)
        assert False is instance.get_force_dconv_date()

    def test_force_dconv_date_true(self, snapshot):
        instance = self.create_instance()
        instance.set_force_dconv_date(True)
        assert True is instance.get_force_dconv_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'force_dconv_date-false.txt')

    def test_force_dconv_date_false(self, snapshot):
        instance = self.create_instance()
        instance.set_force_dconv_date(False)
        assert False is instance.get_force_dconv_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'force_dconv_date-false.txt')

    def test_force_perl_date_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_force_perl_date()

    def test_force_perl_date_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_force_perl_date()
        instance.set_force_perl_date(True)
        assert True is instance.get_force_perl_date()
        instance.set_force_perl_date(False)
        assert False is instance.get_force_perl_date()

    def test_force_perl_date_true(self, snapshot):
        instance = self.create_instance()
        instance.set_force_perl_date(True)
        assert True is instance.get_force_perl_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'force_perl_date-false.txt')

    def test_force_perl_date_false(self, snapshot):
        instance = self.create_instance()
        instance.set_force_perl_date(False)
        assert False is instance.get_force_perl_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'force_perl_date-false.txt')

    def test_ecdsa_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ecdsa()

    def test_ecdsa_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ecdsa()
        instance.set_ecdsa(True)
        assert True is instance.get_ecdsa()
        instance.set_ecdsa(False)
        assert False is instance.get_ecdsa()

    def test_ecdsa_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ecdsa(True)
        assert True is instance.get_ecdsa()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ecdsa-false.txt')

    def test_ecdsa_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ecdsa(False)
        assert False is instance.get_ecdsa()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ecdsa-false.txt')

    def test_dtls_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_dtls()

    def test_dtls_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_dtls()
        instance.set_dtls(True)
        assert True is instance.get_dtls()
        instance.set_dtls(False)
        assert False is instance.get_dtls()

    def test_dtls_true(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls(True)
        assert True is instance.get_dtls()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls-false.txt')

    def test_dtls_false(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls(False)
        assert False is instance.get_dtls()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls-false.txt')

    def test_dtls1_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_dtls1()

    def test_dtls1_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_dtls1()
        instance.set_dtls1(True)
        assert True is instance.get_dtls1()
        instance.set_dtls1(False)
        assert False is instance.get_dtls1()

    def test_dtls1_true(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls1(True)
        assert True is instance.get_dtls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls1-false.txt')

    def test_dtls1_false(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls1(False)
        assert False is instance.get_dtls1()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls1-false.txt')

    def test_dtls1_2_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_dtls1_2()

    def test_dtls1_2_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_dtls1_2()
        instance.set_dtls1_2(True)
        assert True is instance.get_dtls1_2()
        instance.set_dtls1_2(False)
        assert False is instance.get_dtls1_2()

    def test_dtls1_2_true(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls1_2(True)
        assert True is instance.get_dtls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls1_2-false.txt')

    def test_dtls1_2_false(self, snapshot):
        instance = self.create_instance()
        instance.set_dtls1_2(False)
        assert False is instance.get_dtls1_2()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dtls1_2-false.txt')

    def test_debug_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_debug()

    def test_debug_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_debug()
        instance.set_debug(True)
        assert True is instance.get_debug()
        instance.set_debug(False)
        assert False is instance.get_debug()

    def test_debug_true(self, snapshot):
        instance = self.create_instance()
        instance.set_debug(True)
        assert True is instance.get_debug()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug-false.txt')

    def test_debug_false(self, snapshot):
        instance = self.create_instance()
        instance.set_debug(False)
        assert False is instance.get_debug()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug-false.txt')

    def test_debug_cert_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_debug_cert()

    def test_debug_cert_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_debug_cert()
        instance.set_debug_cert(True)
        assert True is instance.get_debug_cert()
        instance.set_debug_cert(False)
        assert False is instance.get_debug_cert()

    def test_debug_cert_true(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_cert(True)
        assert True is instance.get_debug_cert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_cert-false.txt')

    def test_debug_cert_false(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_cert(False)
        assert False is instance.get_debug_cert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_cert-false.txt')

    def test_debug_headers_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_debug_headers()

    def test_debug_headers_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_debug_headers()
        instance.set_debug_headers(True)
        assert True is instance.get_debug_headers()
        instance.set_debug_headers(False)
        assert False is instance.get_debug_headers()

    def test_debug_headers_true(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_headers(True)
        assert True is instance.get_debug_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_headers-false.txt')

    def test_debug_headers_false(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_headers(False)
        assert False is instance.get_debug_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_headers-false.txt')

    def test_debug_time_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_debug_time()

    def test_debug_time_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_debug_time()
        instance.set_debug_time(True)
        assert True is instance.get_debug_time()
        instance.set_debug_time(False)
        assert False is instance.get_debug_time()

    def test_debug_time_true(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_time(True)
        assert True is instance.get_debug_time()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_time-false.txt')

    def test_debug_time_false(self, snapshot):
        instance = self.create_instance()
        instance.set_debug_time(False)
        assert False is instance.get_debug_time()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_time-false.txt')

    def test_default_format_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_default_format()

    def test_default_format_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_default_format()
        instance.set_default_format(True)
        assert True is instance.get_default_format()
        instance.set_default_format(False)
        assert False is instance.get_default_format()

    def test_default_format_true(self, snapshot):
        instance = self.create_instance()
        instance.set_default_format(True)
        assert True is instance.get_default_format()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'default_format-false.txt')

    def test_default_format_false(self, snapshot):
        instance = self.create_instance()
        instance.set_default_format(False)
        assert False is instance.get_default_format()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'default_format-false.txt')

    def test_crl_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_crl()

    def test_crl_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_crl()
        instance.set_crl(True)
        assert True is instance.get_crl()
        instance.set_crl(False)
        assert False is instance.get_crl()

    def test_crl_true(self, snapshot):
        instance = self.create_instance()
        instance.set_crl(True)
        assert True is instance.get_crl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'crl-false.txt')

    def test_crl_false(self, snapshot):
        instance = self.create_instance()
        instance.set_crl(False)
        assert False is instance.get_crl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'crl-false.txt')

    def test_check_ciphers_warnings_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_check_ciphers_warnings()

    def test_check_ciphers_warnings_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_check_ciphers_warnings()
        instance.set_check_ciphers_warnings(True)
        assert True is instance.get_check_ciphers_warnings()
        instance.set_check_ciphers_warnings(False)
        assert False is instance.get_check_ciphers_warnings()

    def test_check_ciphers_warnings_true(self, snapshot):
        instance = self.create_instance()
        instance.set_check_ciphers_warnings(True)
        assert True is instance.get_check_ciphers_warnings()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ciphers_warnings-false.txt')

    def test_check_ciphers_warnings_false(self, snapshot):
        instance = self.create_instance()
        instance.set_check_ciphers_warnings(False)
        assert False is instance.get_check_ciphers_warnings()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ciphers_warnings-false.txt')

    def test_check_http_headers_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_check_http_headers()

    def test_check_http_headers_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_check_http_headers()
        instance.set_check_http_headers(True)
        assert True is instance.get_check_http_headers()
        instance.set_check_http_headers(False)
        assert False is instance.get_check_http_headers()

    def test_check_http_headers_true(self, snapshot):
        instance = self.create_instance()
        instance.set_check_http_headers(True)
        assert True is instance.get_check_http_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_http_headers-false.txt')

    def test_check_http_headers_false(self, snapshot):
        instance = self.create_instance()
        instance.set_check_http_headers(False)
        assert False is instance.get_check_http_headers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_http_headers-false.txt')

    def test_check_chain_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_check_chain()

    def test_check_chain_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_check_chain()
        instance.set_check_chain(True)
        assert True is instance.get_check_chain()
        instance.set_check_chain(False)
        assert False is instance.get_check_chain()

    def test_check_chain_true(self, snapshot):
        instance = self.create_instance()
        instance.set_check_chain(True)
        assert True is instance.get_check_chain()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_chain-false.txt')

    def test_check_chain_false(self, snapshot):
        instance = self.create_instance()
        instance.set_check_chain(False)
        assert False is instance.get_check_chain()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_chain-false.txt')

    def test_noauth_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_noauth()

    def test_noauth_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_noauth()
        instance.set_noauth(True)
        assert True is instance.get_noauth()
        instance.set_noauth(False)
        assert False is instance.get_noauth()

    def test_noauth_true(self, snapshot):
        instance = self.create_instance()
        instance.set_noauth(True)
        assert True is instance.get_noauth()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'noauth-false.txt')

    def test_noauth_false(self, snapshot):
        instance = self.create_instance()
        instance.set_noauth(False)
        assert False is instance.get_noauth()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'noauth-false.txt')

    def test_all_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_all()

    def test_all_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_all()
        instance.set_all(True)
        assert True is instance.get_all()
        instance.set_all(False)
        assert False is instance.get_all()

    def test_all_true(self, snapshot):
        instance = self.create_instance()
        instance.set_all(True)
        assert True is instance.get_all()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'all-false.txt')

    def test_all_false(self, snapshot):
        instance = self.create_instance()
        instance.set_all(False)
        assert False is instance.get_all()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'all-false.txt')

    def test_all_local_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_all_local()

    def test_all_local_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_all_local()
        instance.set_all_local(True)
        assert True is instance.get_all_local()
        instance.set_all_local(False)
        assert False is instance.get_all_local()

    def test_all_local_true(self, snapshot):
        instance = self.create_instance()
        instance.set_all_local(True)
        assert True is instance.get_all_local()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'all_local-false.txt')

    def test_all_local_false(self, snapshot):
        instance = self.create_instance()
        instance.set_all_local(False)
        assert False is instance.get_all_local()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'all_local-false.txt')

    def test_allow_empty_san_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_allow_empty_san()

    def test_allow_empty_san_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_allow_empty_san()
        instance.set_allow_empty_san(True)
        assert True is instance.get_allow_empty_san()
        instance.set_allow_empty_san(False)
        assert False is instance.get_allow_empty_san()

    def test_allow_empty_san_true(self, snapshot):
        instance = self.create_instance()
        instance.set_allow_empty_san(True)
        assert True is instance.get_allow_empty_san()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'allow_empty_san-false.txt')

    def test_allow_empty_san_false(self, snapshot):
        instance = self.create_instance()
        instance.set_allow_empty_san(False)
        assert False is instance.get_allow_empty_san()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'allow_empty_san-false.txt')

    def test_ipv4_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ipv4()

    def test_ipv4_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ipv4()
        instance.set_ipv4(True)
        assert True is instance.get_ipv4()
        instance.set_ipv4(False)
        assert False is instance.get_ipv4()

    def test_ipv4_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ipv4(True)
        assert True is instance.get_ipv4()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ipv4-false.txt')

    def test_ipv4_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ipv4(False)
        assert False is instance.get_ipv4()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ipv4-false.txt')

    def test_ipv6_default_value(self):
        instance = self.create_instance()
        assert False is instance.get_ipv6()

    def test_ipv6_set_correct(self):
        instance = self.create_instance()
        assert False is instance.get_ipv6()
        instance.set_ipv6(True)
        assert True is instance.get_ipv6()
        instance.set_ipv6(False)
        assert False is instance.get_ipv6()

    def test_ipv6_true(self, snapshot):
        instance = self.create_instance()
        instance.set_ipv6(True)
        assert True is instance.get_ipv6()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ipv6-false.txt')

    def test_ipv6_false(self, snapshot):
        instance = self.create_instance()
        instance.set_ipv6(False)
        assert False is instance.get_ipv6()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ipv6-false.txt')

    def test_file_default(self):
        instance = self.create_instance()
        assert None is instance.get_file()

    def test_file_value(self, snapshot):
        instance = BaseCheckTest.create_instance(self)
        assert None is instance.get_file()
        instance.set_file('TestValue1')
        assert 'TestValue1' == instance.get_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'file-TestValue1.txt')
        instance.set_file('TestValue2')
        assert 'TestValue2' == instance.get_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'file-TestValue2.txt')

    def test_host_default(self):
        instance = BaseCheckTest.create_instance(self)
        assert None is instance.get_host()

    def test_host_value(self, snapshot):
        instance = BaseCheckTest.create_instance(self)
        assert None is instance.get_host()
        instance.set_host('TestValue1')
        assert 'TestValue1' == instance.get_host()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'host-TestValue1.txt')
        instance.set_host('TestValue2')
        assert 'TestValue2' == instance.get_host()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'host-TestValue2.txt')

    def test_clientcert_default(self):
        instance = self.create_instance()
        assert None is instance.get_clientcert()

    def test_clientcert_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_clientcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientcert-default.txt')
        instance.set_clientcert('TestValue1')
        assert 'TestValue1' == instance.get_clientcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientcert-TestValue1.txt')
        instance.set_clientcert('TestValue2')
        assert 'TestValue2' == instance.get_clientcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientcert-TestValue2.txt')

    def test_check_ciphers_default(self):
        instance = self.create_instance()
        assert None is instance.get_check_ciphers()

    def test_check_ciphers_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_check_ciphers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ciphers-default.txt')
        instance.set_check_ciphers('TestValue1')
        assert 'TestValue1' == instance.get_check_ciphers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ciphers-TestValue1.txt')
        instance.set_check_ciphers('TestValue2')
        assert 'TestValue2' == instance.get_check_ciphers()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ciphers-TestValue2.txt')

    def test_check_ssl_labs_warn_default(self):
        instance = self.create_instance()
        assert None is instance.get_check_ssl_labs_warn()

    def test_check_ssl_labs_warn_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_check_ssl_labs_warn()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs_warn-default.txt')
        instance.set_check_ssl_labs_warn('TestValue1')
        assert 'TestValue1' == instance.get_check_ssl_labs_warn()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs_warn-TestValue1.txt')
        instance.set_check_ssl_labs_warn('TestValue2')
        assert 'TestValue2' == instance.get_check_ssl_labs_warn()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs_warn-TestValue2.txt')

    def test_clientpass_default(self):
        instance = self.create_instance()
        assert None is instance.get_clientpass()

    def test_clientpass_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_clientpass()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientpass-default.txt')
        instance.set_clientpass('TestValue1')
        assert 'TestValue1' == instance.get_clientpass()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientpass-TestValue1.txt')
        instance.set_clientpass('TestValue2')
        assert 'TestValue2' == instance.get_clientpass()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientpass-TestValue2.txt')

    def test_configuration_default(self):
        instance = self.create_instance()
        assert None is instance.get_configuration()

    def test_configuration_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_configuration()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'configuration-default.txt')
        instance.set_configuration('TestValue1')
        assert 'TestValue1' == instance.get_configuration()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'configuration-TestValue1.txt')
        instance.set_configuration('TestValue2')
        assert 'TestValue2' == instance.get_configuration()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'configuration-TestValue2.txt')

    def test_custom_http_header_default(self):
        instance = self.create_instance()
        assert None is instance.get_custom_http_header()

    def test_custom_http_header_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_custom_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'custom_http_header-default.txt')
        instance.set_custom_http_header('TestValue1')
        assert 'TestValue1' == instance.get_custom_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'custom_http_header-TestValue1.txt')
        instance.set_custom_http_header('TestValue2')
        assert 'TestValue2' == instance.get_custom_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'custom_http_header-TestValue2.txt')

    def test_curl_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_curl_bin()

    def test_curl_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_curl_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'curl_bin-default.txt')
        instance.set_curl_bin('TestValue1')
        assert 'TestValue1' == instance.get_curl_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'curl_bin-TestValue1.txt')
        instance.set_curl_bin('TestValue2')
        assert 'TestValue2' == instance.get_curl_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'curl_bin-TestValue2.txt')

    def test_date_default(self):
        instance = self.create_instance()
        assert None is instance.get_date()

    def test_date_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'date-default.txt')
        instance.set_date('TestValue1')
        assert 'TestValue1' == instance.get_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'date-TestValue1.txt')
        instance.set_date('TestValue2')
        assert 'TestValue2' == instance.get_date()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'date-TestValue2.txt')

    def test_debug_file_default(self):
        instance = self.create_instance()
        assert None is instance.get_debug_file()

    def test_debug_file_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_debug_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_file-default.txt')
        instance.set_debug_file('TestValue1')
        assert 'TestValue1' == instance.get_debug_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_file-TestValue1.txt')
        instance.set_debug_file('TestValue2')
        assert 'TestValue2' == instance.get_debug_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'debug_file-TestValue2.txt')

    def test_dig_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_dig_bin()

    def test_dig_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_dig_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dig_bin-default.txt')
        instance.set_dig_bin('TestValue1')
        assert 'TestValue1' == instance.get_dig_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dig_bin-TestValue1.txt')
        instance.set_dig_bin('TestValue2')
        assert 'TestValue2' == instance.get_dig_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dig_bin-TestValue2.txt')

    def test_email_default(self):
        instance = self.create_instance()
        assert None is instance.get_email()

    def test_email_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_email()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'email-default.txt')
        instance.set_email('TestValue1')
        assert 'TestValue1' == instance.get_email()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'email-TestValue1.txt')
        instance.set_email('TestValue2')
        assert 'TestValue2' == instance.get_email()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'email-TestValue2.txt')

    def test_file_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_file_bin()

    def test_file_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_file_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'file_bin-default.txt')
        instance.set_file_bin('TestValue1')
        assert 'TestValue1' == instance.get_file_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'file_bin-TestValue1.txt')
        instance.set_file_bin('TestValue2')
        assert 'TestValue2' == instance.get_file_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'file_bin-TestValue2.txt')

    def test_fingerprint_default(self):
        instance = self.create_instance()
        assert None is instance.get_fingerprint()

    def test_fingerprint_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_fingerprint()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'fingerprint-default.txt')
        instance.set_fingerprint('TestValue1')
        assert 'TestValue1' == instance.get_fingerprint()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'fingerprint-TestValue1.txt')
        instance.set_fingerprint('TestValue2')
        assert 'TestValue2' == instance.get_fingerprint()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'fingerprint-TestValue2.txt')

    def test_grep_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_grep_bin()

    def test_grep_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_grep_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'grep_bin-default.txt')
        instance.set_grep_bin('TestValue1')
        assert 'TestValue1' == instance.get_grep_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'grep_bin-TestValue1.txt')
        instance.set_grep_bin('TestValue2')
        assert 'TestValue2' == instance.get_grep_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'grep_bin-TestValue2.txt')

    def test_format_default(self):
        instance = self.create_instance()
        assert None is instance.get_format()

    def test_format_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_format()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'format-default.txt')
        instance.set_format('TestValue1')
        assert 'TestValue1' == instance.get_format()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'format-TestValue1.txt')
        instance.set_format('TestValue2')
        assert 'TestValue2' == instance.get_format()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'format-TestValue2.txt')

    def test_http_headers_path_default(self):
        instance = self.create_instance()
        assert None is instance.get_http_headers_path()

    def test_http_headers_path_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_http_headers_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'http_headers_path-default.txt')
        instance.set_http_headers_path('TestValue1')
        assert 'TestValue1' == instance.get_http_headers_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'http_headers_path-TestValue1.txt')
        instance.set_http_headers_path('TestValue2')
        assert 'TestValue2' == instance.get_http_headers_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'http_headers_path-TestValue2.txt')

    def test_issuer_default(self):
        instance = self.create_instance()
        assert None is instance.get_issuer()

    def test_issuer_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_issuer()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer-default.txt')
        instance.set_issuer('TestValue1')
        assert 'TestValue1' == instance.get_issuer()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer-TestValue1.txt')
        instance.set_issuer('TestValue2')
        assert 'TestValue2' == instance.get_issuer()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer-TestValue2.txt')

    def test_inetproto_default(self):
        instance = self.create_instance()
        assert None is instance.get_inetproto()

    def test_inetproto_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_inetproto()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'inetproto-default.txt')
        instance.set_inetproto('TestValue1')
        assert 'TestValue1' == instance.get_inetproto()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'inetproto-TestValue1.txt')
        instance.set_inetproto('TestValue2')
        assert 'TestValue2' == instance.get_inetproto()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'inetproto-TestValue2.txt')

    def test_issuer_cert_cache_default(self):
        instance = self.create_instance()
        assert None is instance.get_issuer_cert_cache()

    def test_issuer_cert_cache_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_issuer_cert_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer_cert_cache-default.txt')
        instance.set_issuer_cert_cache('TestValue1')
        assert 'TestValue1' == instance.get_issuer_cert_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer_cert_cache-TestValue1.txt')
        instance.set_issuer_cert_cache('TestValue2')
        assert 'TestValue2' == instance.get_issuer_cert_cache()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'issuer_cert_cache-TestValue2.txt')

    def test_jks_alias_default(self):
        instance = self.create_instance()
        assert None is instance.get_jks_alias()

    def test_jks_alias_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_jks_alias()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'jks_alias-default.txt')
        instance.set_jks_alias('TestValue1')
        assert 'TestValue1' == instance.get_jks_alias()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'jks_alias-TestValue1.txt')
        instance.set_jks_alias('TestValue2')
        assert 'TestValue2' == instance.get_jks_alias()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'jks_alias-TestValue2.txt')

    def test_clientkey_default(self):
        instance = self.create_instance()
        assert None is instance.get_clientkey()

    def test_clientkey_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_clientkey()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientkey-default.txt')
        instance.set_clientkey('TestValue1')
        assert 'TestValue1' == instance.get_clientkey()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientkey-TestValue1.txt')
        instance.set_clientkey('TestValue2')
        assert 'TestValue2' == instance.get_clientkey()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'clientkey-TestValue2.txt')

    def test_check_ssl_labs_default(self):
        instance = self.create_instance()
        assert None is instance.get_check_ssl_labs()

    def test_check_ssl_labs_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_check_ssl_labs()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs-default.txt')
        instance.set_check_ssl_labs('TestValue1')
        assert 'TestValue1' == instance.get_check_ssl_labs()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs-TestValue1.txt')
        instance.set_check_ssl_labs('TestValue2')
        assert 'TestValue2' == instance.get_check_ssl_labs()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'check_ssl_labs-TestValue2.txt')

    def test_maximum_validity_default(self):
        instance = self.create_instance()
        assert None is instance.get_maximum_validity()

    def test_maximum_validity_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_maximum_validity()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'maximum_validity-default.txt')
        instance.set_maximum_validity('TestValue1')
        assert 'TestValue1' == instance.get_maximum_validity()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'maximum_validity-TestValue1.txt')
        instance.set_maximum_validity('TestValue2')
        assert 'TestValue2' == instance.get_maximum_validity()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'maximum_validity-TestValue2.txt')

    def test_nmap_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_nmap_bin()

    def test_nmap_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_nmap_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'nmap_bin-default.txt')
        instance.set_nmap_bin('TestValue1')
        assert 'TestValue1' == instance.get_nmap_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'nmap_bin-TestValue1.txt')
        instance.set_nmap_bin('TestValue2')
        assert 'TestValue2' == instance.get_nmap_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'nmap_bin-TestValue2.txt')

    def test_not_issued_by_default(self):
        instance = self.create_instance()
        assert None is instance.get_not_issued_by()

    def test_not_issued_by_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_not_issued_by()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_issued_by-default.txt')
        instance.set_not_issued_by('TestValue1')
        assert 'TestValue1' == instance.get_not_issued_by()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_issued_by-TestValue1.txt')
        instance.set_not_issued_by('TestValue2')
        assert 'TestValue2' == instance.get_not_issued_by()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_issued_by-TestValue2.txt')

    def test_not_valid_longer_than_default(self):
        instance = self.create_instance()
        assert None is instance.get_not_valid_longer_than()

    def test_not_valid_longer_than_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_not_valid_longer_than()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_valid_longer_than-default.txt')
        instance.set_not_valid_longer_than('TestValue1')
        assert 'TestValue1' == instance.get_not_valid_longer_than()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_valid_longer_than-TestValue1.txt')
        instance.set_not_valid_longer_than('TestValue2')
        assert 'TestValue2' == instance.get_not_valid_longer_than()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'not_valid_longer_than-TestValue2.txt')

    def test_org_default(self):
        instance = self.create_instance()
        assert None is instance.get_org()

    def test_org_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_org()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'org-default.txt')
        instance.set_org('TestValue1')
        assert 'TestValue1' == instance.get_org()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'org-TestValue1.txt')
        instance.set_org('TestValue2')
        assert 'TestValue2' == instance.get_org()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'org-TestValue2.txt')

    def test_openssl_default(self):
        instance = self.create_instance()
        assert None is instance.get_openssl()

    def test_openssl_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_openssl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'openssl-default.txt')
        instance.set_openssl('TestValue1')
        assert 'TestValue1' == instance.get_openssl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'openssl-TestValue1.txt')
        instance.set_openssl('TestValue2')
        assert 'TestValue2' == instance.get_openssl()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'openssl-TestValue2.txt')

    def test_path_default(self):
        instance = self.create_instance()
        assert None is instance.get_path()

    def test_path_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'path-default.txt')
        instance.set_path('TestValue1')
        assert 'TestValue1' == instance.get_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'path-TestValue1.txt')
        instance.set_path('TestValue2')
        assert 'TestValue2' == instance.get_path()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'path-TestValue2.txt')

    def test_precision_default(self):
        instance = self.create_instance()
        assert None is instance.get_precision()

    def test_precision_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_precision()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'precision-default.txt')
        instance.set_precision('TestValue1')
        assert 'TestValue1' == instance.get_precision()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'precision-TestValue1.txt')
        instance.set_precision('TestValue2')
        assert 'TestValue2' == instance.get_precision()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'precision-TestValue2.txt')

    def test_protocol_default(self):
        instance = self.create_instance()
        assert None is instance.get_protocol()

    def test_protocol_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_protocol()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'protocol-default.txt')
        instance.set_protocol('TestValue1')
        assert 'TestValue1' == instance.get_protocol()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'protocol-TestValue1.txt')
        instance.set_protocol('TestValue2')
        assert 'TestValue2' == instance.get_protocol()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'protocol-TestValue2.txt')

    def test_password_default(self):
        instance = self.create_instance()
        assert None is instance.get_password()

    def test_password_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_password()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'password-default.txt')
        instance.set_password('TestValue1')
        assert 'TestValue1' == instance.get_password()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'password-TestValue1.txt')
        instance.set_password('TestValue2')
        assert 'TestValue2' == instance.get_password()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'password-TestValue2.txt')

    def test_proxy_default(self):
        instance = self.create_instance()
        assert None is instance.get_proxy()

    def test_proxy_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_proxy()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'proxy-default.txt')
        instance.set_proxy('TestValue1')
        assert 'TestValue1' == instance.get_proxy()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'proxy-TestValue1.txt')
        instance.set_proxy('TestValue2')
        assert 'TestValue2' == instance.get_proxy()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'proxy-TestValue2.txt')

    def test_python_bin_default(self):
        instance = self.create_instance()
        assert None is instance.get_python_bin()

    def test_python_bin_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_python_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'python_bin-default.txt')
        instance.set_python_bin('TestValue1')
        assert 'TestValue1' == instance.get_python_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'python_bin-TestValue1.txt')
        instance.set_python_bin('TestValue2')
        assert 'TestValue2' == instance.get_python_bin()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'python_bin-TestValue2.txt')

    def test_rootcert_default(self):
        instance = self.create_instance()
        assert None is instance.get_rootcert()

    def test_rootcert_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_rootcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert-default.txt')
        instance.set_rootcert('TestValue1')
        assert 'TestValue1' == instance.get_rootcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert-TestValue1.txt')
        instance.set_rootcert('TestValue2')
        assert 'TestValue2' == instance.get_rootcert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert-TestValue2.txt')

    def test_require_dnssec_default(self):
        instance = self.create_instance()
        assert None is instance.get_require_dnssec()

    def test_require_dnssec_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_require_dnssec()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_dnssec-default.txt')
        instance.set_require_dnssec('TestValue1')
        assert 'TestValue1' == instance.get_require_dnssec()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_dnssec-TestValue1.txt')
        instance.set_require_dnssec('TestValue2')
        assert 'TestValue2' == instance.get_require_dnssec()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_dnssec-TestValue2.txt')

    def test_require_http_header_default(self):
        instance = self.create_instance()
        assert None is instance.get_require_http_header()

    def test_require_http_header_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_require_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_http_header-default.txt')
        instance.set_require_http_header('TestValue1')
        assert 'TestValue1' == instance.get_require_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_http_header-TestValue1.txt')
        instance.set_require_http_header('TestValue2')
        assert 'TestValue2' == instance.get_require_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_http_header-TestValue2.txt')

    def test_require_no_http_header_default(self):
        instance = self.create_instance()
        assert None is instance.get_require_no_http_header()

    def test_require_no_http_header_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_require_no_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_http_header-default.txt')
        instance.set_require_no_http_header('TestValue1')
        assert 'TestValue1' == instance.get_require_no_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_http_header-TestValue1.txt')
        instance.set_require_no_http_header('TestValue2')
        assert 'TestValue2' == instance.get_require_no_http_header()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_no_http_header-TestValue2.txt')

    def test_resolve_default(self):
        instance = self.create_instance()
        assert None is instance.get_resolve()

    def test_resolve_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_resolve()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'resolve-default.txt')
        instance.set_resolve('TestValue1')
        assert 'TestValue1' == instance.get_resolve()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'resolve-TestValue1.txt')
        instance.set_resolve('TestValue2')
        assert 'TestValue2' == instance.get_resolve()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'resolve-TestValue2.txt')

    def test_rootcert_dir_default(self):
        instance = self.create_instance()
        assert None is instance.get_rootcert_dir()

    def test_rootcert_dir_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_rootcert_dir()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-default.txt')
        instance.set_rootcert_dir('TestValue1')
        assert 'TestValue1' == instance.get_rootcert_dir()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-TestValue1.txt')
        instance.set_rootcert_dir('TestValue2')
        assert 'TestValue2' == instance.get_rootcert_dir()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-TestValue2.txt')

    def test_rootcert_file_default(self):
        instance = self.create_instance()
        assert None is instance.get_rootcert_file()

    def test_rootcert_file_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_rootcert_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-default.txt')
        instance.set_rootcert_file('TestValue1')
        assert 'TestValue1' == instance.get_rootcert_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-TestValue1.txt')
        instance.set_rootcert_file('TestValue2')
        assert 'TestValue2' == instance.get_rootcert_file()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'rootcert_dir-TestValue2.txt')

    def test_serial_default(self):
        instance = self.create_instance()
        assert None is instance.get_serial()

    def test_serial_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_serial()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'serial-default.txt')
        instance.set_serial('TestValue1')
        assert 'TestValue1' == instance.get_serial()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'serial-TestValue1.txt')
        instance.set_serial('TestValue2')
        assert 'TestValue2' == instance.get_serial()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'serial-TestValue2.txt')

    def test_sni_default(self):
        instance = self.create_instance()
        assert None is instance.get_sni()

    def test_sni_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_sni()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'sni-default.txt')
        instance.set_sni('TestValue1')
        assert 'TestValue1' == instance.get_sni()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'sni-TestValue1.txt')
        instance.set_sni('TestValue2')
        assert 'TestValue2' == instance.get_sni()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'sni-TestValue2.txt')

    def test_timeout_default(self):
        instance = self.create_instance()
        assert None is instance.get_timeout()

    def test_timeout_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_timeout()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'timeout-default.txt')
        instance.set_timeout('TestValue1')
        assert 'TestValue1' == instance.get_timeout()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'timeout-TestValue1.txt')
        instance.set_timeout('TestValue2')
        assert 'TestValue2' == instance.get_timeout()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'timeout-TestValue2.txt')

    def test_temp_default(self):
        instance = self.create_instance()
        assert None is instance.get_temp()

    def test_temp_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_temp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'temp-default.txt')
        instance.set_temp('TestValue1')
        assert 'TestValue1' == instance.get_temp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'temp-TestValue1.txt')
        instance.set_temp('TestValue2')
        assert 'TestValue2' == instance.get_temp()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'temp-TestValue2.txt')

    def test_url_default(self):
        instance = self.create_instance()
        assert None is instance.get_url()

    def test_url_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_url()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'url-default.txt')
        instance.set_url('TestValue1')
        assert 'TestValue1' == instance.get_url()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'url-TestValue1.txt')
        instance.set_url('TestValue2')
        assert 'TestValue2' == instance.get_url()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'url-TestValue2.txt')

    def test_xmpphost_default(self):
        instance = self.create_instance()
        assert None is instance.get_xmpphost()

    def test_xmpphost_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_xmpphost()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'xmpphost-default.txt')
        instance.set_xmpphost('TestValue1')
        assert 'TestValue1' == instance.get_xmpphost()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'xmpphost-TestValue1.txt')
        instance.set_xmpphost('TestValue2')
        assert 'TestValue2' == instance.get_xmpphost()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'xmpphost-TestValue2.txt')

    def test_user_agent_default(self):
        instance = self.create_instance()
        assert None is instance.get_user_agent()

    def test_user_agent_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_user_agent()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'user_agent-default.txt')
        instance.set_user_agent('TestValue1')
        assert 'TestValue1' == instance.get_user_agent()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'user_agent-TestValue1.txt')
        instance.set_user_agent('TestValue2')
        assert 'TestValue2' == instance.get_user_agent()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'user_agent-TestValue2.txt')

    def test_security_level_default(self):
        instance = self.create_instance()
        assert None is instance.get_security_level()

    def test_security_level_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_security_level()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'security_level-default.txt')
        instance.set_security_level(1)
        assert 1 == instance.get_security_level()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'security_level-1.txt')
        instance.set_security_level(2)
        assert 2 == instance.get_security_level()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'security_level-2.txt')

    def test_port_default(self):
        instance = self.create_instance()
        assert None is instance.get_port()

    def test_port_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_port()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'port-default.txt')
        instance.set_port(1)
        assert 1 == instance.get_port()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'port-1.txt')
        instance.set_port(2)
        assert 2 == instance.get_port()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'port-2.txt')

    def test_ocsp_critical_default(self):
        instance = self.create_instance()
        assert None is instance.get_ocsp_critical()

    def test_ocsp_critical_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_ocsp_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_critical-default.txt')
        instance.set_ocsp_critical(1)
        assert 1 == instance.get_ocsp_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_critical-1.txt')
        instance.set_ocsp_critical(2)
        assert 2 == instance.get_ocsp_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_critical-2.txt')

    def test_ocsp_warning_default(self):
        instance = self.create_instance()
        assert None is instance.get_ocsp_warning()

    def test_ocsp_warning_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_ocsp_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_warning-default.txt')
        instance.set_ocsp_warning(1)
        assert 1 == instance.get_ocsp_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_warning-1.txt')
        instance.set_ocsp_warning(2)
        assert 2 == instance.get_ocsp_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'ocsp_warning-2.txt')

    def test_critical_default(self):
        instance = self.create_instance()
        assert None is instance.get_critical()

    def test_critical_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'critical-default.txt')
        instance.set_critical(1)
        assert 1 == instance.get_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'critical-1.txt')
        instance.set_critical(2)
        assert 2 == instance.get_critical()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'critical-2.txt')

    def test_warning_default(self):
        instance = self.create_instance()
        assert None is instance.get_warning()

    def test_warning_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'warning-default.txt')
        instance.set_warning(1)
        assert 1 == instance.get_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'warning-1.txt')
        instance.set_warning(2)
        assert 2 == instance.get_warning()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'warning-2.txt')

    def test_element_default(self):
        instance = self.create_instance()
        assert None is instance.get_element()

    def test_element_value(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_element()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'element-default.txt')
        instance.set_element(1)
        assert 1 == instance.get_element()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'element-1.txt')
        instance.set_element(2)
        assert 2 == instance.get_element()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'element-2.txt')

    def test_long_output_default(self):
        instance = self.create_instance()
        assert 0 == len(instance.get_long_output())

    def test_long_output_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-default.txt')
        values1 = ["ABC", "DEF"]
        instance.set_long_output(values1)
        assert len(values1) == len(instance.get_long_output())
        assert values1 == instance.get_long_output()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-values1.txt')
        values2 = ["UVW", "XYZ"]
        instance.set_long_output(values2)
        assert len(values2) == len(instance.get_long_output())
        assert values2 == instance.get_long_output()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-values2.txt')
        values3 = []
        instance.set_long_output(values3)
        assert len(values3) == len(instance.get_long_output())
        assert values3 == instance.get_long_output()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-values3.txt')
    def test_long_output_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_long_output())
        instance.add_long_output("ABC")
        assert 1 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''),'long_output-1.txt')
        instance.remove_long_output('XYZ')
        assert 1 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-2.txt')
        instance.add_long_output('XYZ')
        assert 2 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-3.txt')
        instance.remove_long_output("XYZ")
        assert 1 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-4.txt')
        instance.remove_long_output("ABC")
        assert 0 == len(instance.get_long_output())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'long_output-5.txt')
    def test_require_client_cert_default(self):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_client_cert())

    def test_require_client_cert_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-default.txt')
        values1 = ["ABC", "DEF"]
        instance.set_require_client_cert(values1)
        assert len(values1) == len(instance.get_require_client_cert())
        assert values1 == instance.get_require_client_cert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-values1.txt')
        values2 = ["UVW", "XYZ"]
        instance.set_require_client_cert(values2)
        assert len(values2) == len(instance.get_require_client_cert())
        assert values2 == instance.get_require_client_cert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-values2.txt')
        values3 = []
        instance.set_require_client_cert(values3)
        assert len(values3) == len(instance.get_require_client_cert())
        assert values3 == instance.get_require_client_cert()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-values3.txt')

    def test_require_client_cert_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_client_cert())
        instance.add_require_client_cert("ABC")
        assert 1 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''),'require_client_cert-1.txt')
        instance.remove_require_client_cert('XYZ')
        assert 1 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-2.txt')
        instance.add_require_client_cert('XYZ')
        assert 2 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-3.txt')
        instance.remove_require_client_cert("XYZ")
        assert 1 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-4.txt')
        instance.remove_require_client_cert("ABC")
        assert 0 == len(instance.get_require_client_cert())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_client_cert-5.txt')




    def test_dane_default(self):
        instance = self.create_instance()
        assert 0 ==len( instance.get_dane())
    def test_dane_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_dane())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-default.txt')
        values1 = ["ABC", "DEF"]
        instance.set_dane(values1)
        assert len(values1) == len(instance.get_dane())
        assert values1 == instance.get_dane()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-1.txt')
        values2 = ["UVW", "XYZ"]
        instance.set_dane(values2)
        assert len(values2) == len(instance.get_dane())
        assert values2 == instance.get_dane()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-2.txt')
        
    def test_dane_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_dane()) 
        instance.add_dane("ABC")
        assert 1 == len(instance.get_dane())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-1.txt')
        instance.remove_dane("XYZ")
        assert 1 == len(instance.get_dane())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-2.txt')
        instance.remove_dane("ABC")
        assert 0 == len(instance.get_dane())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'dane-3.txt')
    def test_match_default(self):
        instance = self.create_instance()
        assert 0 == len(instance.get_match())
    def test_match_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_match())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-default.txt')
        values1 = ["ABC", "DEF"]
        instance.set_match(values1)
        assert len(values1) == len(instance.get_match())
        assert values1 == instance.get_match()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-1.txt')
        values2 = ["UVW", "XYZ"]
        instance.set_match(values2)
        assert len(values2) == len(instance.get_match())
        assert values2 == instance.get_match()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-2.txt')
        
    def test_match_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_match()) 
        instance.add_match("ABC")
        assert 1 == len(instance.get_match())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-1.txt')
        instance.remove_match("XYZ")
        assert 1 == len(instance.get_match())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-2.txt')
        instance.remove_match("ABC")
        assert 0 == len(instance.get_match())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'match-3.txt')
    def test_require_purpose_default(self):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_purpose())
    def test_require_purpose_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_purpose())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-default.txt')
        values1 = ["ABC", "DEF"]
        instance.set_require_purpose(values1)
        assert len(values1) == len(instance.get_require_purpose())
        assert values1 == instance.get_require_purpose()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-1.txt')
        values2 = ["UVW", "XYZ"]
        instance.set_require_purpose(values2)
        assert len(values2) == len(instance.get_require_purpose())
        assert values2 == instance.get_require_purpose()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-2.txt')
        
    def test_require_purpose_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_require_purpose()) 
        instance.add_require_purpose("ABC")
        assert 1 == len(instance.get_require_purpose())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-1.txt')
        instance.remove_require_purpose("XYZ")
        assert 1 == len(instance.get_require_purpose())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-2.txt')
        instance.remove_require_purpose("ABC")
        assert 0 == len(instance.get_require_purpose())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'require_purpose-3.txt')
    def test_skip_element_default(self):
        instance = self.create_instance()
        assert 0 == len(instance.get_skip_element())
    def test_skip_element_set(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_skip_element())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-default.txt')
        values1 = [0, 1]
        instance.set_skip_element(values1)
        assert len(values1) == len(instance.get_skip_element())
        assert values1 == instance.get_skip_element()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-1.txt')
        values2 = [4, 5]
        instance.set_skip_element(values2)
        assert len(values2) == len(instance.get_skip_element())
        assert values2 == instance.get_skip_element()
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-2.txt')
        
    def test_skip_element_add_remove(self, snapshot):
        instance = self.create_instance()
        assert 0 == len(instance.get_skip_element()) 
        instance.add_skip_element(1)
        assert 1 == len(instance.get_skip_element())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-1.txt')
        instance.remove_skip_element(2)
        assert 1 == len(instance.get_skip_element())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-2.txt')
        instance.remove_skip_element(1)
        assert 0 == len(instance.get_skip_element())
        snapshot.assert_match(instance.get_config().replace('  ', ''), 'skip_element-3.txt')
