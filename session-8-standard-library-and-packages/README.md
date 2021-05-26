# learn<span>.</span>py Session 8: Standard Library and Packages <!-- omit in toc -->

**Date**: May 26, 2021

**Location**: Zoom

**Teachers**: [Jakob Reinwald](https://github.com/jakobreinwald), [Chandra Suresh](???)

## Resources <!-- omit in toc -->

- [Slides](http://links.uclaacm.com/learnpy21-s8-slides)
- [ACM Membership Attendance Portal](https://members.uclaacm.com/login)

## What we'll be learning today <!-- omit in toc -->
- [A Couple Quick Library Shoutouts](#a-couple-wuick-library-shoutouts)
- [Preview Demo Libraries](#preview-demo-libraries)
- [Demo!](#demo)
- [More Standard Libraries!](#more-standard-libraries)
  - [TensorFlow](#tensorflow)
  - [OpenCV](#opencv)

## A Couple Quick Library Shoutouts
- [Quick Note](#quick-note)
- [os](#os)
- [glob](#glob)
- [timeit](#timeit)
- [Data Structures](#data-structures)


## Quick Note
- The following few slides are meant to be a *very* brief introduction to a few libraries you may find useful
- Within a Python file/interpreter, run the following commands:
  - ```dir(<module>)```
    - Returns a list of all module functions
  - ```help(>module>)
    - Returns an etensive manual page for module


## os
- os provides dozens of functions for interacting with the operating system
  -  Make directory, list directory contents, get current working directory, and more!
-  imported with ```import os```
-  [os docs](https://docs.python.org/3/library/os.html)


## glob
- glob is used to retrieve files and pathnames that match a specific pattern
  - If you are familiar with grep in linux, it is kind of like that
  - It also accepts regex! (woohoo regex)
- imported with ```import glob```
- Example usage:
  - ```glob.glob('something')```
  - ```glob.glob('./[0-9].*')```


## timeit
- If you're interested in checking the performance of your programs or comparing speeds of different commands,
  - the timeit library is perfect for you!
- imported with ```import timeit```
- Example usage: 
  ```
  from timeit import Timer
  Timer(`commands to check`).timeit()
  ```
  - This will time and returns the time it took to run the command in the quotes.


## Data Structures
- Remember stacks, queues, heaps, etc. from cs32? We can use those in python too! One of the main benefits of
  - using data structures such as deque is that they provide quicker append and pop options than a normal list.
Examples:
  ```
  from collections import deque
  my_deque = deque(["Mr Krabs", "Gary", "Squidward"])
  ```
  ```
  import heapq
  heapq.heapify(<some list you already have>)
  ```
  The heapify command will rearrange the list you have into a heap order.
  
  
## Preview Demo Libraries
- Alright! Now that we have shown you just a couple of standard libraries you could find useful, lets talk
  - about some of the ones we will be demoing and taking a closer look at!
  - 
## Demo! (Numpy, Matplotlib, + more)

