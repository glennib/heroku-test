from peewee import *
import urllib.parse
import os
from pprint import pprint

url = urllib.parse.urlparse(os.getenv('CLEARDB_DATABASE_URL'))
dbname = url.path

pprint(vars(url))

db = MySQLDatabase(dbname, host=url.hostname, user=url.username, passwd=url.password)


class Setting(Model):
    name = CharField(index=True, unique=True)
    value = FloatField()

    class Meta:
        database = db


db.connect()


# Create setting table if it doesn't exist already
if 'setting' not in db.get_tables():
    db.create_table(Setting)
    print('Setting table not found. Created.')
else:
    print('Setting table exists. Do nothing.')

# Delete if true
if True:
    print('Deleting all entries in table Setting')
    for setting in Setting.select():
        setting.delete_instance()

# Define function for safely creating setting
def create_safe_setting(name, value):
    setting = Setting()
    try:
        print('Trying to find ' + name + '...')
        setting = Setting.get(Setting.name == name)
        print('Found it! Assigning...')
    except DoesNotExist:
        print(name + ' not found. Creating...')
        setting = Setting.create(name=name, value=value)
        setting.save()
    return setting

# Create setting_1 if it doesn't exist already
setting_1 = create_safe_setting('setting_1', 0)
setting_2 = create_safe_setting('setting_2', 12.3)

print()
print(setting_1.name, ':', setting_1.value)
print(setting_2.name, ':', setting_2.value)
