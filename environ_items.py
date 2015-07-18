import os

def getCounter():
    str_counter = os.environ['HT_COUNTER']
    return int(str_counter)

def setCounter(n):
    new_value = str(n)
    os.putenv('HT_COUNTER', new_value)