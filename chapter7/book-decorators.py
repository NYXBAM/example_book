def deco(func):
    def inner():
        print('running inner()')
    return inner
    
@deco
def target():
    print('running target()')

target()
# running inner()

###### registration.py ####### 

registry = []

def register(func):
    print(f'running register{func}')
    registry.append(func)
    return func

@register 
def f1():
    print('running f1()')

@register 
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()