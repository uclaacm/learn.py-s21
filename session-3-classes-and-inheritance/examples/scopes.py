# scopes.py

### Demo that less specific cannot access more specific
less_specific = 5

def foo():
    more_specific = 2
    print('Inside foo:', less_specific)

foo()
# print(more_specific) will not work (accessing local scope variable outside of local scope)


### Nested function example
def a():
    def b():
        print('hello from nested function!')
    print('hello from outer function!')
    b()
a()
# Output will be: 
# hello from outer function!
# hello from nested function!



### Demo including non-local scope
# global scope
global_var = 'hello from global scope'

def regular_func():
    # non-local scope of nested_func, local scope of regular_func
    non_local_var = 'hello from non-local scope'
    def nested_func():
        # local scope of nested_func
        local_var = 'hello from local scope'
        print(global_var)
        print(non_local_var)
        print(local_var)
    nested_func()

# regular_func calls nested_func, so everything will be outputted
regular_func()
# print(local_var), print(non_local_var), or trying to call nested_func() will not work,
#   as we are outside of the scope that contains them