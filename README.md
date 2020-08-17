Icinga2 configuration generator
===============================
Icinga2 configuration file generator for hosts, commands, checks, ... in python 

Copyright (c) 2020 Fabian Fröhlich <mail@f-froehlich.de>

Full License Information see  [LICENSE](LICENSE) file in root directory of this source code and License section of this File.

# Setup
## required
* install nagios plugins
* install icinga2
* install python 3.7 (other versions could also working)


## dnssec
Clone [https://github.com/f-froehlich/check_dnssec_expiry](https://github.com/f-froehlich/check_dnssec_expiry) and link `check_dnssec_expiry.sh` into `/usr/lib/nagios/plugins/`
Be sure you have `dig` installed

# License
This section contains the additional terms of the AGPLv3 license agreement, a copy of the AGPLv3 is included in the [LICENSE](LICENSE) file.

1. Adaptation of the [README.md](README.md) is prohibited. The file must also be included with each copy without any modification. 
K
2. Adjustments of any kind must be listed in the attached [CHANGELOG.md](CHANGELOG.md) file. It is sufficient to name the change and the reason for the change here and to give appropriate references to the processing in the source code at the appropriate place.

3. All edited copies must be made available on [github](https://github.com). You have to fork the original repository or use a fork from the original repository.

4. Each editor of copies can adapt the license terms for his source code. At the appropriate place in the [CHANGELOG.md](CHANGELOG.md) and in the source code there must be a corresponding note on adaptation of the license and where it is located. The adaptation of the license must be enclosed in a separate document with the source code.
Further license terms must not restrict already existing terms. If they nevertheless violate the terms, they shall be considered invalid.

5. You have to place the following link on your Homepage in a suitable place, if you using this software ***not*** only for your own Servers, Applications, ...:

    ```html
    We using monitoring configuration tools from <a href="https://icinga2.confgen.org">Fabian Fr&ouml;hlich</a>
   ```

    The wording is decisive here, so another language may be used. Attributes of the link may also be adjusted, but the link must be followable by web crawlers (e.g. Googlebot).

    Furthermore, the imprint has to include a clear reference to the original github repository [https://github.com/f-froehlich/icinga2-config-generator](https://github.com/f-froehlich/icinga2-config-generator) as well as the link mentioned above in the body text.

