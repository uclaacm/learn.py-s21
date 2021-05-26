# Brief demo of timeit 
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

import matplotlib.pyplot as plt
import numpy as np
import random
import math
from statistics import mean, median

# Set the first subplot of 4 as active
plt.subplot(2, 2, 1)
# generaate a range between 0 and 2pi, with steps of .2
x = np.arange(0.0, 2 * np.pi, .1)
# y = sin of x
y = np.sin(x)
# plot x and y and add graph title
plt.plot(x, y)
plt.title('Sine Graph', y=.96, fontsize=9)

# Set the second subplot of 4 as active
plt.subplot(2, 2, 2)
# generate a range between 0 and 3pi, with steps of .1
x = np.arange(0, 3 * np.pi, 0.1) 
# generate a random y value between -10 and 10 for each x value
y = [random.randrange(-10, 10) for i in range(0, len(x))]
# plot x and y and add graph title
plt.plot(x, y) 
plt.title('Random', y=.96, fontsize=9) 
   
# Set the third subplot as active
plt.subplot(2, 2, 3) 
# generate a range between 0 and 5, with steps of .2
t = np.arange(0., 5., 0.2)
# plot y = x, y = x^2, and y = x^3, add graph title
plt.plot(t, t, 'r--')
plt.plot(t, [math.pow(t, 2) for t in t], 'bs') 
plt.plot(t, [math.pow(t, 3) for t in t], 'g^')
plt.title('Cool Graph', y=.96, fontsize=9) 

# Set the fourth subplot as active
plt.subplot(2, 2, 4) 
# generate 3 sets of random data, each with different ranges
data1 = [random.randrange(0, 15) for i in range(1, 10)]
data2 = random.sample(range(0, 30), 10)
data3 = [random.randint(0, 60) for i in range(1, 10)]
# set the bar titles
x_axis = ['d1mean', 'd1med', 'd2mean', 'd2med', 'd3mean', 'd3med']
# set the y value of each bar
y_axis = [mean(data1), median(data1), mean(data2), median(data2), mean(data3), median(data3)]
# rotate xticks so they don't overlap
plt.xticks(rotation=40)
# plot x and y and add graph title
plt.bar(x_axis, y_axis)
plt.title('Random Data', y=.96, fontsize=9)  
 
 
# Show the figure. 
plt.show()

