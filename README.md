Icinga2 configuration generator
===============================
Icinga2 configuration file generator for hosts, commands, checks, ... in python 

Copyright (c) 2020 Fabian Fröhlich <mail@icinga2.confgen.org> [https://icinga2.confgen.org](https://icinga2.confgen.org)

Full License Information see  [LICENSE](LICENSE) file in root directory of this source code and License section of this File.

# Setup
## required
* install nagios plugins
* install icinga2
* install icingaweb2
* install python 3.7 (other versions could also working)


## dnssec
Clone [https://github.com/f-froehlich/check_dnssec_expiry](https://github.com/f-froehlich/check_dnssec_expiry) and link `check_dnssec_expiry.sh` into `/usr/lib/nagios/plugins/`
Be sure you have `dig` installed

## Deny TLS Version check
* link or copy `plugins/check_deny_tls_version.sh` to `/usr/lib/nagios/plugins` 

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

