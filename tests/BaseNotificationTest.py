from abc import abstractmethod

import pytest

from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Groups.UserGroup import UserGroup
from icinga2confgen.Notification.TimePeriod import TimePeriod
from icinga2confgen.User.User import User
from tests.BaseTest import BaseTest


class BaseNotificationTest(BaseTest):

    @abstractmethod
    def get_command_class(self):
        raise NotImplementedError()

    def create_instance(self, force=False):
        instance = BaseTest.create_instance(self, force)

        user = User.create('BaseTestUser')
        user.add_email('user1@mail1')
        user.add_email('user1@mail2')

        instance.add_user(user)

        user_group = UserGroup.create('BaseTestUserGroup')
        user_group.add_email('group1@mail1')
        user_group.add_email('group1@mail2')

        instance.add_user_group(user_group)

        instance.set_key_id('KEY_ID')
        instance.set_secret('SECRET')
        instance.set_sender('SENDER')

        return instance

    def test_can_get_instance_from_config_builder(self):
        instance = self.create_instance()
        assert instance == ConfigBuilder.get_notification('instance')

    def test_has_correct_notification_command(self):
        instance = self.create_instance()
        assert isinstance(instance.get_command_config(), self.get_command_class())

    def test_has_correct_time_period(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_time_period()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'no_period.txt')

        tp1 = TimePeriod.create('tp1')
        instance.set_time_period('tp1')
        assert 'tp1' == instance.get_time_period()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'tp1.txt')

        tp2 = TimePeriod.create('tp2')
        instance.set_time_period(tp2)
        assert 'tp2' == instance.get_time_period()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'tp2.txt')

        with pytest.raises(Exception) as excinfo:
            instance.set_time_period('tp3')

        with pytest.raises(Exception) as excinfo:
            instance.set_time_period(None)

    def test_have_correct_id(self):
        instance = self.create_instance()
        assert 'instance' == instance.get_id()

    def test_have_correct_interval(self, snapshot):
        instance = self.create_instance()
        assert '1h' == instance.get_interval()
        instance.set_interval('2h')

        assert '2h' == instance.get_interval()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_escalation(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_escalation()
        escalation = ('1h', '2h')
        instance.set_escalation(escalation[0], escalation[1])

        assert escalation == instance.get_escalation()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_set_host_types(self, snapshot):
        instance = self.create_instance()

        host_types = ['DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved', 'Custom', 'Acknowledgement', 'Problem',
                      'Recovery', 'FlappingStart', 'FlappingEnd']
        assert host_types == instance.get_host_types()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        for host_type in host_types:
            instance.set_host_types([host_type])
            assert [host_type] == instance.get_host_types()
            snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), f'config_{host_type}.txt')

        with pytest.raises(Exception) as excinfo:
            instance.set_host_types(['NoType'])

    def test_set_host_states(self, snapshot):
        instance = self.create_instance()

        host_states = ['Up', 'Down']
        assert host_states == instance.get_host_states()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        for host_state in host_states:
            instance.set_host_states([host_state])
            assert [host_state] == instance.get_host_states()
            snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), f'config_{host_state}.txt')

        with pytest.raises(Exception) as excinfo:
            instance.set_host_states(['NoType'])

    def test_set_service_types(self, snapshot):
        instance = self.create_instance()

        service_types = ['DowntimeStart', 'DowntimeEnd', 'DowntimeRemoved', 'Custom', 'Acknowledgement',
                         'Problem', 'Recovery', 'FlappingStart', 'FlappingEnd']
        assert service_types == instance.get_service_types()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        for service_type in service_types:
            instance.set_service_types([service_type])
            assert [service_type] == instance.get_service_types()
            snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), f'config_{service_type}.txt')

        with pytest.raises(Exception) as excinfo:
            instance.set_service_types(['NoType'])

    def test_set_service_states(self, snapshot):
        instance = self.create_instance()

        service_states = ['Warning', 'Critical', 'Unknown', 'OK']

        assert service_states == instance.get_service_states()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        for service_state in service_states:
            instance.set_service_states([service_state])
            assert [service_state] == instance.get_service_states()
            snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), f'config_{service_state}.txt')

        with pytest.raises(Exception) as excinfo:
            instance.set_service_states(['NoType'])

    def test_add_user(self, snapshot):
        instance = self.create_instance()

        user = User.create('testUser')
        instance.add_user(user)

        assert 2 == len(instance.get_users())
        assert user in instance.get_users()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        instance.add_user(user)
        assert 2 == len(instance.get_users())
        assert user in instance.get_users()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        instance.add_user('testUser')
        assert 2 == len(instance.get_users())
        assert user in instance.get_users()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        with pytest.raises(Exception) as excinfo:
            instance.add_user('NotExisting')

        with pytest.raises(Exception) as excinfo:
            instance.add_user(None)

    def test_remove_user(self, snapshot):
        instance = self.create_instance()

        user = User.create('testUser')
        instance.add_user(user)

        assert 2 == len(instance.get_users())
        assert user in instance.get_users()

        instance.remove_user(user)
        assert 1 == len(instance.get_users())
        assert user not in instance.get_users()

        instance.add_user('testUser')
        assert 2 == len(instance.get_users())
        assert user in instance.get_users()

        instance.remove_user('testUser')
        assert 1 == len(instance.get_users())
        assert user not in instance.get_users()

        instance.remove_user('notExisting')
        assert 1 == len(instance.get_users())

    def test_add_user_group(self, snapshot):
        instance = self.create_instance()

        user_group = UserGroup.create('testUserGroup')
        instance.add_user_group(user_group)

        assert 2 == len(instance.get_user_groups())
        assert user_group in instance.get_user_groups()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        instance.add_user_group(user_group)
        assert 2 == len(instance.get_user_groups())
        assert user_group in instance.get_user_groups()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        instance.add_user_group('testUserGroup')
        assert 2 == len(instance.get_user_groups())
        assert user_group in instance.get_user_groups()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

        with pytest.raises(Exception) as excinfo:
            instance.add_user_group('NotExisting')

        with pytest.raises(Exception) as excinfo:
            instance.add_user_group(None)

    def test_remove_user_group(self, snapshot):
        instance = self.create_instance()

        user_group = UserGroup.create('testUserGroup')
        instance.add_user_group(user_group)

        assert 2 == len(instance.get_user_groups())
        assert user_group in instance.get_user_groups()

        instance.remove_user_group(user_group)
        assert 1 == len(instance.get_user_groups())
        assert user_group not in instance.get_user_groups()

        instance.add_user_group('testUserGroup')
        assert 2 == len(instance.get_user_groups())
        assert user_group in instance.get_user_groups()

        instance.remove_user_group('testUserGroup')
        assert 1 == len(instance.get_user_groups())
        assert user_group not in instance.get_user_groups()

        instance.remove_user_group('notExisting')
        assert 1 == len(instance.get_user_groups())
