import time
import database


while True:
    print('Counter value at start:')
    print(database.counter_1.Value)

    print('Increase counter value by 3:')
    database.counter_1.Value += 3
    print(database.counter_1.Value)

    print('Going to sleep for 10 seconds...')
    time.sleep(10)