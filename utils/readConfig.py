# -*- encoding : utf-8 -*-
import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="utf-8")

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value


