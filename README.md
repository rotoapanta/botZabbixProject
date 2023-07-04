# <p align="center">Zabbix API with Telegram bot

<p align="center">This project consists of a Telegram bot that integrates with Zabbix to perform host searches and execute ping commands.</p>

##

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
[![GitHub issues](https://img.shields.io/github/issues/rotoapanta/botZabbixPackage)](https://github.com/rotoapanta/botZabbixPackage/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/botZabbixPackage)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/botZabbixPackage)
![GitHub commit merge status](https://img.shields.io/github/commit-status/rotoapanta/botZabbixPackage/master/d8b7bfe)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/gpl-2.0)
![Discord](https://img.shields.io/discord/996422496842694726)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/Gs9b3HFd)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/botZabbixPackage?style=social)

# Contents

  * [Getting started](#getting-started)
    * [Getting started with Tiltmeter and Zabbix](#getting-started-with-tiltmeter-and-zabbix)
    * [Requirements](#requirements)
    * [Components Description](#components-description)
    * [Power Supply Options](#power-supply-options)
    * [Pin Layout](#pin-layout)
  * [Instructions](#instructions)
  * [Environment Variables](#environment-variables)
  * [Change Log](#change-log)
  * [Running Tests](#running-tests)
  * [Usage/Examples](#usage-examples)
  * [Feedback](#feedback)
  * [Support](#support)
  * [License](#license)
  * [Autors](#autors)
  * [More Info](#more-info)
  * [Links](#links)

# Getting started

## Getting started with Zabbix and Telegram

Welcome to the project! This guide will help you get started with setting up and running the application.
Introduction

The project is a Python-based application designed to perform certain tasks using the Zabbix monitoring system and integrate with the Telegram messaging platform. It provides functionalities such as searching and pinging hosts through a Telegram bot.

Let’s get started!
 
## Requirements

  * Python 3.10 or higher installed on your system.
  * `python-telegram-bot` library version 13.1 installed.
  * Access to a Zabbix server with appropriate credentials. 
  * A Telegram bot token obtained from the BotFather.
  * `pyzabbix` library installed to interact with the Zabbix API..
  * Computer running Anaconda on Windows, Linux or macOS (in this case macOS is used).
  * [Install py-zabbix 1.1.7](https://pypi.org/project/pyzabbix/)
  * [Install pyserial 3.5](https://pypi.org/project/pyserial/)

## Components Description

This project consists of the following components:

- app.py
- app.log
- config.ini
- config_reader.py
- logging.ini
  - zbx_bot/
    -__init__.py
    - telegram_bot.py
    - zabbix.py
  - requirements.txt
  - README.md

`app.py`: This is the main entry point of the application. It initializes the logging configuration, reads the configuration file, connects to the Zabbix server, and starts the Telegram bot.

`app.log`: This file is the application's log file. It will store the log messages generated during the program's execution.

`config.ini`: This configuration file contains the necessary parameters for the application, such as the Zabbix URL, username, password, and the Telegram bot token. It is used by the config_reader.py module to retrieve the configuration values.

`config_reader.py`: This module is responsible for reading the configuration file (config.ini). It uses the configparser library to parse the file and extract the required configuration parameters.

`logging.ini`: This configuration file contains the logging settings for the application. It specifies the log format, log levels, and log file location.

    `zbx_bot`: This folder contains the modules related to the Zabbix bot functionality.
        `init.py`: This file is required to mark the "zbx_bot" folder as a Python package.
        `telegram_bot.py`: This module implements the Telegram bot functionality.
        `zabbix.py`: This module provides functions to interact with the Zabbix API.

    `requirements.txt`: This file lists all the required Python dependencies for the project. It can be used with the pip command to install the necessary packages.

    README.md: This file provides an overview of the project, including installation instructions, usage guidelines, troubleshooting information, and licensing details.



- `app.py`: The main file that starts the Telegram bot application and handles the integration with Zabbix.
- `config.ini`: The configuration file that contains the Zabbix credentials and Telegram access token.
- `config_reader.py`: Module to read the configuration from the `config.ini` file.
- `zbx_bot/`: Directory that contains the files related to the Telegram bot and Zabbix integration.
  - `zabbix.py`: Module that connects to the Zabbix API and performs operations related to hosts.
  - `telegram_bot.py`: Module that implements the Telegram bot and handles commands and responses.
- `README.md`: This file provides information about the project and its structure.

## Configuration

Before running the application, you need to configure the Zabbix credentials and the Telegram access token in the `config.ini` file. Make sure to provide the correct values in the `[Zabbix]` and `[Telegram]` sections.

## Execution

To run the application, use the following command:

## Power Supply Options

There is a way to provide power to the tiltmeter:

  * Connect the 12V DC adapter to the tiltmeter jack.

**_It is recommended to verify the polarity of the jack (- ring and + center)._**

## Pin Layout
![Pinout-tiltmeter.png](https://github.com/rotoapanta/digital_tiltmeter_zabbix/assets/16738424/a8703cc0-d72a-41af-a456-22ba8f73b432)


# Instructions

1. Install Anaconda.

2. Create a new environment with python 3.10.

   ```bash
   conda create --name bot_zabbix_env python=3.10
   ```

3. Install pythonping library.

   ```bash
   pip install pythonping
   ```

4. Install pythonping library.

   ```bash
   pip install python-telegram-bot==13.1
   ```
   
5. Install py-zabbix library.

   ```bash
   pip install py-zabbix
   ```
5. Check tiltmeter data frame with a hyperterminal.

   ```bash
   $-9162.82, 9162.82,23.88,N7624
   ```
6. Insert into the server's crontab to run periodically.
   ```bash
   chmod +x run_tiltmeter_zabbix.sh
   ```
   
   ```bash
   crontab -e
   ```
   
   ```bash
   * * * * * /home/rotoapanta/script/run_tiltmeter_zabbix.sh
   ```
## Environment Variables

To run this project, you will need to add the IP address of the Zabbix server to the `configuration.ini file.

`[zabbix_server]`

`ip=XXX.XXX.XXX.XXX`

`port=10051`

## Change Log

* Revision: 1.1 - Code cleaned.
* Revision: 1.0 - Initial commit

## Running Tests

To run tests, run the following command

```python
  ampy --port /dev/ttyUSB0 run main.py
```

## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Feedback

If you have any feedback, please reach out to us at robertocarlos.toapanta@gmail.com

## Support

For support, email robertocarlos.toapanta@gmail.com or join our Discord channel.

## License

[GPL v2](https://www.gnu.org/licenses/gpl-2.0)

## Autors
- [@rotoapanta](https://github.com/rotoapanta)

## More Info

* [Zabbix Sender](https://www.zabbix.com/documentation/4.0/en/manual/concepts/sender)
* [Zabbix Handy Tips: Collect and send custom metrics with Zabbix sender](https://www.youtube.com/watch?v=AWJgEHLOHe0)
* [Official documentation for py-zabbix](https://py-zabbix.readthedocs.io/en/latest/)
* [GitHub py-zabbix](https://github.com/adubkov/py-zabbix)

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)

