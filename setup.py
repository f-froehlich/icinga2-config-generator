from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='icinga2confgen',
    version='0.0.3',
    description='Icinga2 configuration file generator for hosts, commands, checks, ... in python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='AGPLv3',
    packages=find_packages(),
    author='Fabian Fröhlich',
    author_email='mail@confgen.org',
    keywords=['icinga', 'icinga2', 'icinga2-configuration', 'icinga2-plugin', 'configuration',
              'configuration-management', 'monitoring', 'check', 'nagios', 'nagios-plugin', 'nrpe', 'healthcheck',
              'serverstatus', 'security', 'security-tools'],
    url='https://github.com/f-froehlich/icinga2-config-generator',
    download_url='https://pypi.org/project/icinga2confgen/'

)

install_requires = [
    'tqdm',
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
