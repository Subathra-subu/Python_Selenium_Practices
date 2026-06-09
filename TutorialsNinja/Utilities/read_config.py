from configparser import ConfigParser
from logging import config

def get_data(category,key):
    config = ConfigParser()
    config.read("TestData/config.ini")
    return config.get(category,key)