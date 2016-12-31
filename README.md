# webpagetest.py

> IN DEVELOPMENT

## Overview

Command line utility to schedule tests with WebPageTest.org & get a test comparison url.

See https://sites.google.com/a/webpagetest.org/docs/advanced-features/webpagetest-restful-apis for additional information

## Installation

- Python pypi - https://pypi.python.org/pypi/webpagetest
- Install - `pip install webpagetest`
- Create a config - `wpt --new config.json`
- Edit the config file `config.json`
    - You will need an API key from http://www.webpagetest.org/getkey.php
    - The API key is limited to 200 page loads per day. Each run, first or repeat view counts as a page load (10 runs, first and repeat view would be 20 page loads)
- Run - `wpt --config config.json`
- Run - `wpt` for full help information


## Development

- `cp config.sample.json config.json` - Create and edit a config file.
- `make` - Installs python packages.
- `make install` - Installs current git repo as a local module.
- `make run` - Runs the package supplying a config.json argument.
