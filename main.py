import time
import config


while True:
    print('Counter value at start:')
    print(config.int_1)

    print('Increase counter value by 3:')
    config.set_int_1(config.int1 + 3)
    print(config.int_1)

    print('Going to sleep for 10 seconds...')
    time.sleep(10)