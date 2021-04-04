# learn<span>.</span>py Session 5: Introduction to Python

**Date**: April 7, 2021

**Location**: Zoom

**Teachers**: [Nareh Agazaryan](https://github.com/nareha), [Einar Balan](https://github.com/EinarBalan)

## Resources

- [Slides](https://docs.google.com/presentation/d/1ATyV4KLqf9qmk8kfnXwJpChtq_fwGhTMVzowa_NdCnU/edit?usp=sharing)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- TBD
- Interpreted vs Compiled Languages
- Variables
    - weak vs strong typing
    - type inference
    - type casting
- I/O
    - print
    - input
    - format strings
- [Conditionals](#conditionals)
    - booleans, operators
    - white space
- [Loops](#loops)
    - while
    - for
        - containers
        - range
- [Functions](#functions)
    - parameters by value/reference
    - None
    - documentation
    - default arguments
    - keyword vs positional arguments
    - arbitrary argument lists
    - lambdas
    - map

## Conditionals
If you've seen conditionals in other languages, conditionals in Python won't surprise you. Keeping with the theme of the language, though, there are a couple differences designed to make your life easier!

Here's what a typical conditional statement looks like in Python:
```python
if anyone_can_cook:
    print("r a t")
```

You can probably already spot a couple differences compared to other languages, but let's go through them one at a time:
- parentheses are optional
- no curly brackets (colon instead)
- white space matters!
    - official documentation recommends using 4 spaces instead of tabs

> Note: If I add more statements below the conditional, they only belong to that conditional if they are at the required indentation level.

i.e. The following two blocks will be treated differently.
```python
if anyone_can_cook:
    print("r a t")
    print("I don't like food,")

    print("I love it.")
```
&
```python
if anyone_can_cook:
    print("r a t")
    print("I don't like food,")

print("I love it.")
```
-----

### Quick Aside on Boolean Conditions
The statement following the `if` keyword is evaluated in exactly the same way as in other languages. If it evaluates to `True` (notice the capitalization), then the body of the conditional will be executed. If `False`, then it won't be. In Python, non-empty collections and numeric values that are not 0 are evaluated as True. All other values are False. See the table below for reference.

| | Truthy | Falsey |
|-|--------|--------|
| True |   x     |      |
| False |        |   x   |
| 1 |     x   |      |
| -12123 |    x    |      |
| 0 |        |   x   |
| [ ] |       |   x   |
| [1, 2, 3] |   x    |      |
| "" |       |  x    |
| "ratatata" |   x    |      |

<br>
I'll gloss over comparison operators, but know that they work exactly as you would expect, with the exception of logical and being written as "and" and logical or being written as "or".

------

There are also else statements!

```python
if anyone_can_cook:
    print("r a t")
else:
    print("m a n")
```

And they work in exactly the same way. How about else if's? In other languages you might be familiar with such as C++, there is no designated else if key word. Instead, the language takes advantage of the fact that white space is ignored to create easy to read statements, like so:

```C++
if (anyoneCanCook) {
    std::cout << "r a t" << std::endl;
}
else if (notEveryoneButRatsCan) {
    std::cout << "r a t !!" << std::endl;  
}
else {
    std::cout << "m a n" << std::endl;
}
```

Unfortunately, this won't work quite as nicely in Python due to the strict enforcement of white space. Here is a direct translation to Python:

```python
if anyone_can_cook:
    print("r a t")
else:
    if not_everyone_but_rats_can: 
            print("r a t !!")
    else: 
        print("m a n")
```

Luckily, we can do better thanks to a new keyword that Python introduces: `elif`. Here's what the above code would look like when using `elif`.

```python
if anyone_can_cook:
    print("r a t")
elif not_everyone_but_rats_can: 
    print("r a t !!")
else: 
    print("m a n")
```

Much cleaner!

> Note: As of Python 3.9.1, there's no switch statement. Keep your eye out though because this will be changing soon (match statements)!

## Loops

### while
Just like conditionals, while loops behave more or less the same as in other languages:

```python
while num_ingredients:
    num_ingredients -= 1
    print("lost ingredient")
```
> Note: there are no increment/decrement operators in Python.

### for
For loops, on the other hand, take quite a different approach than in languages like C++. Here's a look at the syntax: 

```python
for word in ["anyone", "can", "cook"]:
    print(word)
```
As you can tell, for loops in Python read a lot more like actual English, which, as we progress, you'll notice is a running theme of the language. Python's for statement will iterate over the items of a sequence/collection (which we'll define later on but for now it's sufficient to know they're simply container types) in the order that they appear. 

This decision to limit for loops to iteration makes some things a lot more convenient and some things less convenient. For example, how can we easily iterate through a range of numbers? Well, you could just use a while loop. If you wanted to use a for loop, however, you would need to use `range()`.

```python
for num in range(10):
    print(num)
```

Just like a list, range is a sequence type that allows you to iterate over some specified range of numbers. 

`range` has the following prototype, as described in the Python documentation,
```python
range(stop)
range(start, stop[, step])
```

### Looping Techniques
Python lets you do a LOT of cool things in relation to looping that will result in extremely clean, elegant code. Unfortunately, our time is limited today so we'll have to defer it to next time. I promise you don't want to miss it though! You can't have clean, elegant code without some level of abstraction, though, and that's where functions come in!

## Functions
Alright, now we're getting to some *fun* stuff. Get it? Fun?? Haha okay bye

But seriously functions in Python are both very simple and very powerful, so let's take a look! 

The basic syntax for a function is as follows:
```python
def f(x, y):
    # do something

f(42, ["hello", "there"]) #ways to call f
f(y="hey", x=99)
f("hey", y=99)
```

where x and y can be any type. The default return value if not specified is a value called `None` which is analagous to `null` in other languages.

An important note to understand is that immutable types (i.e. integers, strings, floats, etc) are passed by value while mutable types (lists, dictionaries, etc) are passed by reference. This means that changing the local value of an immutable argument will not change its value beyond the scope of the function. 

> Note: There are no pointers in Python! You're just going to have to remember which data types are mutable and which are immutable. 

### Fun with Arguments
The main way Python functions differ from functions in lower level languages is in the immense flexibility of the arguments. As an example, let's take a look at the print function's documentation.

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

Woah! That looks a lot more complicated than expected. Let's break it down.

1. The first argument `*objects`, allows the user of the function to enter an arbitrary number of arguments into the function. In the case of `print()`, each of these arguments is printed in order with the `sep` string between them.

2. The remaining 4 arguments have default values provided to them. As a result, they're optional when calling the function.

This flexibility allows the designer of a library to hide away much of the complexity of the function! 

Let's design a function called `concat()`, which will take an arbitrary number of strings and return a single string with them all joined together. Let's also allow the user of the function to speficy a string to separate each string.

```python
def concat(*args, sep=""):
    return sep.join(args)
```

See how simple that was! Granted it was because there already is a function that did most of the work for us, but still! Now we can call our `concat()` function as follows:

```python
concat("anton", "ego", "is", "a", sep=" ") # returns "anton ego is a "
concat("r", "a", "t", "a", "t") # returns "ratat"
concat() # returns ""
```

> Note: the `sep` argument is called a keyword-only argument because it can only be specified in a function call by its keyword. All arugments following an arbitrary list argument are keyword-only argmuments. Otherwise, how would Python know which argument the parameter belongs to?

You can also allow for an arbitrary number of keyword arguments (represented as a dictionary) using **.

```python
def keywords(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

keywords(key="lock", dir="ection", lo="down")
"""
prints:
    key: lock
    dir: ection
    lo: down
"""
```

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

Sometimes it becomes convenient create anonymous functions (i.e small functions that don't have a name) and pass those around instead of doing the whole declaration. To showcase this, let me introduce the `map` function.

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
lambda i: i * 2 # a lambda that takes in a value and returns twice the value
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

## Wrapup
Alright, that was a ton of information! I encourage you to go back and reread sections that were confusing, and if you still don't get it feel free to reach out! We're always happy to help on the ACM discord :)

