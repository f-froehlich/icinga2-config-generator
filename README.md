Icinga2 configuration generator
===============================
Icinga2 configuration file generator for hosts, commands, checks, ... in python 

Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> [https://icinga2.confgen.org](https://icinga2.confgen.org)

Full License Information see  [https://github.com/f-froehlich/icinga2-config-generator/blob/master/LICENSE](LICENSE) file in root directory of this source code and License section of this File.

# Donate
This project needs donations. Please check out [https://icinga2.confgen.org/Donate](https://icinga2.confgen.org/Donate) for details.

# Quick setup
See our [documentation](https://icinga2.confgen.org) for details.

## Prerequisite
* install check plugins, that you need e.g. [our Plugins](https://github.com/f-froehlich/icinga2-config-generator/tree/master/plugins), [Monitoring Plugins](https://www.monitoring-plugins.org) or [Nagios Plugins](https://github.com/harisekhon/nagios-plugins)
* install icinga2
* install icingaweb2

## Required
* install python 3.7 (other versions may also work)
* install python3-pip
* `pip3 install icinga2confgen`

## Optional
If you want to use our monitoring plugins, it is recommended to create a group on all your server and grant the permission to it. See our [documentation](https://icinga2.confgen.org) for details.
* create group `monitorpermissions` and add user `icinga2` to the group (`usermod -aG monitorpermissions icinga2`). Note that the username, who runs icinga2 daemon, may be different.

### Install our Plugins
Just copy or link the plugins into your `plugindir`. A few plugins need other libaries as `curl` or `dig`. See our [documentation](https://icinga2.confgen.org) for details.


# Notice
Because there are many different check plugin libraries we sort our commands and checks into different modules. Therefore we using the parameter description of the Plugins itself, so you can lookup the documentation of the plugins on there project page.

* [Checks/Icinga2Confgen](https://icinga2.confgen.org)
* [Checks/MonitoringPlugins](https://www.monitoring-plugins.org)
* [Checks/NagiosPlugins](https://github.com/harisekhon/nagios-plugins)

# License
This section contains the additional terms of the AGPLv3 license agreement, a copy of the AGPLv3 is included in the [LICENSE](https://github.com/f-froehlich/icinga2-config-generator/blob/master/LICENSE) file.

1. Adaptation of the [https://github.com/f-froehlich/icinga2-config-generator/blob/master/REDME.md](README.md) is prohibited. The file must also be included with each copy without any modification. 

2. Adjustments of any kind must be listed in the attached [https://github.com/f-froehlich/icinga2-config-generator/blob/master/CHANGELOG.md](CHANGELOG.md) file. It is sufficient to name the change and the reason for the change here and to give appropriate references to the processing in the source code at the appropriate place.

3. All edited copies must be made available on [github](https://github.com). You have to fork the original repository or use a fork from the original repository.

4. You have to place the following link on your Homepage in a suitable place, if you using this software ***not*** only for your own Servers, Applications, ...:

    ```html
    We using monitoring tools from <a href="https://icinga2.confgen.org">Fabian Fr&ouml;hlich</a>
   ```

    The wording is decisive here, so another language may be used. Attributes of the link may also be adjusted, but the link must be followable by web crawlers (e.g. Googlebot).

    Furthermore, the imprint has to include a clear reference to the original github repository [https://github.com/f-froehlich/icinga2-config-generator](https://github.com/f-froehlich/icinga2-config-generator) as well as the link mentioned above in the body text.
    
5. You are not allowed to earn money with this tool.