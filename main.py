import time
import database


while True:
    print('Counter value at start:')
    print(database.setting_1.value)

    print('Increase counter value by 3:')
    database.setting_1.value += 3
    database.setting_1.save()
    print(database.counter_1.value)

    print('Going to sleep for 10 seconds...')

    time.sleep(10)