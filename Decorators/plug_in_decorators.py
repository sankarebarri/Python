##########################################################################################


def logged(func):
    '''Prints out the name of a function with the arguments passed into it'''
    def wrapper_logged(*args, **kwargs):
        print(f"you called {func.__name__}{args}")
        print(f'it returned {func(*args)}')
        return func(*args)
        
    return wrapper_logged


@logged
def bizzare_function(*args):
    return 3 + len(args)

print(bizzare_function(4,4,4))
##########################################################################################



##########################################################################################

import random
PLUGINS = dict()
def register(func):
    '''Register a function as a plug-in'''
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name!r}"


print(say_hello('Ibrahim'))
print(PLUGINS)

@register
def be_awesome(name):
    return f"Yo, {name!r} we're awesomest together"

print(be_awesome('Sankare'))
print(PLUGINS)

def greeter_name(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(greeter_name('Barri'))
##########################################################################################
