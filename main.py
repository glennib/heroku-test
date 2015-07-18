import time
import environ_items

while True:
    print('Counter value at start:')
    print(environ_items.getCounter())

    print('Increase counter value by 3:')
    environ_items.setCounter(environ_items.getCounter() + 3)
    print(environ_items.getCounter())

    print('Going to sleep for 10 seconds...')
    time.sleep(10)