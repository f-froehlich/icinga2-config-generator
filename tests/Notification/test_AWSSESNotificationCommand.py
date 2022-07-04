from icinga2confgen.Notification.AWSSESNotificationCommand import AWSSESNotificationCommand
from tests.BaseNotificationCommandTest import BaseNotificationCommandTest


class TestAWSSESNotificationCommand(BaseNotificationCommandTest):

    def get_instance_class(self):
        return AWSSESNotificationCommand

    def get_command_executable_host(self):
        return 'aws_ses_notification_host.py'

    def get_command_executable_service(self):
        return 'aws_ses_notification_service.py'

    def get_script_dir(self):
        return '$monitoring_script_dir$'

    def test_get_command_definition_service(self, snapshot):
        instance = self.create_instance()
        snapshot.assert_match(instance.get_aws_ses_args().replace('  ', ''),
                              'aws_ses_args.txt')
