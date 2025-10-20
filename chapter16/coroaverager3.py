from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
        
    return Result(count, average)


def grouper(results, key):
    print('Grouper started for key:', key)
    while True:
        results[key] = yield from averager()
        

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None) 
        
    report(results)
    
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
            result.count, group, result.average, unit
            ))
        
data ={
    'girls;kg':
        [40.9, 38.5, 44.3, 39.2, 41.7],
        
    'girls;m':
        [1.6, 1.51, 1.75, 1.6, 1.65],
    'boys;kg':
        [39.0, 40.8, 43.2, 41.1, 39.3],
    'boys;m':
        [1.58, 1.62, 1.80, 1.75, 1.60],
}

if __name__ == '__main__':
    main(data)