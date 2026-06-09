from configparser import ConfigParser
from logging import config

def get_config(category,key):
    config = ConfigParser()
    config.read("./config.ini")
    return config.get(category,key)