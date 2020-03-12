import appdirs
import os
from configparser import ConfigParser

CONFIG_DIR = appdirs.user_config_dir('translate_it')


class Config:

    def __init__(self):
        self.path = os.path.join(CONFIG_DIR, 'config.ini')
        self.config = ConfigParser()

        if not os.path.isfile(self.path):
            self.create()
            self.write()
        else:
            self.config.read(self.path)

    def get(self, section, option):
        try:
            value = self.config.get(section, option)
        except Exception:
            value = None
        return value

    def create(self):
        os.makedirs(CONFIG_DIR)

        self.config.add_section('auth')
        self.config.set('auth', 'user', '')
        self.config.set('auth', 'password', '')
        self.config.add_section('dictionaries')
        self.config.set('dictionaries', 'youdao', 'True')

    def write(self):
        with open(self.path, 'w+') as f:
            self.config.write(f)

    def update(self, section, option, value):
        self.config.set(section, option, value)
        self.write()
