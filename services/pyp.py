"""
Module delegated to handling pyp logic
"""

# Native Modules
import logging
import sys
from itertools import tee
from subprocess import Popen, call, check_output, PIPE, DEVNULL

# Third Party Modules
import pexpect

# Custom Modules
from singletons.setup import SetupSingleton
from utils.general import consume, partition, format_ansi_string, \
    format_success_message
from utils.unicode import ForeGroundColor

SETUP: SetupSingleton = SetupSingleton.get_instance()
LOGGER = logging.getLogger()


def process_file() -> list:
    """
    Parses the config file generated from 'pip freeze > pip_leaves' located in
    the config directory

    The content of the file will look like this (excluding the (-|+) border):
    +-------------------------------+
    | Package             Version   |
    | ------------------- ----------|
    | autopep8            1.5       |
    | ...                           |
    | ...                           |
    +-------------------------------+
    We need to parse from the third line onwards & install the latest by
    reading the first column only of each line
    """
    return
    # with open(SETUP.pyp_config_file) as text_file:


def install_packages():
    """
    Downloads & installs every package config if it's valid
    """
    return


# def install_powerline_at_user():
#     """
#     Installs the powerline tool at the user level of the system
#     """
#     command = 'pip3 install --user powerline-status'
#     with Popen(command.split(), stdout=PIPE, stderr=PIPE) as process:
#         out, err = process.communicate()

#         if err:
#             LOGGER.error(err.decode('utf-8'))
#             LOGGER.error(format_ansi_string('Failed to install powerline from '
#                                             'pip3', ForeGroundColor.RED))
#             sys.exit()
#         else:
#             LOGGER.debug(out.decode('utf-8'))
#             LOGGER.info(format_ansi_string('Powerline now installed from pip3 '
#                                            'at the user level',
#                                            ForeGroundColor.GREEN))