# learn<span>.</span>py Session 3: Classes and Inheritance

**Date**: April 21, 2021

**Location**: Zoom

**Teachers**: [Jakob Reinwald](https://github.com/jakobreinwald), [Alex Xia](https://github.com/khxia)

## Resources

- [Slides](TODO)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- Intro to Scopes
- Classes
  - __init__()
  - Instance Objects
  - Attribute References 
- [Inheritance](#inheritance)
  - Overriding methods
  - `super()` function
  - Private variables in Python
- [`__doc__`](#__doc__)
- [Iterators](#Iterators)
- [Generators](#generators)
  - Generator Expressions

## Intro to Scopes

Let’s start with a quick demo. 
```py
less_specific = 5

def foo():
    more_specific = 2
    print('Inside foo:', less_specific)

foo()
# print(more_specific) will not work (accessing local scope variable outside of local scope)
```
As we could see, I could not access the variable more_specific outside of the function foo, but I could access the variable less_specific inside the function foo. Huh?
So, let’s start with a question. At any point in a program, what variables and functions do I have access to? Does it matter where I am in my program?
The short answer is. . . Yes! It does matter. The information you currently have access to is determined by the scope you are currently in.

Scopes are textual regions of a Python program that define in your code where variables/methods can be accessed. One of the most important aspects of scopes is that a more specific scope can access the information of a less specific scope, but not the other way around

Now, lets go into the types of scopes! But before that, a quick note for people migrating from C++ or might not be familiar with this concept in Python:
- In python, functions can be nested within other functions, which is super cool! They’re just called nested functions. Here’s an example: 
```py
def a():
    def b():
        print('hello from nested function!')
    print('hello from outer function!')
    b()
a()
```
I have a function a that has a nested function b, which prints out ‘hello from nested function’. Then, in a, I print ‘hello from out function’ then call the nested function b. That means that if I call a, I would expect an output of the outer function message, then the nested function message. To check though, lets run it ourselves.

Now, lets go over the types of scopes.
In order from most to least zoomed in:
Local Scope: The local scope refers to the names inside a class/function. Outside a class/function, the local scope is same as global scope. Even if a function has a nested function, the local scope of a class/function is always itself. We will see this demonstrated on the next slide.
Non-local Scope: Midways between the local and global scope. Relevant for nested functions (ex: the non-local scope of a function a within function b is function b)
Global Scope: The scope outside any functions of class definitions. This is sometimes also called the “module” scope
Built-ins Scope: Built into python. TThe function print is not defined in our program, but is built into python itself (built-ins scope)

What does this all mean?? Basically, Scopes allow us to be sure that:
- More specific namespaces will never be altered by less specific namespaces
- More specific namespaces will always have access to less specific namespaces (read-only, however)

Here is a short demo of how scopes work:
```py
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
```

## Classes

Now, lets move on to classes. As a basic intro, Classes provide a means of bundling data and functionality together. They allow us to create a new type of object and create instances of that object. Each class has attributes attached to it that maintain its state and functionality. As a quick sidenote, what is an attribute? A class attribute is a feature or characteristic that belongs to a class. It can be a variable, but it can also be a method. They allow for the object to maintain and perform its functionality. 

Another quick thing: instance variables vs class variables: their difference is important: instance variables are data unique to each instance of a class, while class variables are common to all instances of the class. Example: every car has four wheels, so number of wheels would be best as a class variable, but each car has a different name, so car name would be best as an instance variable.

Now, how do we create a class?? Basically, you put `class Classname:`, indent, and write out all your statements of class definition. This could be variable declaration, method declaration, etc.. Once the class definition is left, a class object is created. Class objects support two kinds of operations: attribute references and instantiation. Attributes can be accessed with `class_object.attribute_name` and are instantiated using function notation:
`x = MyClass()`  creates a new instance of the class and assigns it to local variable x. 
The instantiation operation creates an empty object, however, many classes need to be created with instances that start in a specific state. Therefore, a class definition may include a special function called `__init__()`. `__init__()` is Python's constructor, and is automatically invoked when a class is created. Its definition looks like this:
```py
def __init__(self):
	<initialize/assign attributes of your class>
```

But wait a minute, what's `self`? `self` is usually the first argument of a method, which represents passing the instance object into the method. It is kind of like `this` from C++, but it has to be passed as a parameter in `__init__()`. Init may also have arguments for greater flexibility. Arguments passed in during class instantiation are given to `__init()__`. So, if I have a variable attribute that I want to initialize to an argument provided by the user, I would do it like so in `__init__()`: 
```py
def __init__(self, argument1):
	self.attribute = argument1
```
And in order to pass the argument argument1 into `__init__()`, I need to pass it in to the function notation when I declare my class:
`new_instance = class_name(argument1)`

So, we have our object, now what? Instance objects can only understand attribute references, of which are two types: data attributes and methods.
Data attributes are “instance variables” or “data members”, and spring into existence when first assigned to. Methods are functions that “belong” to a class. Additionally, the method belonging to an instance of a class is a method object, meaning that it can be stored for later use:
`xf = x.f()`
Now, `xf()` can be called later.

Demo time! We are going to go over a very basic class demo, and then I want to do a demonstration of why you should be careful using mutable objects as class variables. 
```py
# Basic class example: class Telescope
class Telescope:
    zoominess = 120

    # Initializing attribute of class by passing arguments into init
    def __init__(self, type):
        self.type = type

    def zoom_in(self):
        self.zoominess *= 2

    def zoom_out(self):
        self.zoominess /= 2

# Pass values that will be given to init for assignment to instance variables
bigboi = Telescope('big')
smallboi = Telescope('small')

# Demonstration of attribute references 
bigboi.zoom_in()
smallboi.zoom_out()

print(bigboi.type, bigboi.zoominess)
print(smallboi.type, smallboi.zoominess)
```

```py
# Another basic class demo, this time showing why mutable class variables is not good
class Telescopes:
    # class variable that is mutable (!)
    telescope_names = []

    def __init__(self, location):
        self.location = location

    def add_telescope(self, telescope_name):
        self.telescope_names.append(telescope_name)


observatory1 = Telescopes('San Jose')
observatory2 = Telescopes('LA')

observatory1.add_telescope('pirate scope')
observatory2.add_telescope('toy scope')

# Both objects' telescope_names is the same! Very bad!
print(observatory1.location, observatory1.telescope_names)
print(observatory2.location, observatory2.telescope_names)
```

```py
# Fixed example
class TelescopeNames:

    # We can fix this by making telescope_names an instance variable, by putting it in init
    def __init__(self, location):
        self.telescope_names = []
        self.location = location

    def add_telescope(self, telescope_name):
        self.telescope_names.append(telescope_name)


observatory1 = TelescopeNames('San Jose')
observatory2 = TelescopeNames('LA')

observatory1.add_telescope('pirate scope')
observatory2.add_telescope('toy scope')

# They are different this time! Yay.
print(observatory1.location, observatory1.telescope_names)
print(observatory2.location, observatory2.telescope_names)

# In summary, why not to use mutable objects as class variables: 
#       They will be modified/shared by all instances of the class
```


## Inheritance

No worthy programming language would have classes without having **inheritance**. But what is **inheritance**? It means that we are able to define a class that can *inherit* all the methods and properties from another class. 

Let's see a simple example of this. Let's say that we definined a `Person` class that was capable introducing itself and burping. 
```py
class Person:
    def __init__(self, first, last):
        print("I am a Person")
        self.firstname = first
        self.lastname = last
    
    def introduce(self): 
        print("Hi! My name is", self.firstname, self.lastname)
    
    def burp(self):
        print("~~burp~~")
```

This is pretty good, but what if we wanted to define another class `Student`? Well, a `Student` is also a `Person`, so we would want the Student to also be able to introduce themselves and burp. But `Student`'s can also study, so let's add that in. 

```py
class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        self.firstname = first
        self.lastname = last

    def introduce(self): 
        print("Hi! My name is", self.firstname, self.lastname)
    
    def burp(self):
        print("~~burp~~")
    
    def study(self):
        print("studying~")
```

This not very efficient. We are repeating the same code from `introduce()` and `burp()`. How do we let Python know that a `Student` should also be able to do things that a `Person` can do? This is through **inheritance**. 

In programming, we refer to the **parent class** as the class being inherited from, in this case it is `Person`. We use **child class** to refer to the class that inherits from a parent class, in this case it is `Student`. Let's see how to do this in Python. 

```py
class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        Person.__init__(self, first, last)
    
    def study(self):
        print("studying~")
```

Notice that we specified the **parent class** as arguments to the first line of the class definition in the **child class**. Inside the class definition, we can then refer to that parent class as if it was a variable being passed in as an argument. It is often good practice to call the **parent class**'s `__init__()` function inside the `__init__()` function of the **child class** (Note that `self` is required as the first argument). 

So now, if we create a `Student` class like so, it is able to access all of `Person` class's methods. 

```py
y = Student("Alex", "Xia") 
# I am a Student
# I am a Person

y.introduce() 
# Hi! My name is Alex Xia

y.burp()
# ~~burp~~

y.study()
# studying~
```

> Why inheritance?
>> Inheritance is useful not only to save us time when writing code, but it also gives programmers a solid foundation with which to work with. It allows us to create relations within our code and can help to structure very complex projects. These are of course, only a few of the reasons. Inheritance is a core part of the object-oriented programming paradigm. 

### Overriding Methods

Sometimes, we may want to override some methods that existed in a base class. How do we do this in Python? 

> Answer: We simply just re-define it.

Say we wanted every `Student` to have a more unique way of introducing themselves as compared to other `Person` objects. 

```py
class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        Person.__init__(self, first, last)

    def introduce(self):
        print("Hi! My name is", self.firstname, self.lastname)
        print("I am a nerd")
    
    def study(self):
        print("studying~")
```

There we go, all we did was redefine the function as if it never existed in the first place. Now, when we call the function, Python will first look in the `Student` class for the `introduce()` function, if it doesn't exist then it will look in the `Person` class; Python will always prioritize the most derived definition of the class. 

So now if we call `y.introduce()`

```py
y.introduce()
# Hi! My name is Alex Xia
# I am a nerd
```

Wait hold up. Something's wrong here 🤔. We have repeated a line! We used the line 

```py
print("Hi! My name is", self.firstname, self.lastname)
```
in both definitions of the `introduce()` function. As programmers, we can do better. So let's call `Person`'s `introduce()` function inside of `Student`'s. 

```py
class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        Person.__init__(self, first, last)

    def introduce(self):
        Person.introduce(self)
        # print("Hi! My name is", self.firstname, self.lastname)
        print("I am a nerd")
    
    def study(self):
        print("studying~")
```

Since we are able to access all of Person's methods and attributes, we can then call Person's functions, hence simplifying the code. 

Notice that, as opposed to `C++`, we don't need to do anything special to the `introduce()` function in `Person`'s definition to allow it to be overrided by a subclass. If you're a `C++` nerd, this basically means that all Python methods are effectively `virtual`. 

### `super()` function

Instead of referring to `Person` inside of `Student`'s class definition, Python actual supplies us with a function called `super()` that will give us a delegate object that refers to ALL parent classes. 

So instead, we can do something like this:

```py
class Student(Person):
    def __init__(self, first, last):
        print("I am a Student")
        super().__init__(first, last)

    def introduce(self):
        super().introduce()
        # print("Hi! My name is", self.firstname, self.lastname)
        print("I am a nerd")
    
    def study(self):
        print("studying~")
```
This is the exact same thing as our previous code. Notice that we no longer need to pass in `self` as an argument. 

`super()` is useful when a class inherits from multiple parent classes. So for example, we can have an `Adult` class that inherits from `Person`, and have a `UCLAStudent` class that inherits from both `Adult` and `Person`. 

```py
class Adult(Person):
    def __init__(self, first, last):
        print("I am an Adult")
        super().__init__(first, last)

class UCLAStudent(Student, Adult):
    def __init__(self, first, last, uid):
        print("I am a UCLA Student")
        super().__init__(first, last)
        self.uid = uid
    
    def study(self):
        print("Studying for the Reinman midterm~")
        super().burp()
```

Notice now, if we do:
```py
z = UCLAStudent("Einar", "Balan", 123456789)
# I am a UCLA Student
# I am a Student
# I am an Adult
# I am a Person

z.study()
# Studying for the Reinman midterm~
# ~~burp~~
```

This is useful because now we don't need to worry about who's inheriting from who, or which parent class to specify, we just need to use `super()` and let it handle all of the inheritance for us. 

> Note: `super()` has other use cases apart from this. Generally, it is recommended to use `super()` since it is well defined even when there is complex inheritance going on. If you're interested in learning more, you can read up about the `super()` function and **[MRO](https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/)** (Method Resolution Order) in Python.


### Private Varibles in Python

Sike! Python doesn't really have private variables that cannot be accessed outside of an object. However, if you prefix an underscore _ to an attribute name, by convention, this means that it is private. Programmers should generally not try to mess with a class attribute that starts with _. 

For example: 

```py
class Person:
    def __init__(self, first, last):
        print("I am a Person")
        self.firstname = first
        self.lastname = last
    
    def introduce(self): 
        print("Hi! My name is", self.firstname, self.lastname)
    
    def burp(self):
        print("~~burp~~")

    _dna = 'secret dna' # technically private! But not really!
```

## `__doc__`

This is an attribute that is used for the documentation of a class. Often times, you may see a class definition with a `""" """` syntax. This is used for documentation purposes and the text inside should be a good, brief description of the class. This description can then be accessed using the `__doc__` attribute. 

For example: 
```py
class Yeet():
    """A class made for Python nerds to yeet"""
    def __init__(self):
        print("yeet")

x = Yeet()
# yeet

print(x.__doc)
# A class made for Python nerds to yeet
```

## Iterators
By now, you've probably noticed that we could iterate over any sequence using a `for` loop.

```py
for element in [1, 2, 3]:
    print(element)

# 1 
# 2
# 3
```

How does Python achieve this? The answer is using **iterators**. 

Every object in Python has the `__iter__()` and `__next__()` methods. Just like the `__init__()` method, they are special methods that have really specific behavior that we can redefine as well. Together, `__iter__()` and `__next__()` are called the **iterator protocol** and using these methods, Python is able to loop over the items in an object. 

- `__iter__()` returns an iterator object that we can iterate over. 
- `__next__()` enables use to manually iterate through all items of an iterator. When we reach the end and there is no data to be returned, it will raise a StopIteration.

Let's see this in action for a `List`.
```py
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> print(it)
<list_iterator object at 0x0000021F6AB3F7F0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    it.__next__()
StopIteration
```

> Note: Instead of using the `x.__iter__()` and `it.__next__()` notation, we can use the built-in `iter(x)` and `next(it)` syntax that does the same thing.

Ok, this is cool and all, but how do we define our own **iterator protocol**? Simple, we just need to define our own `__iter__()` and `__next__()` methods in our class. 

For example, let's say that I want to define a class that will return a counter that will count up to a certain number. It will initially look like this:

```py
class NumberCounter():
    def __init__(self, num):
        self.max = num
```

Now, let's define the `__iter__()`. 

```py
class NumberCounter():
    def __init__(self, num):
        self.max = num
    
    def __iter__(self):
        self.count = 0
        return self
```

In our `__iter__()` function, we initialized a `count` variable to 0 to start counting, and then we returned `self`. All `__iter__()` functions return `self`, since we are going to be iterating over ourselves. 

Now, let's define the `__next__()`.

```py
class NumberCounter():
    def __init__(self, num):
        self.max = num
    
    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        self.count = self.count + 1
        if self.count <= self.max:
            return self.count
        else:
            raise StopIteration
```

This one's a little more complicated. So first, we increment our count. If we are not over the maximum, then we simply return our incremented count. If not, then we need to return a `StopIteration` exception. 

So in the normal case, our `__next__()` function should `return` whatever we are iterating over. In this case, it is our integer `count`. 

When we want to stop iterating, we need to return a `StopIteration` exception. But in Python, whenever we need to raise an exception, we don't `return` it. Instead, we `raise` an exception using the `raise` keyword.

So now, if we do something like this:

```py
>>> count5 = NumberCounter(5)
>>> it = count5.__iter__()
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
4
>>> it.__next__()
5
>>> it.__next__()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    it.__next__()
  File "<pyshell#18>", line 14, in __next__
    raise StopIteration
StopIteration
```

We see that this is exactly the output that we want. In fact, now, we can iterate over an instance of this object with a `for` loop.

```py
count4 = NumberCounter(4)
	  
for elem in count9:
	print(elem)

# 1
# 2
# 3
# 4
```

So now we see that `Lists`, `Tupes`, `Strings` are iterated using the **iterator protocol** because these things are all objects in Python.

## Generators

So we just learned about **iterators**, which was pretty cool. But honestly, that was kind of a lot of work just to implement a counter. We had to implement a class with the `__iter__()` and `__next__()` methods, keep track of internal states, and raise `StopIteration` when we are done. 

This is quite lengthy and shouldn't need to be that long for something so simple. 

Generators to the rescue! It turns out that Python [generators](https://www.programiz.com/python-programming/generator) are a simple way of creating iterators. To put it simply, generators are functions that will return an iterator object. Using this iterator object, we can manually iterate over whatever we defined inside the function. The generator will take care of all the `__iter__()` and `__next__()` stuff. 


Defining generators in Python is as easy as defining a normal function, except that instead of using the `return` statement, we use the `yield` statement. 

The key is that while a `return` statement will make the program exit the function for good, a `yield` statement *pauses* the function: saving all states and variables, and later *continues* execution from that pausing point whenever the function is called again.

**So what's the difference between a normal function and a generator?**

- Generator function contains one or more `yield` statements.
- When called, it returns an iterator
`__iter__()` and `__next__()` are implemented automatically
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables are remembered between successive calls.
- Finally, when the function terminates, `StopIteration` is raised automatically on further calls.
  
Let's see how we can implement our `NumberCounter` from the previous example:

```py
def countGen(max):
    for i in range(1, max+1):
        yield i
```

Wow! That was so much shorter and it makes so much sense. When we are in the `for` loop, whenever we call, `yield i`, the generator function will return the value of `i`, but when the function is called again, it will continue execution from where it left off in the `for` loop. 

Now, when we do this:

```py
>>> count6 = countGen(6)
>>> count6.__next__()
1
>>> count6.__next__()
2
>>> count6.__next__()
3
>>> count6.__next__()
4
>>> count6.__next__()
5
>>> count6.__next__()
6
>>> count6.__next__()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    count6.__next__()
StopIteration
```

Similarly if we do:
```py
count3 = countGen(3)
for num in count3:
    print(num)

# 1
# 2
# 3
```

### Syntactic Sugar: Generator Expressions

So, remember how we could do list comprehension to shorten our code? We can do the same thing with generator expressions!

However, instead of using square brackets [], we use parentheses () instead. 

If you recall, if we did something like this with a list:

```py
# Creates a new list with elements from 1 to 20
newlist = [x for x in range(1, 20)]
```

We can do exactly the same thing with generators:

```py
count19 = (x for x in range(1, 20))

# This is the exact same as:

count19 = countGen(20)
```

Again, as we stated with list comprehension, while generator expressions are useful and can are super succinct, if your generators expressions get more complex, we should generally avoid them since we are sacrificing readability for simplicity.
