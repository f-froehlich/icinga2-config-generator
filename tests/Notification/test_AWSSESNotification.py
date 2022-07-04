from icinga2confgen.ConfigBuilder import ConfigBuilder
from icinga2confgen.Notification.AWSSESNotification import AWSSESNotification
from icinga2confgen.Notification.AWSSESNotificationCommand import AWSSESNotificationCommand

from tests.BaseNotificationTest import BaseNotificationTest


class TestAWSSESNotification(BaseNotificationTest):

    def get_instance_class(self):
        return AWSSESNotification

    def get_command_class(self):
        return AWSSESNotificationCommand

    def test_have_correct_key_id(self, snapshot):
        instance = self.create_instance()
        instance.set_key_id('THIS_IS_A_KEY')
        assert 'THIS_IS_A_KEY' == instance.get_key_id()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_secret(self, snapshot):
        instance = self.create_instance()
        instance.set_secret('THIS_IS_A_SECRET')
        assert 'THIS_IS_A_SECRET' == instance.get_secret()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_sender(self, snapshot):
        instance = self.create_instance()
        instance.set_sender('THIS_IS_A_SENDER')
        assert 'THIS_IS_A_SENDER' == instance.get_sender()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_region(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_region()

        instance.set_region('THIS_IS_A_REGION')
        assert 'THIS_IS_A_REGION' == instance.get_region()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_subject_template(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_subject_template()

        instance.set_subject_template('THIS_IS_A_SUBJECT_TEMPLATE')
        assert 'THIS_IS_A_SUBJECT_TEMPLATE' == instance.get_subject_template()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_message_template_short(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_message_template_short()

        instance.set_message_template_short('THIS_IS_A_MESSAGE_TEMPLATE_SHORT')
        assert 'THIS_IS_A_MESSAGE_TEMPLATE_SHORT' == instance.get_message_template_short()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')

    def test_have_correct_message_template_additional(self, snapshot):
        instance = self.create_instance()
        assert None is instance.get_message_template_additional()

        instance.set_message_template_additional('THIS_IS_A_MESSAGE_TEMPLATE_ADDITIONAL')
        assert 'THIS_IS_A_MESSAGE_TEMPLATE_ADDITIONAL' == instance.get_message_template_additional()
        snapshot.assert_match(ConfigBuilder.get_config_as_string().replace('  ', ''), 'config.txt')
