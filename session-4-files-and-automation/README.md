# learn<span>.</span>py Session 4: File I/O and Automation

**Date**: April 28, 2021

**Location**: Zoom

**Teachers**: [Jody Lin](https://github.com/jodymlin), [Eric Yang](https://github.com/eric8yang)

## Resources

- [Slides](https://docs.google.com/presentation/d/1JKIXgOLKNuJj7zGxKSG4leX-1PoU2lQDoriBueyQdfY/edit?usp=sharing)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- [Modules](#modules)
- [Exceptions and Handling](#exceptions)
- [File I/O](#File-I/O)
- [Time/Scheduling](#time)
- [Twilio text bot demo](#twilio-text-bot-demo)


> Note: This workshop series is designed with the assumption that attendees have taken CS31/PIC10A, or any of its equivalents. While we will go through the basics of Python, we do not explain all the details and fundamentals. Rather, we are showing how to what you have previously done, but within Python.

## Modules
Python modules allow programmers to organize their code into
separate files. If your program is really long, you want to
break apart your program into files, ~~or you are stealing 
your friend's code~~, this can be very easily done. 

Modules work like this:
Suppose we have 2 files as shown below: 
```py
# cool_module.py - really cool code
print('beep boop')
print('eric is cool')

def boop():
  print('boop boop')
```
```py
# main.py - file i want to import module into
import cool_module
cool_module.boop()
```

`cool_module.py` is just a regular python file with some code
in it. From here we will be calling this python file a _module_.

`main.py` is another regular python file that we will be
running. We want to import all of our modules here. 

To import, we simply import the name of our file `cool_module`.
Note that we drop the `.py` extension at the end. To run
the function from `cool_module`, we use the format:
```py
name_of_module.function_from_module()
```

When we execute `main.py` via the command `python3 main.py` in
the terminal, the output will be as follows:
```
beep boop
eric is cool
boop boop
```

Let's take a look at what happened:

When we import a module at the top of our file, python will 
execute all the statements in that module _once_. Any variables,
functions, and lines of code will be executed, thus we see
that `cool_module.py`'s initial 2 print statements get printed
_once_. No matter how many times we use other functions or 
classes from `cool_module.py`, those first print statements
will only execute once. 

Thus as expected, `beep boop` prints, then `eric is cool` prints,
then `boop boop`, which was printed by the call 
`cool_module.boop()`, prints. 


### Other Ways to Import
There are a few ways to import modules in python. Let's
use this short file as our module: 
```py
 # cool_module.py - really cool code
def boop():
  print('boop boop')

def yeet():
  print('yote')
```
This module can be imported in the following ways:

1. Directly import module
```py
import cool_module
cool_module.boop()
```
Just as we mentioned, to use the functions within the file,
follow the format `module_name.function_from_module()`.

2. Import a specific function/class
```py
from cool_module import boop, yeet
boop()
yeet()
```
Using the syntax `from <module_name> import <class or function>`
we can import specific functions and/or classes. Functions
or classes imported this way do not need to be accessed
via the dot operator (.) after the module name. They can
directly be called like a global function. 

3. Import and rename module
```py
import cool_module as cm
cm.boop()
```
Using the `as` keyword allows our module to be renamed to
something else. This is often used when it becomes
tedius to type out a long module name over and over, but we
still want to have a clear indication of which module
our functions come from. 

4. (Not recommended) Import entire module
```py
from cool_module import *
boop()
yeet()
```
> tl;dr This imports everything, but is not recommended.

Using the `*` operator, we import _everything_ from the 
module. This saves us the time from writing out each 
function/class we want to import at the top of the file. 
**However**, this method is generally **not recommended**.
This is because we may inadvertently import a _very large_ file
when we only intended on using 1 or 2 functions. This can
hurt performance in our program since we'll load in a lot
of code that won't ever get used. Another reason this is
not recommended is that this code can quickly clutter up
our existing file code. A function imported here may
overwrite a function with the same name in the currently file
without use realizing it. 

### Importing Multiple Modules

Importing multiple modules is as easy as adding more import
lines like this:
```py
import chloe_ting_workout
import jodys_moms_workout
```

Let's assume these modules look like this:
```py
# chloe_ting_workout.py
def push_up():
  print('Chloe Ting does push ups')
```
```py
# jodys_moms_workout
def push_up():
  print("Jody's Mom does push ups")
```
Calling functions from each is easy to differentiate since
we specify the module.
```py
# main.py
chloe_ting_workout.push_up()
jodys_moms_workout.push_up()
```
The output is pretty straightforward and would look like this:
```
Chloe Ting does push ups
Jody's Mom does push ups
```
But what if we did something like this?
```py
# main.py
from chloe_ting_workout import push_up
from jodys_moms_workout import push_up

push_up() # which one will we call???
```
Which push_up function gets called here? **Answer:** The
second one (from `jodys_moms_workout`) gets called.

This is because when we import `push_up` the second time from
`jodys_moms_workout`, it overwrites the first `push_up` we
imported from the `chloe_ting_workout` module. 

If we had first imported `push_up` from `jodys_moms_workout`
and then imported `push_up` from `chloe_ting_workout`, then
we'd call the `chloe_ting_workout` version of `push_up`. 

This is yet another example of why programmers tend to
not directly import functions from modules since they
may accidentally overwrite another one. 

## Exceptions
Exceptions are errors that are detected during the execution
of code. These will stop running the program and often
print an error message in the console.

Here are some common exceptions:
1. `ZeroDivisionError` - Dividing by 0
1. `NameError` - Referencing a variable that doesn't exist
1. `IndexError` - Accessing an index out of bounds in a 
sequence object
1. `KeyError` - Accessing a key that doesn't exist in a
 dictionary

There are [many more](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) that also exist. 

As mentioned before, these will raise an Exception and stop
the execution of your code. Often times though, we don't
want our code to crash. In this case, we'll have to _handle_
these Exceptions.

### Exception Handling
Exception handling gives us a way to keep our programs running
even when exceptions occur. So when an exception occurs, we'll
run a specific block of code, and then continue with the 
program. 

We do this in the form of a **try-except-finally** block. It
looks like this:
```py
try:
  code_that_could_raise_an_exception()
except Exception:
  # only execute if Exception is raised
  print('exception caught!')
finally: 
  # this code executes regardless if exception is raised
  print('this code executes regardless if exception was thrown')
```

In the `try` block, we put code that _might_ throw an 
exception.

In the `except` block, we will run this code
_only if an Exception is raised_. Otherwise we'll skip
this code and move on to the next block. 

In the `finally` block, we will run this code regardless
if an exception was raised or not. This block is optional
and doesn't need to be included. In other words, it
is valid to write only a `try-except` block without
a `finally` block. 

With this code, we no longer have to worry about our code
crashing! This block will handle the exception and then
continue. 

### Catching Different Types of Exceptions
In our `try-except-finally` block in the previous section 
we wrote `except Exception`. `Exception` is a type of 
exception that encompasses all exceptions. Thus this
block will catch _all_ exceptions. However, we can 
handle different types of exceptions by specifying
which exceptions to handle. 

Here's an example:
```py
try:
  1 / 0 
except ZeroDivisionError:
  print('oh no we divided by 0')
except Exception:
  print('exception caught!')
finally: 
  print('this code executes regardless if exception was thrown')
```
When executed, the output of this code is:
```
oh no we divided by 0
this code executes regardless if exception was thrown
```

Since we divide by 0 in the `try` block, we'll jump
to the code in the `except ZeroDivisionError` block. 
After this we'll jump to the `finally` block and execute
the remaining code. 

### Raising Exceptions
Often times we'll want to raise our own exceptions. Perhaps
we are writing a module and wish to raise an exception
for programs that use our module wrong. Python gives us
a way to raise exceptions. 

This syntax is:
```py
raise NameOfExceptionHere
```
Some examples of this are
```py
# raises general exception
raise Exception

# raise ValueError with custom Error message
raise ValueError('your custom error message here')

# rasise ValueError with no custom Error message
raise ValueError
```
Many built-in exceptions (like `ValueError`), will allow
you to write a custom error message that can be accessed
by the programmer. If you don't want a custom error message
you can write `raise ExceptionName` without `()`. 

We can also print out the exception itself. This will
print out either the custom message specified or a default
message pre-defined by the exception. 
```py
try:
  1 / 0
except ZeroDivisionError as e:
  print(e)
```

Just as the `as` keyword allowed us to rename a module, 
we can rename the exception raised and print it out. 

The output of this block would look like this:
```
division by zero
```
This is the default exception message given to 
`ZeroDivisionError`. 

### Custom Exceptions
If the list of built-in exceptions does not suit your needs,
you can also define your own custom exception.

Defining a custom exception looks like this:
```py
class WorkoutError(Exception):
  def __init__(self, message):
    # we didn't really have to define this attribute
    self.message = message 
```

First we have to inherit from the base `Exception` class
provided by python. If you recall from our last workshop
on [Classes & Inheritance](https://github.com/uclaacm/learn.py-s21/tree/main/session-3-classes-and-inheritance), 
this allows our custom class to inherit all the properties
and methods of the `Exception` class. Thus our custom
exception will behave just like another `Exception`, with
a few of our own customizations of course. 

> If you read the code comment, you'll know that the `message` 
> parameter passed to the constructor is optional. You do
> not have to add any extra parameters in your custom 
> exception. However adding this parameter allows us
> to add a mandatory message parameter to our exception.

Using our exception would look like this:
```py
class WorkoutError(Exception):
  def __init__(self, message):
    # we didn't really have to define this attribute
    self.message = message 

try:
  raise WorkoutError('I don\'t want to workout')
except WorkoutError as e:
  print(e)
```

The output of this code would be:
```
I don't want to workout
```

## File I/O
File I/O stands for File Input/Ouput, which is just fancy
terminology for "reading and writing to files". 

In real life, the way we read and write files follows 3 
very simple steps:
1. Open the file
1. Read or write to the file
1. Close the file

The way we read and write to files in Python is the same.
Writing to a python file would look like this:
```py
f = open('test.txt', 'w')
f.write('boop')
f.close()
```
Let's break this down:
```py
f = open('test.txt', 'w')
```
The `open()` function returns a file object that allows
us to interact file. All future interactions (ex: reading,
writing, etc.) will be through the returned file object
in `f`. 

The `open()` function also takes two parameters. The first
is the name of the file. The second is a letter representing
the _mode_ we are interacting with the file in. `w` stands
for "write". This means that through the file object `f`, we
can write to the file `test.txt`. Here is a summarized
table of the some common modes:

| mode | Description |
| ---- | ------------|
| r | Read from a file. Raise exception if file doesn't exist
| w | Write to a file. Create file if it doesn't exist. 
| a | Append to an existing file or create file if it doesn't exist. 

A full table of all these modes can be found [here in the
documentation](https://docs.python.org/3/library/functions.html#open). 

The mode will determine what functions we can call on the
file object. For example, if we try _write_ through a file object
that was created with _read_ mode, python will raise
an exception. 

Let's get back to our code now:
```py
f = open('test.txt', 'w')
f.write('boop')
```
This code will write the word `boop` to file `test.txt`, 
creating a new file if it didn't already exist. Note: This
`f.write('boop')` will overwrite any pre-existing text 
in the file. If we wanted to append to the file, we would
instead use the `a` mode in `open()`.

If we instead wanted to read from a file, we would do this:
```py
f = open('test.txt', 'a')
data = f.read()
print(data)
```
Assuming that `test.txt` looked like this:
```
eric is cool
```
Then the output of our program would print:
```
eric is cool
```
`f.read()` will _read_ in the contents of the file and
store it into the data variable. We then printed that out
so we could see what was in it. 

> Note: if `test.txt` didn't already exist, python would raise
> an exception. 

Let's finish our file i/o code:
```py
f = open('test.txt', 'w')
f.write('boop')
f.close()
```
`.close()` _closes_ our file object. Aka, we can no longer use
it any more to interact with the file. If we tried writing
to the file again, we'd get an exception:
```py
f = open('test.txt', 'w')
f.write('boop')
f.close()
f.write('beep') # ERROR
```
It is important that you _**always**_ close any file objects
that you are finished with them. This prevents any other
part of your program from having unitentional interactions
with the file. Any writes to a file may also be incomplete
if you don't properly close the file pointer, even if the
program successfully finishes and exits. 

### Safe File I/O
As we have mentioned, it is possible for exceptions to occur
during file i/o. To practice safe coding, we can wrap
our file i/o in `try-except-finally` blocks. 
```py
try:
  f = open('test.txt', 'w')
  try: 
    f.write('boop')
  finally:
    f.close()
except IOError:
  print('Error opening the file')
```
Let's break this down. First we try to open the file, if this
succeeds, then we will try write to the file. Finally, when
we are finished writing to the file, we can close the file
object. If there is an error during any of this code execution,
we can handle it it with the `except IOError` block. 

This is nice, but very tedius to write. 

Fortunately, Python provides a better way to write this.

### the `with` keyword
The `with` keyword can be used during file i/o with the
following benefits:
1. There is less code that is more readable.
1. The file object will automatically be closed without
having to explicitly type it out. 

This looks like this
```py
with open('test.txt', 'w') as f:
  f.write('boop')
```
This opens the file the same as before, stores the file
object into a variable called `f`, then executes the code
block. When the code block exits, `f.close()` will automatically
be called. 
> Note: internally, another function closes the file object,
> but it does the same thing as `f.close()`

To finish this, we can rewrite our entire safe file i/o 
code:
```py
try: 
  with open('test.txt', 'w') as f:
    f.write('boop')
except IOError:
  print('An error occurred')
```

Notice we still have to use a `try-except` block in case
the `open()` function fails. However, this code is much 
cleaner and simpler than our previous code. 

## Time

## Twilio Text Bot Demo



## Wrapup
If you got to here you are a real trooper 😤. Feel free to ask any Hack officer or pop in the ACM discord if you have any questions!

