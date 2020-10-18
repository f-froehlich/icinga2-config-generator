Icinga2 configuration generator
===============================
Icinga2 configuration file generator for hosts, commands, checks, ... in python 

Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> [https://icinga2.confgen.org](https://icinga2.confgen.org)

Full License Information see  [LICENSE](LICENSE) file in root directory of this source code and License section of this File.

# Setup
## Required
* install check plugins, that you need e.g. [our Plugins](plugins), [Monitoring Plugins](https://www.monitoring-plugins.org) or [Nagios Plugins](https://github.com/harisekhon/nagios-plugins)
* install icinga2
* install icingaweb2
* install python 3.7 (other versions may also work)
* create group `monitorpermissions` and add user `icinga2` to the group (`usermod -aG monitorpermissions icinga2`). Note that the username, who runs icinga2 daemon, may be different.

## Optional

### Install our Plugins
Just copy or link the plugins into your `plugindir`. A few plugins need other libaries as `curl` or `dig`. See installation instructions for each check for details or run the plugin and follow instructions.



#### Deny TLS Version check
Check if a Server denies a TLS Version. It is recommended to check TLSv1.0 and TLSv1.1. 
* require `curl`
* link or copy `plugins/check_deny_tls_version.sh` to `plugindir` 

#### Path exist
Check if a Dir or File exist
* link or copy `plugins/check_path_exists.sh` to `plugindir` 

#### Group Members
Check Members of given group
* link or copy `plugins/check_group_members.py` to `plugindir`

***NOTICE:*** It is recommended to check the sudoers of a server.

#### Existing users
Check if only given users exists
* link or copy `plugins/check_existing_users.py` to `plugindir`

#### Docker login
Check if login into docker registry succeed
* link or copy `plugins/check_docker_login.sh` to `plugindir`
* require `docker`
* User of check must have the permission to execute docker commands. You can also run this command as sudo but you should only give the permission to execute `docker` as root.

***NOTICE:*** Due security reasons, you should only use credentials without any privileges on the registry
Recommendated configuration for sudo on `docker login`
```shell script
# /etc/sudoers.d/monitorpermissions

Cmnd_Alias            DOCKERLOGIN = /usr/bin/docker login
%monitorpermissions   ALL=NOPASSWD: DOCKERLOGIN
```

#### SSHD Security
Check the running configuration from sshd.
* link or copy `plugins/check_sshd_security.py` to `plugindir`
* require python3 (other versions may also work, change interpreter in executable)
* require sshd daemon
* require root access on `sshd -T`

Recommendated configuration for sudo on `sshd -T`
```shell script
# /etc/sudoers.d/monitorpermissions

Cmnd_Alias            SSHDCONFIG = /usr/sbin/sshd -T
%monitorpermissions   ALL=NOPASSWD: SSHDCONFIG
```

#### DNSSEC
Clone [https://github.com/f-froehlich/check_dnssec_expiry](https://github.com/f-froehlich/check_dnssec_expiry) and link `check_dnssec_expiry.sh` into `/usr/lib/nagios/plugins/`
Be sure you have `dig` installed


# Notice
Because there are many different check plugin libraries we sort our commands and checks into different modules. Therefore we using the parameter description of the Plugins itself, so you can lookup the documentation of the plugins on there project page.

* [Checks/Icinga2Confgen](https://icinga2.confgen.org)
* [Checks/MonitoringPlugins](https://www.monitoring-plugins.org)
* [Checks/NagiosPlugins](https://github.com/harisekhon/nagios-plugins)

# License
This section contains the additional terms of the AGPLv3 license agreement, a copy of the AGPLv3 is included in the [LICENSE](LICENSE) file.

1. Adaptation of the [README.md](README.md) is prohibited. The file must also be included with each copy without any modification. 

2. Adjustments of any kind must be listed in the attached [CHANGELOG.md](CHANGELOG.md) file. It is sufficient to name the change and the reason for the change here and to give appropriate references to the processing in the source code at the appropriate place.

3. All edited copies must be made available on [github](https://github.com). You have to fork the original repository or use a fork from the original repository.

4. You have to place the following link on your Homepage in a suitable place, if you using this software ***not*** only for your own Servers, Applications, ...:

    ```html
    We using monitoring configuration tools from <a href="https://icinga2.confgen.org">Fabian Fr&ouml;hlich</a>
   ```

    The wording is decisive here, so another language may be used. Attributes of the link may also be adjusted, but the link must be followable by web crawlers (e.g. Googlebot).

    Furthermore, the imprint has to include a clear reference to the original github repository [https://github.com/f-froehlich/icinga2-config-generator](https://github.com/f-froehlich/icinga2-config-generator) as well as the link mentioned above in the body text.
    
5. You have to sign up to a free account on our [project page](https://icinga2.confgen.org), if you are using this configuration generator in commercial way.

