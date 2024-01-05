import pytest

from icinga2confgen.Checks.MonitoringPlugins.Git.CheckGithubLatestRelease import CheckGithubLatestRelease
from icinga2confgen.Commands.MonitoringPlugins.Git.GithubLatestReleaseCommand import GithubLatestReleaseCommand
from tests.BaseCheckTest import BaseCheckTest


class TestCheckGithubLatestRelease(BaseCheckTest):

    def get_instance_class(self):
        return CheckGithubLatestRelease

    def get_command_class(self):
        return GithubLatestReleaseCommand

    def get_default_check_interval(self) -> str:
        return '15m'

    def get_default_service_groups(self):
        return [
        ]

    def create_instance(self, force=False):
        instance = BaseCheckTest.create_instance(self, force)
        instance.set_expected('expected')
        instance.set_repository('repository')
        return instance

    def test_validate_raise_exception_if_repository_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_expected('expected')

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'repository' in str(excinfo.value)

    def test_validate_raise_exception_if_expected_not_set(self):
        instance = BaseCheckTest.create_instance(self)
        instance.set_repository('repository')

        self.validate_snapshot = False
        with pytest.raises(Exception) as excinfo:
            instance.validate()
        assert 'expected' in str(excinfo.value)

    def test_validate_set_timeout(self):
        instance = self.create_instance()
        instance.set_timeout(55)

        assert 55 == instance.get_timeout()

    def test_validate_set_expected(self):
        instance = self.create_instance()
        instance.set_expected("my_expected")

        assert "my_expected" == instance.get_expected()

    def test_validate_set_repository(self):
        instance = self.create_instance()
        instance.set_repository("my_repository")

        assert "my_repository" == instance.get_repository()
