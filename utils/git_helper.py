'''
Module delegated to handling git logic
'''

# System/Third-Party modules
import logging
import re
import sys

# Custom modules
from utils.setup_wrapper import SETUP
from utils.github_wrapper import GITHUB

LOGGER = logging.getLogger()

def update_ssh_config():
    '''
    Update config file in .ssh directory
    '''
    home_dir = SETUP.dir['home']
    ssh_config = f'{home_dir}/.ssh/config'

    config = None

    with open(ssh_config) as text_file:
        config = [line for line in text_file.readlines()]

    content = ''.join(config)

    pattern = re.compile(r'IdentityFile .*')
    key_match = re.search(pattern, content)

    identity_val = f'IdentityFile {home_dir}/.ssh/id_rsa'

    if not key_match:
        with open(ssh_config, 'a') as text_file:
            text_file.write(identity_val)
        LOGGER.info('IdentityFile key value appended to ssh config file')
        return

    start, end = key_match.span()
    current_config = content[start:end]

    if current_config == identity_val:
        LOGGER.info('IdentityFile key value already configured in ssh config file')
        return

    content = content[:start] + identity_val + content[end:]
    with open(ssh_config, 'w') as text_file:
        text_file.write(content)

    LOGGER.info('IdentityFile key value updated in ssh config file')

def github_public_key_exists(current_key: str, public_keys: list) -> bool:
    '''
    Check if current public key passed in exists on github
    '''
    pattern = re.compile(re.escape(current_key))

    for key in public_keys:
        if re.match(pattern, key['key']):
            return True
    return False

def delete_github_pub_key(current_key: str, public_keys: list):
    '''
    Removes current public key in host machine stored on github
    '''
    pattern = re.compile(re.escape(current_key))

    for key in public_keys:
        if re.match(pattern, key['key']):
            GITHUB.delete_public_key(key['id'])
            LOGGER.info('Provided public key now deleted from github account')
            return

def remove_ssh_config():
    '''
    Removes the identity value of the rsa private key from the ssh config file
    '''
    home_dir = SETUP.dir['home']
    ssh_config = f'{home_dir}/.ssh/config'

    config = None

    with open(ssh_config) as text_file:
        config = [line for line in text_file.readlines()]

    content = ''.join(config)

    pattern = re.compile(r'IdentityFile .*')
    key_match = re.search(pattern, content)

    if not key_match:
        LOGGER.info('IdentityFile key value already deleted from ssh config file')
        return

    start, end = key_match.span()

    content = content[:start] + content[end:]
    with open(ssh_config, 'w') as text_file:
        text_file.write(content)

    LOGGER.info('IdentityFile key value is now removed from ssh config file')

def remove_ssh_github_host():
    '''
    Remove host key & agent from known_host file in .ssh directory
    '''
    home_dir = SETUP.dir['home']
    known_hosts = f'{home_dir}/.ssh/config'

    config = None
    with open(known_hosts) as text_file:
        config = [line for line in text_file.readlines()]

    content = ''.join(config)

    pattern = re.compile(r'github.* ssh-rsa .*')
    key_match = re.search(pattern, content)

    if not key_match:
        LOGGER.info('Github host value already deleted from known_host file')
        return

    start, end = key_match.span()

    content = content[:start] + content[end:]
    with open(known_hosts, 'w') as text_file:
        text_file.write(content)

    LOGGER.info('Github host value is now removed from known_host file')
