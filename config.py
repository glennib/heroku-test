import configparser
import os

FILENAME = 'config.cfg'
config = configparser.ConfigParser()

def create_config_file(filename):
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




if not os.path.isfile(FILENAME):
    create_config_file(config, FILENAME)

config.read(FILENAME)


int_1 = config.getint('section1', 'int_1')
int_2 = config.getint('section2', 'int_2')

def set_int_1(n):
    config.set('section1', 'int_1', str(n))
    with open(FILENAME, 'w') as configfile:
        config.write(configfile)
    global int_1
    int_1 = n

def set_int_2(n):
    config.set('section2', 'int_2', str(n))
    with open(FILENAME, 'w') as configfile:
        config.write(configfile)
    global int_2
    int_2 = n

