#!/usr/bin/python3


import argparse
import binascii
import sys
import subprocess


class SSHDSecurity:

    def __init__(self, args):
        self.__args = args
        self.__running_config = self.get_running_config()

    def main(self):

        for arg in self.__args:
            if 'config' is arg[0]:
                if None is not arg[1]:
                    for config in arg[1]:
                        config = config.split("=")
                        self.check_value(config[0], config[1].split("|"))
            else:
                self.check_value(arg[0], [arg[1]])

    def check_value(self, option, expected_array):

        if 1 == len(expected_array):
            expected = expected_array[0]
            for config in self.__running_config:
                if config[0] == option:
                    if str(config[1]).lower() != str(expected).lower():
                        print(
                            "WARNING: Configuration does not match expected value for param " + option + ". Expected: " + str(
                                expected) + " got: " + str(config[1]))
                        sys.exit(1)
                    return
            print("WARNING: Can't find expected configuration " + option + ". Expected: " + str(expected))
            sys.exit(1)
        else:
            current_values = []
            for config in self.__running_config:
                if config[0] == option:
                    current_values.append(config[1])

            not_existing_in_config = []
            exist_in_config_but_not_expected = []

            for expected in expected_array:
                if expected not in current_values:
                    not_existing_in_config.append(expected)

            for current in current_values:
                if current not in expected_array:
                    exist_in_config_but_not_expected.append(current)

            if 0 != len(not_existing_in_config):
                print(
                    "WARNING: There are some values of configuration '" + option + "' expected, which are not configured yet! Not configured values: " + ", ".join(
                        not_existing_in_config))
                sys.exit(1)

            if 0 != len(exist_in_config_but_not_expected):
                print(
                    "WARNING: There are some values of configuration '" + option + "' configured, which are not expected! Not expected values: " + ", ".join(
                        exist_in_config_but_not_expected))
                sys.exit(1)

    def get_running_config(self):
        out = subprocess.Popen(['sudo', '-n', 'sshd', '-T'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout, stderr = out.communicate()

        if 0 is not out.returncode:
            stderr = stderr.decode("utf-8")
            if 'a password is required' in stderr:
                print(
                    'UNKNOWN: can\'t run sudo without password. Please give executable rights without password in /ets/sudoers for sshd command.')
            else:
                print('UNKNOWN: ' + stderr)

            sys.exit(3)
        stdout = stdout.decode("utf-8")

        parsed_config = []
        for config in stdout.split("\n"):
            config = config.split(" ")
            key = config[0]
            value = " ".join(config[1:])
            parsed_config.append((key, value))

        return parsed_config


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check sshd config')

    parser.add_argument('-r', '--permit-root-login', dest='permitrootlogin',
                        choices=['yes', 'no', 'without-password', 'forced-commands-only'], default='no',
                        help='Permit root login')
    parser.add_argument('-k', '--public-key-auth', dest='pubkeyauthentication', choices=['yes', 'no'], default='yes',
                        help='Public key authentication')
    parser.add_argument('-P', '--password-auth', dest='passwordauthentication', choices=['yes', 'no'], default='no',
                        help='Password authentication')
    parser.add_argument('--permit-empty-passwords', dest='permitemptypasswords', choices=['yes', 'no'], default='no',
                        help='Permit empty passwords')
    parser.add_argument('-H', '--fingerprint-hash', dest='fingerprinthash', default='SHA256',
                        help='Fingerprint Hash function')
    parser.add_argument('-p', '--port', dest='port', type=int, default=22, help='Listen port')
    parser.add_argument('-C', '--config', dest='config', action='append',
                        help='Other config values to check. Format: OPTION=VALUE_1|VALUE_2|...|VALUE_N')

    args = parser.parse_args()

    SSHDSecurity(args._get_kwargs()).main()