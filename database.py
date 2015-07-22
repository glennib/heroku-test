import peewee
from peewee import *

import urllib.parse
import os

url = urllib.parse.urlparse(os.getenv('CLEARDB_DATABASE_URL'))
dbname = url.path
db = MySQLDatabase(dbname, host=url.hostname, user = url.username, passwd=url.password)

class BaseModel(Model):
    """A base model for all other models"""
    class Meta:
        database = db

class Setting(BaseModel):
    Name = CharField(index=True, unique=True)
    Value = FloatField()

counter_1 = Setting()
counter_1.Name = 'Counter 1'
counter_1.Value = 0


