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
    * [Getting started with Zabbix and Telegram](#getting-started-with-zabbix-and-telegram)
    * [Requirements](#requirements)
    * [Components Description](#components-description)
  * [Installation](#installation)
  * [Configuration](#configuration)
  * [Running the Application](#running-the-application)
  * [Running the Project Automatically with Crontab](#running-the-project-automatically-with-crontab)
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

## Components Description

This project consists of the following components:

  - utils/
    - __init__.py
    - config_reader.py
    - logging.utils.py
  - zbx_bot/
    - __init__.py
    - telegram_bot.py
    - zabbix.py
- app.py
- app.log
- config.ini
- requirements.txt
- run_bot_zabbix.sh

- `utils/`: This directory contains utility modules for the project.
  - `init.py`: An empty file that marks the directory as a Python package.
  - `config_reader.py`: This module is responsible for reading the configuration file (config.ini). It uses the configparser library to parse the file and extract the required configuration parameters.
  - `logging_utils.py`: A module containing utility functions for logging.
 - `zbx_bot/`: This directory contains modules related to the Zabbix bot functionality.
   - `init.py`: An empty file that marks the directory as a Python package.
   - `telegram_bot.py`: A module that handles the Telegram bot functionality.
   - `zabbix.py`: A module that interacts with the Zabbix monitoring system.
- `app.py`: The main application file where the bot is initialized and run.
- `app.log`: A log file where application logs are stored.
- `config.ini`: A configuration file that contains settings for the application.
- `requirements.txt`: A file listing the required Python packages and their versions for the project.
- `run_bot_zabbix.sh`: A shell script used to execute the Zabbix bot, possibly with environment setup and specific commands.

# Installation

1. Clone the repository:

```shell
https://github.com/rotoapanta/botZabbixProject.git
```
   
2. Navigate to the project directory:

 ```shell
   cd repository
```

3. Ensure that you have Anaconda or Python 3.10 with the venv tool installed on your system.

Follow the instructions in the run_bot_zabbix.sh script to set up and run the project. This script takes care of environment setup, dependency installation, and execution of the Zabbix bot.

1. Create a new environment with python 3.10.

 ```shell
conda create --name bot_zabbix_env python=3.10
   ```

2. Clone the repository:

   ```bash
    git clone https://github.com/your-username/telegram-zabbix-bot.git
    ```

3. Navigate to the project directory:

   ```bash
    cd telegram-zabbix-bot`
    ```

4. Install the required Python packages:

   ```bash
    pip install -r requirements.txt
    ```
   
# Configuration

1. Open the config.ini file in the project directory.

2. Configure the Zabbix credentials:
   - Set the Zabbix URL in the url field.
   - Enter your Zabbix username in the user field.
   - Provide your Zabbix password in the password field.

3. Configure the Telegram access token:
   - Set your Telegram bot token in the token field under the [Telegram] section.

# Running the Application

1. Run the application using the following command:

    ```bash
      python app.py config.ini
    ```
2. The Telegram bot will start and listen for commands.

# Running the Project Automatically with Crontab
To automate the execution of the project using the crontab, you can follow these steps:

1. Open the crontab for editing by running the following command in the terminal:

    ```bash
      crontab -e
    ```

2. In the crontab file, add a new line with the following command to execute the project continuously:

    ```bash
      * * * * * while true; do cd /path/to/project && python app.py config.ini; sleep 1; done
    ````
Replace /path/to/project with the actual path to the project directory.

3. Save the crontab file and exit the editor.

## Environment Variables

## Environment Variables

Before running the project, make sure to set the following environment variables:

- `ZABBIX_URL`: The URL of the Zabbix instance.
- `ZABBIX_USER`: The username for accessing the Zabbix API.
- `ZABBIX_PASSWORD`: The password for accessing the Zabbix API.
- `TELEGRAM_TOKEN`: The token for accessing the Telegram Bot API.

You can either set these environment variables manually or create a `.env` file in the root directory of the project and populate it with the required values.

Example `.env` file:

## Change Log

* Revision: 1.3 - Add requeriments.txt
* Revision: 1.2 - Add app.log
* Revision: 1.1 - Code cleaned.
* Revision: 1.0 - Initial commit

## Usage

- Send `/ping` command to the bot in a Telegram chat to initiate a host search and perform a ping test.
- Follow the prompts and instructions provided by the bot to interact and retrieve information from Zabbix.

## Logging

- The application logs are stored in the app.log file in the same directory as app.py.

- You can refer to this log file to track the application's execution and any errors or exceptions that may occur.

## Feedback

If you have any feedback, please reach out to us at robertocarlos.toapanta@gmail.com

## Support

For support, email robertocarlos.toapanta@gmail.com or join our Discord channel.

## License

[GPL v2](https://www.gnu.org/licenses/gpl-2.0)

## Autors
- [@rotoapanta](https://github.com/rotoapanta)

## More Info

* [Official documentation for py-zabbix](https://py-zabbix.readthedocs.io/en/latest/)
* [GitHub py-zabbix](https://github.com/adubkov/py-zabbix)
* [Install py-zabbix 1.1.7](https://pypi.org/project/pyzabbix/)
* [Install pyserial 3.5](https://pypi.org/project/pyserial/)

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)

