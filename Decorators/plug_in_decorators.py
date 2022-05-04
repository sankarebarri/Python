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