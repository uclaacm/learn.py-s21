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
- Awesome! (Don't worry, the title will be fixed later)
- Alright, now let's go up another step. This time, let's generate some random data, then graph it and see how it looks.
```
x = np.arange(0, 3 * np.pi, 0.1) 
y = [random.randrange(-10, 10) for i in range(0, len(x))]
```
- This time, our x values are a range from 0 to 3pi, with steps of .1, and our y values are, for each value in x, a randomnly generated 
  number between -10 and 10. This will probably look really interesting.
- Now, say I want to see both my old graph, and my new graphs! Luckily, we can totally do that. So, in front of our old graph's code, lets add:
```plt.subplot(2, 2, 1)```, which will initialize the first of four subplots in a 2 by 2 grid. That way, when we plot our first graph, it'll go
  in the first spot.
- Then, we can put the following in front of our second graph:
```plt.subplot(2, 2, 2)```, which will initialize it as our second plot of 4. (if you haven't picked up by now, we're going to make 4 graphs.
- Don't forget to also plot your second graph! 
```plt.plot(x, y) 
plt.title('Random', y=.96, fontsize=9)
```
- Now, let's see how it looks.
![Two Graphs](./part-1-numpy-matplotlib/assets/2graphs.png)

- Awesome! Now, let's just make two more quick graphs to test out a couple other things.
- For our third graph, we first have to initialize the third subplot, then our x:
```
plt.subplot(2, 2, 3) 
t = np.arange(0., 5., 0.2)
```
- Now, let's demonstrate that we can show multiple lines on the same graph! 
```
plt.plot(t, t, 'r--')
plt.plot(t, [math.pow(t, 2) for t in t], 'bs') 
plt.plot(t, [math.pow(t, 3) for t in t], 'g^')
plt.title('Cool Graph', y=.96, fontsize=9) 
```
- Here, we plot 3 lines. The first is just y = x. The third parameter, ```r--```, sets the color of the line to red (```r```), and makes the line's
  style a dotted line (```--```). Our second line is going to be y = x^2, as you can see from our use of the math.pow(base, exponent) function. Here,
  the third parameter sets the line color to blue, and the line style to squares. The third line, as we can see, is going to be y = x^3, and the third 
  parameter means we're going to have a green line represented by triangles. 
- I'm sure this seems like a lot of information, but remember, we are just trying to show you some of the capabilities of these libraries. You definitely
  don't need to remember any of this, as you can always look at the documentation or look it up easily! Hopefully this just gives you an idea so that one day,
  when you're thinking about a certain way to implement something in python, you can remember, "oh hey that one guy in that workshop mentioned *xyz* thing, 
  let's look that up!"
- Awesome. Let's check out this graph now:
![Three Graphs](./part-1-numpy-matplotlib/assets/3graphs.png)

- For our fourth graph, let's actually try to involve some data. I told you those libraries would be useful! First, let's initialize our subplot and generate
  some random data sets:
```
plt.subplot(2, 2, 4) 
data1 = [random.randrange(0, 15) for i in range(1, 10)]
data2 = random.sample(range(0, 30), 10)
data3 = [random.randint(0, 60) for i in range(1, 10)]
```
- As you will find out, the randrange function generates a random integer in the given range. The random sample function randomnly samples without replacement 
  from a range or dataset. Finally, the randint function also returns a random integer in a given range. There are some subtle differences between randrange
  and randint that I won't go over here, but if you are interested, you can find some info at this link: 
  [difference between randint and randrange](https://stackoverflow.com/questions/3540431/what-is-the-difference-between-random-randint-and-randrange)
- Now, for this one, we're going to create a bar graph! Let's first generate our bar titles to see what we are graphing:
```x_axis = ['d1mean', 'd1med', 'd2mean', 'd2med', 'd3mean', 'd3med']```
- As you can see, we're going to be graphing the mean and median of each of our data sets. Let's get right to it:
- ```y_axis = [mean(data1), median(data1), mean(data2), median(data2), mean(data3), median(data3)]```
- Now, lets graph away!
```
plt.bar(x_axis, y_axis)
plt.title('Random Data', y=.96, fontsize=9)
```
![Ugly Graphs](./part-1-numpy-matplotlib/assets/ugly-graphs.png)
- Woah, what the heck is that! Why are our x ticks all bunched up and ugly?
- Well, everything is beautiful in its own way, but you're right, we should probably change that. We can easily do that by rotating our xticks before plotting:
```plt.xticks(rotation=40)```
- And now it will look perfect:
![Four Graphs](./part-1-numpy-matplotlib/assets/4graphs.png)

- We have done it! We now have four different graphs with various styles and data sets. Hopefully this servers as an example of literally just the tiniest 
  of possibilities with matplotlib, there is so, so, so much more! 
  
  
- Additionally, if you want to see the second demo I did during the workshop, where I go over some more graph beautifying with some *actual* data, check
  out our recording on the acm youtube channel! 
  - [Full recording will be in this playlist](https://www.youtube.com/playlist?list=PLPO7_kXilXFa1VwNhWRYGOokQORrIfi8G)
  - If you'd rather do it yourself, I have you covered! All of the code from that demo is already in this repository, in the part 1 folder. The csv data is
    there as well, but if you want to obtain it from it's source, here's some intructions on how to do so:
      - Go to the Google trends website, in the search box, type "spongebob" into the search trend box, press enter, then type "paw patrol" into the comparison
        box. 
      - Then, if you want (it doesn't really matter), select "Worldwide" for location and "2004-present" for time period (this is what I did). 
        - After that, you should be here: [spongebob vs paw patrol](https://trends.google.com/trends/explore?date=all&q=spongebob,paw%20patrol)
      - Then, click the arrow in the top right corner to download the data as a csv file. 
      - Move the file into a local project with your python file.
      - Make sure to delete the top two rows of the csv file, for some reason Google Trends adds them and it messes everything up. I just did so by opening
        up the file in a texteditor and manually deleting them. 
      - Then, you should be good to go! Check out the file "spongebob_vs_paw.py" in the part 1 folder for all of the code that creates the graph.
      - Here's a pretty awesome before-after:
![original graph](./part-1-numpy-matplotlib/assets/original-graph.png)
![Cooler Graph](./part-1-numpy-matplotlib/assets/cooler-graph.png)

## More Standard Libraries!
- Lets go ahead and look at some more useful standard libraries!
- [sys](#sys)
- [argparse](#argparse)

## sys
- The sys library provides various functions/variables used to manipulate the Python runtime environment/interpreter
- imported with ```import sys```
- [sys docs](https://docs.python.org/3/library/sys.html)


## argparse
- The argpase library is used for more ~sophisticated~ of processing command line arguments than sys.argv()
- imported with ```imported argparse```
- [argparse docs](https://docs.python.org/3/library/argparse.html)


## OpenCV 
- OpenCV is Python’s very own a computer vision library. It is a huge open-source library for all things computer vision, machine learning, and image processing. You can use it for generating images, analyzing images, and much more! 
- Many modern technologies you interact with everyday are powered by computer vision, and potentially OpenCV! This includes self driving cars, face detection software, and even tele-medicine!
- imported with ```import cv2 as cv```
- [cv docs](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)

### Reading in images
In order to actually play around with our beautiful images, we first have to read it into our program somehow. OpenCV provides just the command for that!
```
img = cv.imread('file/path/for/image.jpg')
```
We can see that this function takes in a single argument specifying the file path. Note that in OpenCV, images are just our classic numpy ndarrays. We can interact with them and play around with them just like we would with any other numpy array. The 3 dimensions of our image variable correspond to rows, columns, and number of channels. The channel number distinguishes RGB images (which has 3 channels) from single channel black and white images.
```
img.= cv.imread('file/path/for/image.jpg')
print(img.shape)
```
Here, if we print out the shape attribute of our image (which is an np.array), we might see something like "(512, 256, 3)".
This means that we have a 512 by 256 pixel RGB image on our hands.

### Viewing our image
Ok, so we have read in our image, done some fancy image processing on it, and now we want to see the fruits of our labour! In order to do so we must use OpenCV's image rendering command.
'''
cv.imshow("This is my image display title', img)
cv.waitKey(0)
cv.destroyAllWindows()
'''
The cv.imshow command is what actually displays the image, in a pop-up window. This function takes in two parameters: the name of the image display window, and the actual image np.array.
We also have two mysterous function calls below. The cv.waitKey(0) function serves to stall our program so that we can take our time to admire our image without worrying about the rest of the program executing and eventually terminating (thereby closing our python display window). This function will only resume execution when a key on the keyboard is pressed. The next function cv.destroyAllWindows() is just to clean up the clutter on our desktop by closing our image display window. This is especially useful when we are running a large program that involves lots of image displaying.

## OpenCV Demo Time: A professional meme deep fryer
We've seen all the alleged capabilities of OpenCV but lets actually get down and dirty and build something cool!
In this demo, our goal will be build a simple meme deep fryer. First, I'll give you a bit of background behind deep fried memes, that will help us in our openCV journey later. The first deep fried memes/images are satirizing the blurriness, low resolution, and high contrast of images/memes that are extensively reposted. Deep fried images are usually sharpened, red tinted, and contrasted to an absurdly high degree.
In this demo, we will mimic these effects, using the power of OpenCV!
First, lets go ahead and import the necessary libraries (please pip install these if you haven't already).
'''
import cv2 as cv
import numpy as np
'''
Then, we can read in our image using the cv.imread command we learned about earlier.
'''
src_img = cv.imread('./assets/bruhmoment.jpeg')
'''
This is what our sample image looks like.
![Bruh Momentum Image](./part-2-opencv/assets/bruhmoment.jpeg)

The first stage of our deep frying journey will be to dial the sharpness of our image up to 11.
'''
img = src_img.copy()
for i in range(10):
  frame = cv.GaussianBlur(img, (3,3), 13)
  img = cv.addWeighted(img, 1.5, frame, -0.5, 0)
'''
We have two main functions of interest in the code snippet above, that get the sharpening job done. 
The cv.GuassianBlur function, in effect rubs a (3,3) sized brush over our image img to blur it out. The third parameter dictates how much our blur decreases from the center versus the edges, but for the sake of the demo we can ignore it. 
The next function cv.addWeighted, subtracts out our blurred image from our original image, and stores it back into the same variable. Intuitively, this aligns with what we expect a sharpened image to be: a regular image minus the blurry portions! The math checks out. 
Then, we have a for loop that runs this piece of code 10 times where it uses the previous iterations output image as the input of the next iteration. This loop thoroughly sharpens our image into deep fried territory.

We then want to add a classic deep fried red hue to our image. We can do this through the following code snippet.
'''
contrast = 2.2
brightness = 50
b, g, r = cv.split(img)
r = r\*contrast + brightness
r = r.astype(np.uint8)
r = np.clip(r, 0, 255)
img = cv.merge((b, g, r))
'''
The general outline of this snippet is as follows. We split up our image using cv.split, into its three RGB channels. We do this, so that we can directly interact with only the red channel. Now to increase the contrast and brightness of the red in our image, we can simply scale it and shift it! Again, images are simply represented as np.arrays in OpenCV so we can directly mess around with the pixel values. We this cast our newly enhanced red image to an 8 bit integer (np.uint8). This is because OpenCV images come in two flavors: float values between 0 and 1, and integer values between 0 and 255. If we leave our image as float values between 0 and 255, then the our program won't work properly. Once we cast to int, we will clip the values in our array to only exist between 0 and 255 (since our scaling and shifting could have caused pixel values to exceed 255). Then, we merge the slices back into our img variable.

Finally, we will redden and bolden the edges in our image to add some extra deep-fried pizzaz.
'''
edges = cv.Canny(src_img, 50, 50)
red_edges = np.zeros(img.shape)
red_edges[:, :, 2] = edges
red_edges = red_edges.astype(np.uint8)
img = cv.addWeighted(img, 0.5, red_edges, 0.5, 0)
'''
We use OpenCV's Canny edge detection function to find out where the edges are in our source image. The two parameters after the img parameter, determine the Canny function's threshold for what constitutes an image. We then construct an RGB image (since the output of the Canny function is a single channel black and white image), and set the red slice to be the edges. We then use the cv.addWeighted function we encountered earlier to combine the red edges with our original image.

If we displayed our image now, we notice that it looks a bit dim. This is due to the addWeighted function where most of the image was black (except for the edges). To rectify this issue, we can just increase the contrast/brightness of our image with the following code.
'''
img = img\*1.5 + 50
img = img.astype(np.uint8)
'''
We're done deep frying our image! Let's take a look at our work of art.
![Deep Fried Image](./part-2-opencv/assets/deepfried.png)

## TensorFlow 
- TensorFlow is a python (and C++) machine learning library. It allows for (relatively) easy developing and training of ML models. Recently it has been integrated with Keras, which is a high-level neural network API, to make the library even easier to use.
- Machine learning at a very high level is a subfield of computer science which deals with computer programs that uses data to automatically detect patterns and improve itself. ACM AI provides wonderful workshops if you are intrigued and want to learn about ML and AI in more detail.
- imported with ```import tensorflow as tf```
- [tensorflow docs](https://www.tensorflow.org/tutorials)
- Tensors are the bread of TensorFlow
  -  Tensors are multi-dimensional arrays of elements that all have the same type
  -  The rank of a tensor is its dimensionality
- Flow is the butter of Tensorflow
  -  A dataflow graph can be used to display the workings of a TF program.
  -  Every edge in the graph is a Tensor, every node is an Operation, and the Tensors "flow" from one Operation to the next.
  -  Below, we see an example of one such tensorflow program, being represented as a graphic of tensors flowing
![TensorFlow](./part-1-tensorflow/assets/datflow.png)

## TensorFlow Demo

This is a very high level demo that illustrates an example of how machine learning can be used. We will be using the MNIST dataset of fashion/clothing to train and classify different types of clothing.
This demo is in the form of a Jupyter notebook.
1. Downlaod the jupyter notebook onto your computer
2. Run '''python3 -m IPython notebook''' on your terminal, from the directory containing the notebook file.
3. Navigate to the file in the browser window that just opened.
4. Open the file, and select "Run All"


Thank you so much!!
