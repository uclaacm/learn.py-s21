# learn<span>.</span>py Session 5: Introduction to Python

**Date**: April 14, 2021

**Location**: Zoom

**Teachers**: [Einar Balan](https://github.com/EinarBalan), [Nareh Agazaryan](https://github.com/nareha)

## Resources

- [Slides](https://docs.google.com/presentation/d/1ATyV4KLqf9qmk8kfnXwJpChtq_fwGhTMVzowa_NdCnU/edit?usp=sharing)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- TBD

### Lambdas
In Python, functions are known as first class objects meaning they can be assigned to variables and passed as arguments to other functions. 

For example the following code is valid:
```python
def f(x):
    return x **	2

g = f

print(g(5)) # prints 25
```

as is 

```python
def transform_by(fun, x):
    return fun(x)

def some_func(i):
    return i ** i

transform_by(some_func, 3)
```

### Motivation for Lambdas

Sometimes it becomes convenient to create anonymous functions (i.e small functions that don't have a name) and pass those around instead of doing the whole declaration. To showcase this, let me introduce the `map` function.

`map` takes as input a function and some iterable object. It returns a list where each item in the iterable object has been given as input to the function and the return value has been placed in the list. This can be quite confusing so let's take a look at an example.

```python
def get_input(a):
    return input(f"{a}: ")

# creates a list of specified size based on user input
def get_list(size):
    return list(map(get_input, range(1, size + 1)))

print(get_list(5)) #get a list with 5 values
```

> A Couple Notes:
> - in python 3, `map` returns a map object (which is why we cast it to list)
> - as the range is iterated over, its value is provided as an argument to the get_input function
> - notice how we never call the get_input function ourselves, it's called by the map function

This is a case where using an anonymous function could be very convenient. The syntax for a lambda expression is as follows:

```python
lambda i, j: i + j # a lambda that takes in two value and returns sum
```

> Note: An important limitation of lambdas to keep in mind is that they are restricted to single expressions for their return values. This means they can only be used for small functions as shown above!

Let's update our example from before to use a lambda.

```python
def get_list(size):
    return list(map(lambda a : input(f"{a}: "), range(1, size + 1))

print(get_list(5))
```

Woah! Very concise. As you proceed with Python, you'll begin to appreciate just how much you can do in a single line, it's honestly kinda crazy (you can even go a bit too far, so take care in making sure your code is readable too!)

Next time we'll go over a much cleaner way of handling behaviour like this (called list comprehension), so don't worry if this is confusing to you.