from icinga2confgen.Checks.HariSekhonNagiosPlugins.CheckYum import CheckYum
from icinga2confgen.Commands.HariSekhonNagiosPlugins.YumCommand import YumCommand
from icinga2confgen.Groups.ServiceGroup import ServiceGroup
from tests.BaseCheckTest import BaseCheckTest


class TestCheckYum(BaseCheckTest):

    def get_instance_class(self):
        return CheckYum

    def get_command_class(self):
        return YumCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
            ServiceGroup.create('yum'),
            ServiceGroup.create('updates'),
        ]

    def test_get_right_timeout(self):
        instance = self.create_instance()
        instance.set_timeout(55)

        assert 55 == instance.get_timeout()

    def test_get_right_all_updates(self):
        instance = self.create_instance()

        instance.set_all_updates(True)
        assert instance.get_all_updates()

        instance.set_all_updates(False)
        assert not instance.get_all_updates()

    def test_get_right_warn_any_update(self):
        instance = self.create_instance()

        instance.set_warn_any_update(True)
        assert instance.get_warn_any_update()

        instance.set_warn_any_update(False)
        assert not instance.get_warn_any_update()

    def test_get_right_no_warn_on_lock(self):
        instance = self.create_instance()

        instance.set_no_warn_on_lock(True)
        assert instance.get_no_warn_on_lock()

        instance.set_no_warn_on_lock(False)
        assert not instance.get_no_warn_on_lock()

    def test_get_right_cache_only(self):
        instance = self.create_instance()

        instance.set_cache_only(True)
        assert instance.get_cache_only()

        instance.set_cache_only(False)
        assert not instance.get_cache_only()

    def test_get_right_yum_config(self):
        instance = self.create_instance()

        instance.set_yum_config('yum_config')
        assert 'yum_config' == instance.get_yum_config()

    def test_get_right_plugin_disabled(self):
        instance = self.create_instance()

        instance.set_plugin_disabled('plugin_disabled')
        assert 'plugin_disabled' == instance.get_plugin_disabled()

    def test_get_right_repo_disabled(self):
        instance = self.create_instance()

        instance.set_repo_disabled('repo_disabled')
        assert 'repo_disabled' == instance.get_repo_disabled()

    def test_get_right_repo_enabled(self):
        instance = self.create_instance()

        instance.set_repo_enabled('repo_enabled')
        assert 'repo_enabled' == instance.get_repo_enabled()
