import configparser
import os

FILENAME = 'config.cfg'

def create_config_file(config, filename):
    try:
        config.add_section('section1')
    except configparser.DuplicateSectionError:
        print('DuplicateSectionError')

    try:
        config.add_section('section2')
    except configparser.DuplicateSectionError:
        print('DuplicateSectionError')

    config.set('section1', 'int_1', '15')
    config.set('section2', 'int_2', '30')

    with open(filename, 'w+') as configfile:
        config.write(configfile)


config = configparser.ConfigParser()

if not os.path.isfile(FILENAME):
    config.create_config_file(config, FILENAME)

