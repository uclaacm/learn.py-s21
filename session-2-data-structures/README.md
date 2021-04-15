# learn<span>.</span>py Session 2: Data Structures in Python

**Date**: April 14, 2021

**Location**: Zoom

**Teachers**: [Einar Balan](https://github.com/EinarBalan), [Nareh Agazaryan](https://github.com/nareha)

## Resources

- [Slides](https://docs.google.com/presentation/d/1PvyGrX8Lxqzl3lpHhAwIUvFeuixkCE3hU-MGUdDtyMc/edit?usp=sharing)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today
- [Sequences](#Sequences)
    - common operations
    - `in`
    - slicing
- [Tuples](#Tuples)
    - sequence unpacking
- [List Comprehension](#list-comprehension)
- [Lambdas](#Lambdas)
- [Stacks & Queues](#stacks-&-queues)
- [Collections](#Collections)
- [Sets](#sets)
- [Dictionaries](#dictionaries)

## Recap
Last week, we showcased lists and explained that they are a container type in Python similar to resizable arrays in other languages. A key takeaway from our discussion was that lists are a **mutable** type.

 ### As a reminder:
> **mutable**: value can change after initialization <br>
> **immutable**: value cannot change after initialization

Lists are by far the most common structure to store ordered data, but Python offers several alternatives. Today, let's take a look at a couple of them! We'll explore use cases, implementations, and some *really* awesome Python-specific features for each one. First though, let's start with the foundation of all ordered data in Python: Sequences.

## Sequences
So what exactly is a sequence? Essentially, it's just a group of items that have some kind of ordering. Based on this definition, it's pretty clear that a list is a type of sequence (since elements in lists are ordered by their indices). In fact, so far we've shown you three sequence types: lists, strings, and ranges. 

```python
# All of these are sequences! 

li = [99, "h-e-l-o", False]
s = "~data structures~ 😎"
r = range(1, 100, 2)
```

Sequence types in Python have a set of **common operations** that can be applied to them, which is really convenient for us! Here's a quick overview:

![sequence operations](./img/sequence-operators.png)

I won't be covering them all in depth, but there are a few I want to highlight due to how useful they can be, such as...

### `in` Operator
Very often in our programs we want to determine if there is a certain value within a sequence type.

Suppose we wanted to determine if the value, `42`, was in some list, `meaning_of_life`. We could take the DIY approach as follows:

```python
for meaning in meaning_of_life:
    if meaning == 42:
        print("42 is in meaning_of_life!")
```

But this takes up 3 *whole* lines of code. We can do better with the `in` operator which is used as such: `x in s`. The expression will return `True` if the value `x` is contained within the sequence `s`. Let's rewrite our code from before:

```python
if 42 in meaning_of_life:
    print("42 is in meaning_of_life!")
```

Looks a lot nicer, right? Thank you Python developers <3

And of course, just like all the other sequence operators I showed before, `in` can be used with any sequence type.

```python
# All of this is valid! 

>>> False in [99, "h-e-l-o", False]
    True

>>> "ruct" in "~data structures~ 😎"
    True

>>> -99 in range(1, 100, 2)
    False
```

> Note: the `in` used above is not the same as the `in` used in for loops!

### Indexing and Slicing
All sequences can be **indexed** in Python using the square bracket operator. For example, to get the element at the second index in a list:

```python
>>> li = ["hello", [a, b, c], -3, 2300.5]
>>> li[2]
    -3
```

You can also use negative values to retrieve values from the opposite end of a sequence. To get the last element in a sequence:

```python
>>> li = ["hello", [a, b, c], -3, 2300.5]
>>> li[-1]
    2300.5
```

**Slicing** is another super useful sequence operation! It allows you to concisely form subsequences based on an existing sequence. For example, if I wanted to get all the elements of a sequence from the 2nd index to the 5th index:

```python
>>> li = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight"]
>>> li[2:6]
    ["two", "three", "four", "five"]

```

More generally, the syntax for slicing is as follows:

```python
sequence[i:j:k]
```

- where i, j, and k are integers
- i is the inclusive starting index
- j is the exclusive stop index
- k is the step

You can also leave certain fields blank. For example:
```python
>>> [0, 1, 2, 3, 4, 5][:2] # i and k are blank
    [0, 1]

>>> [0, 1, 2, 3, 4, 5][2:] # j and k are blank
    [2, 3, 4, 5]

>>> [0, 1, 2, 3, 4, 5][:] # i,j, and k are blank
    [0, 1, 2, 3, 4, 5]   

 >>> [0, 1, 2, 3, 4, 5][::2] # i and j are blank
    [0, 2, 4]
>>> [0, 1, 2, 3, 4, 5][::-1] 
    [5, 4, 3, 2, 1, 0]
```

One really important thing to understand is that slicing creates **shallow copies**, not deep copies! This means that nested values are not copied, but merely referenced (i.e. they have the same id).

> Note: If the sequence type you're dealing with is mutable, you can use splicing to update the section of the sequence you specify! Check out the docs linked below for more information.

### Key Takeaway
If you take anything away from this discussion, let it be that all sequence types in Python have a set of common operations that can be performed on them. I can't cover them all but I highly recommend checking out [this](https://docs.python.org/3/library/stdtypes.html#:~:text=There%20are%20three%20basic%20sequence,%2C%20tuples%2C%20and%20range%20objects.) website if you're interested in seeing more (particularly about mutable sequences)! 

## Tuples
Tuples are another sequence type in Python (meaning all the same operations from before still apply!). A tuple, much like a list, is simply a general sequence of elements. Tuples can be declared as follows:

```python
t = (1, 2, 3, 4)
t = 1, 2, 3, 4 # parentheses optional!
t = () # empty tuple
t = (1, ) # single element tuple
```

> Note: single element tuples *must* include a trailing comma.

Tuples differ from lists in one very significant way: they're immutable. That means it's not possible to reassign, remove, or insert any elements into an initialized tuple. Note that it is possible to reassign mutable objects within tuples (i.e. lists within tuples).

I know what you're thinking. Why the hell would I ever want to use a tuple over a list?

The short answer is for **optimization**. Tuples take up less space than lists and can be initialized significantly faster. As a result, if there's ever a case where you know that you won't change the values in a sequence, consider placing them in a tuple over a list.

Very often, tuples are used for **heterogenous sequences**, or sequences of different types and the elements in the tuple are accessed via **unpacking**.

### Sequence Unpacking
Unpacking is once again applicable to all sequence types, but it is especially relevant in the case of tuples because it allows for some very nice syntactic sugar (which we'll get to in a second).

Unpacking allows you to directly assign all elements in a sequence to a variable, as follows: 
```python
>>> t = ("a", "b", "c")
>>> x, y, z = t
>>> print(x, y, z)
    a b c

# can be done with any sequence type
>>> t = ["a", "b", "c"] 
>>> x, y, z = t
>>> print(x, y, z)
    a b c
```

Notice that the first variable is assigned to the first element in the sequence, the second variable is assigned to the second element, and so on.

Like I mentioned, unpacking tuples allows for some very convenient syntax:

```python
# assigning multiple variables at once
a, b, c, = 1, 2, 3

# swapping the values of variables
x, y = y, x
```

It's because of simple things like this that Python has won my heart : )

## Demo
Let's write a function that, given two lists, will return a list of every possible pairing of elements between those two lists. If you care, this is called the [Cartesian Product](https://en.wikipedia.org/wiki/Cartesian_product). Let's also add a restriction that given each pairing, each element must be distinct.

There are a ton of ways we could approach this, but let's first take the most obvious route: using loops.

```python
def cart_product(l1, l2):
    result = []
    for i in l1:
        for j in l2:
            if i != j:
                result.append((i, j))
    return result
```

This technically works, but its super ugly to look at! Too much indentation for my tastes 🤮

Let's explore some other options. 

## List Comprehension
List comprehension is a concise way to generate a list from another list in a simple, readable, and elegant way! In order to see just how magical it is, let's transform our cartesian product function from before to use list comprehension.

```python
def cart_product(l1, l2):
    return [(i, j) for i in l1 for j in l2 if i != j]
```

We went from 7 lines of code to just 2. Woah!

Here's the general syntax:

```python
[expression for iterator in iterable if condition]
```
Let's break it down a bit. There are 3 distinct sections: the expression to be added to the list, the iteration, and the condition. For each iteration of the loop, if the condition is met then the expression will be evaluated and added to the resulting list generated by the comprehension (the if condition can also be left off to add values unconditionally). You can also nest multiple loops, as I showed in the `cart_product()` example.

It's definitely possible to go slightly overboard with list comprehensions and make them a bit unreadable, so make sure not to get too carried away! 

## Lambdas
Sometimes it becomes convenient to create anonymous functions (i.e small functions that don't have a name) and pass those around instead of doing the typical declaration. In these cases, we use lambdas! Here's a look at the progression in syntax from a simple `def` function to a `lambda`. Note that none of the intermediates are valid functions.

```python
# normal function declaration
def sum(a, b, c):
    return a + b + c

# start transition
def (a, b, c):
    return a + b + c

         |
         V

lambda (a, b, c):
    return a + b + c

         |
         V

lambda (a, b, c):
    a + b + c

         |
         V

lambda (a, b, c): a + b + c

# lambda expression
lambda a, b, c: a + b + c
```

The lambda expression above (which represents a sum of three values) can then be assigned to a variable or passed around just like any other function in Python.

An important limitation of lambdas to keep in mind is that they are restricted to single expressions for their return values. This means they can only be used for small functions as shown above!

Lambda's (as well as the fact that functions are first class objects) are key to Python's status as a multi-paradigm programming language. They allow the langauge to be used in a functional way. Next week, we'll take a look at an object-oriented approach to Python.

## Stacks & Queues

Let's explore a really cool application of lists, which leads to a very important concept with data structures. We're talking about stacks and queues! These are very similar in concept, but work quite different fundamentally.

First, the stack. A stack is a structure where the elements that are inserted *first* are removed *last*. We call this **LIFO**, which is a cool way of saying that the elements that go in last are the first to leave. Conceptually, think of this like a stack of dishes or flapjacks. You stack dishes on top of each other, then remove them one by one from the top (unless you want all the dishes to drop and break). Adding items to a stack is called "push", and removing is called "pop"!

Let's observe some stack operations!
```python
cool_letters = []
cool_letters.append('n')
cool_letters.append('b')
cool_letters.append('x')
print(cool_letters)
# ['n', 'b', 'x']

# This has been the same as a list so far, so let's get into how to use lists as stacks and queues. First, with a stack.

# .pop() returns a value, that we can store in a variable
current_fav_letter = cool_letters.pop()
print(current_fav_letter)
# x
print(cool_letters.pop())
# b
print(cool_letters)
# ['n']

type(cool_letters)
# <class 'list'>

# Let's pop one more time to get an empty stack
cool_letters.pop()
# 'n'
print(cool_letters)
# []

# What happens if we try to pop again?
cool_letters.pop()

# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     cool_letters.pop()
# IndexError: pop from empty list
# DO NOT pop on an empty stack, or you'll get an error!
```

Queues work in a similar way. A queue is a structure where the elements that are inserted *first* are also removed *first*. We call this **FIFO**, meaning the elements that go in first are the first to leave as well. You may think of it like standing in line at a store, where the customers in front are the ones who will be checked out first, and so on. Adding items to a queue is called "enqueue", and removing is called "dequeue"!

Now let's observe some queue operations!
```python
# Let’s see how we work with queues!

fav_fruits = ['strawberry', 'orange', 'watermelon']
print(fav_fruits)
# ['strawberry', 'orange', 'watermelon']

# Use .pop(0) to dequeue an item!
fav_fruits.pop(0)
# 'strawberry'
fav_fruits
# ['orange', 'watermelon']

# Let's clear the queue
fav_fruits.pop(0)
# 'orange'
fav_fruits.pop(0)
# 'watermelon'


fav_fruits.pop(0)
# What happens if we try to pop again?
# Traceback (most recent call last):
#   File "<pyshell#31>", line 1, in <module>
#     fav_fruits.pop(0)
# IndexError: pop from empty list
# DO NOT pop on an empty queue, or you'll get an error!
```

There are many applications of stacks and queues, some of which can get quite complex. Some examples of stacks are an undo feature in a text editor, or the back button in your browser. Queues tend to have a bit more complex applications, but consider any situations in which you need to keep track the order in which things come in. A CPU does this often when keeping track of what tasks to accomplish.

>As a side note, one cool thing you may try is think about how you might implement a maze solver with a stack, versus how you would accomplish this with a queue. How are they different? We call these *depth-first search* and *breadth-first search*. Can you figure out what they mean and which belongs to which data structure? :)

>Note: When making queues, lists are not the most efficient way to do so. Because of the way lists are implemented, popping the first item is very inefficient. In fact, due to this, traditionally lists aren't used for queues. Instead, we can use `collections.deque` or `queue.Queue` (pronounce deque as "deck" to distinguish from the queue operation of dequeueing). I'll describe here how to do so with `collections.deque`, because once you understand different data structures conceptually, it is better to use the most efficient data structure for what you're trying to achieve. If you've taken CS 32 or any equivalent, you may have heard of linked lists. In fact, the linked list is how a deque is implemented, which is why deque is more efficient than having to shift over elements within a list when popping from the front.

To use `collections.deque`, we will need to make an import statement. Import essentially gives you access to code that isn't immediately built into Python, but exists in a different "module" (an object that serves as an organizational unit of Python code). Once we have it imported, we can use deque!

```python
from collections import deque
 
# This is how you may initialize an empty deque
my_seque = deque()
 
# Populating the queue with some elements
my_queue.append('a')
my_queue.append('b')
my_queue.append('c')
 
# This will show us the initial queue, which is ['a', 'b', 'c']
print(my_queue)
 
# Removing each elements from a queue
print(my_queue.popleft()) # 'c'
print(my_queue.popleft()) # 'b'
print(my_queue.popleft()) # 'a'

# We now have an empty queue
print(my_queue)
 
# Any .popleft() operations from this point will result in an error, since the queue is empty
```

We observe that while conceptually and operationally, they are very similar to how queues work, there are some different operations. `.popleft()` is equivalent to `.pop(0)`, but is more efficient behind the scenes. As you go forward, it is recommend that you use deque once you have an understanding of how queues operate!

## Collections

Collections in Python are similar to sequences in that they also hold data, but they work a little differently! Collections __don't use deterministic ordering__, meaning what you added **will not** stay in the same order that you added them. The ones we will talk about today are Sets and Dictionaries!

## Sets

A set is a type of *unordered* collection that does not allow duplicate items. To initialize a set, you either use `set()`, which you do to make an empty set, or `my_set_name = {1, 2, 3}`.

We can perform some mathematical operations that are inherent to sets. Let’s say we perform these on sets myset and myset2.
-  Union: Resulting set is all items in myset and myset2 (both unique and shared items).
- Intersection: Resulting set is all items in myset and myset2 that are shared amongst the two.
- Difference: Resulting set is all items in myset that are not in myset2.
- Symmetric Difference: Resulting set is all items in myset and myset2 that are in one, or the other, but not both.

Why should we use Sets over, say, a list? We use sets because sets are faster than lists if you want to check if a certain item is contained within it. However, they can only contain one occurrence of an item. If you wanted to just store a certain amount of things, ie all your favorite fruits, it may be better to use a set because you do not need your favorite fruits to be listed twice and it's not really necessary to access a certain fruit in a certain order. You may just want to know whether a certain fruit is a favorite or not.

There are more set operations that we can do!
- To add an item to a set, you do `set_name.add(value)`.
    - You are able to add items that are of different types into a set
- To remove a certain item, we have two methods, `discard` and `remove`.
    - The difference between the two is that if the element is not in the set and you try to remove it, remove will give you an error, while discard will not.
    - There is also the previous `.pop()` removes one random element from the set.


## Dictionaries

Dictionaries are another very useful form of storing data. You can think of dictionaries as **key:value** pairs, where the keys must be unique within each dictionary. Dictionaries can be iterated over, but since they use keys, they cannot be indexed, which is why they are not a sequence. For example, you can still make make a for loop to print out each of the items within a dictionary! It's important to note that in a dictionary, the keys can be of any **immutable** data type.

To create an empty dictionary, you may simply do `variable_name = {}` and add one by one. You may also put some initial key:value pairs into the dictionary by doing something similar to the following:
```python
percent_of_hades_completion = {‘run1’ : 2, ‘run19’ : 20}
```

Now you may be wondering: *Wait, how does Python know the difference between an empty set and an empty dictionary, if they’re both using curly braces?* Good question! By default, doing `my_var = {}` will tell Python that you want to make a dictionary. The way to create an empty set is by doing `my_var = set()`.

As with all containers, there are some dictionary operations that we may do!
- You may do `sorted(dictionary_name)` to sort the dictionary by key!
- Adding items to the dictionary is done by doing `dictionary_name[some_new_key] = some_new_value`
- You can retrieve values by either using `dictionary_name[some_key]` or `.get(some_key)`
    - Using [] will give you an error on keys that do not exist, while .get() will simply return None
- You can update items by doing `some_dictionary[some_key] = some_updated value`
- You can delete items by either doing:
    - `.pop(key_name)` [This will give an error if it does not exist]
    - `.popitem()` [This will remove the last item that was inserted]
        - Before version 3.7, it popped a random item
    - You may also do `.clear()` to wipe the entire dictionary!
