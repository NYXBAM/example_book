import collections
import queue
import random
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

taxis = {
    0: taxi_process(ident=0, trips=2, start_time=0),
    1: taxi_process(ident=1, trips=4, start_time=5),
    2: taxi_process(ident=2, trips=6, start_time=10),
}


def compute_duration(action):
    if 'pick up' in action:
        return random.randint(5, 10) 
    elif 'drop off' in action:
        return random.randint(10, 20)  
    else:
        return 0
    
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
    
    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
            
        sim_time = 0
        
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print('taxi:', proc_id, proc_id * '', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
            
            
sim = Simulator(taxis)
sim.run(100)
# RESULT 

# taxi: 0  Event(time=0, proc=0, action='leave garage')
# taxi: 0  Event(time=0, proc=0, action='pick up passanger')
# taxi: 1  Event(time=5, proc=1, action='leave garage')
# taxi: 1  Event(time=5, proc=1, action='pick up passanger')
# taxi: 0  Event(time=8, proc=0, action='drop off passanger')
# taxi: 1  Event(time=10, proc=1, action='drop off passanger')
# taxi: 2  Event(time=10, proc=2, action='leave garage')
# taxi: 2  Event(time=10, proc=2, action='pick up passanger')
# taxi: 2  Event(time=15, proc=2, action='drop off passanger')
# taxi: 1  Event(time=22, proc=1, action='pick up passanger')
# taxi: 0  Event(time=26, proc=0, action='pick up passanger')
# taxi: 2  Event(time=28, proc=2, action='pick up passanger')
# taxi: 1  Event(time=31, proc=1, action='drop off passanger')
# taxi: 0  Event(time=34, proc=0, action='drop off passanger')
# taxi: 2  Event(time=38, proc=2, action='drop off passanger')
# taxi: 1  Event(time=41, proc=1, action='pick up passanger')
# taxi: 1  Event(time=47, proc=1, action='drop off passanger')
# taxi: 2  Event(time=48, proc=2, action='pick up passanger')
# taxi: 0  Event(time=52, proc=0, action='going home')
# taxi: 2  Event(time=53, proc=2, action='drop off passanger')
# taxi: 1  Event(time=61, proc=1, action='pick up passanger')
# taxi: 2  Event(time=64, proc=2, action='pick up passanger')
# taxi: 1  Event(time=69, proc=1, action='drop off passanger')
# taxi: 2  Event(time=70, proc=2, action='drop off passanger')
# taxi: 1  Event(time=81, proc=1, action='going home')
# taxi: 2  Event(time=83, proc=2, action='pick up passanger')
# taxi: 2  Event(time=91, proc=2, action='drop off passanger')
# taxi: 2  Event(time=103, proc=2, action='pick up passanger')
# *** end of simulation time: 1 events pending ***