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
  the timeit library is perfect for you!
- imported with ```import timeit```
- Example usage: 
  ```
  from timeit import Timer
  Timer(`commands to check`).timeit()
  ```
  - This will time and returns the time it took to run the command in the quotes.


## Data Structures
- Remember stacks, queues, heaps, etc. from cs32? We can use those in python too! One of the main benefits of
  using data structures such as deque is that they provide quicker append and pop options than a normal list.
- Examples:
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
- Alright! Now that we have shown you just a couple of standard libraries you could find useful, lets quickly
  talk about some of the libraries we will be demoing and taking a closer look at!
- [math](#math)
- [random](#random)
- [statistics](#statistics)
- [numpy](#numpy)
- [matplotlib](#matplotlib)


## math
- The math library is used for mathematical operations and constants.
- imported with ```import math```
- [math docs](https://docs.python.org/3/library/math.html)


## random
- The random library is used for generating numbers and other cool random stuff! 
- imported with ```imported random```
- [random docs](https://docs.python.org/3/library/random.html)


## statistics
- The statistics library is used for calculating basic statistical properties of numerical data.
- This one needs to be installed:
  - ```pip3 install statistics```
  - imported with ```import statistics```
- [statistics docs](https://docs.python.org/3/library/statistics.html)


## NumPy
- Numpy, which stands for Numerical Python, consists of more advanced math and logical operations. It's most
  used attributes are its powerful n-dimensional arrays, and various numerical comuting tools.
- imported with ```import numpy as np```
- [numpy docs](https://numpy.org/doc/stable/user/quickstart.html)

- Here's a little more detail about some of the cool stuff in ```numpy```:
  - ndarray
    - "n-dimensional array", each dimension is an "axis"
    - ```numpy``` has TONS of array manipulation, slicing, indexing functionality (chandra will be demonstrating
      some of this later :-) )
  - ```arrange(start, stop, step)```
    - Returns an ndarray of evenly spaced (by step) values, from start to stop
  - Basic math functionality
    - ```random()```, ```sin()```, ```cos()```, ```pi```, etc. etc. etc.


## matplotlib
- matplotlib is a library for creating graphs in Python
- Basically, imagine you have control in some way of literally every single aspect of a graph you could ever think of,
  and that's kind of where you're at with ```matplotlib```
- I'll save the rest of this description for the demo! Most of it will become very self explanatory :)
  
## Demo! (Numpy, Matplotlib, + more)
- Let's get started with some basic graphing! First, we need to add our imports:
```
import matplotlib.pyplot as plt
import numpy as np
import random
import math
from statistics import mean, median
```
- Let's start with someting super basic, like just graphing sin of x. We can begin by creating x and y:
```
x = np.arange(0.0, 2 * np.pi, .1)
y = np.sin(x)
```
- For x, we generate a range between 0 and 2pi, with steps of .1. Then, for y, we just have a numpy array of 
  the sin of all the x values.
- From here, it's super easy! All we have to do is:
```
plt.plot(x, y)
plt.title('Sine Graph', y=.96, fontsize=9)
```
which plots x and y, and adds a graph title (more on those weird parameters later). Now, lets run it and see our graph!
![Sine Graph](./part-1-numpy-matplotlib/assets/sine.png)

