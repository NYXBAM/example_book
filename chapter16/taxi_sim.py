import collections
import time


Event = collections.namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0):
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passanger')
        time = yield Event(time, ident, 'drop off passanger')
    yield Event(time, ident, 'going home')
    
_ = ''    
taxi = taxi_process(ident=13, trips=2, start_time=0)
temp_result = next(taxi)
print(temp_result)
print(taxi.send(temp_result.time + 7))
print(taxi.send(temp_result.time + 23))
print(taxi.send(temp_result.time + 5))
# Event(time=0, proc=13, action='leave garage')
# Event(time=7, proc=13, action='pick up passanger')
# Event(time=23, proc=13, action='drop off passanger')
# Event(time=5, proc=13, action='pick up passanger')

