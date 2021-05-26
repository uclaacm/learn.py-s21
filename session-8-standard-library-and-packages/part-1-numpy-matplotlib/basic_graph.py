# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

import matplotlib.pyplot as plt
import numpy as np
import random
import math
from statistics import mean, median

plt.subplot(2, 2, 1)
x = np.arange(0.0, 2 * np.pi, .1)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Graph', y=.96, fontsize=9)

x = np.arange(0, 3 * np.pi, 0.1) 
y = [random.randrange(-10, 10) for i in range(0, len(x))]
plt.subplot(2, 2, 2)
plt.plot(x, y) 
plt.title('Random', y=.96, fontsize=9) 
   
# Set the second subplot as active, and make the second plot. 
plt.subplot(2, 2, 3) 
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--')
plt.plot(t, [math.pow(t, 2) for t in t], 'bs') 
plt.plot(t, [math.pow(t, 3) for t in t], 'g^')
plt.title('Cool Graph', y=.96, fontsize=9) 

plt.subplot(2, 2, 4) 
data1 = [random.randrange(0, 15) for i in range(1, 10)]
data2 = random.sample(range(0, 30), 10)
data3 = [random.randint(0, 60) for i in range(1, 10)]
x_axis = ['d1mean', 'd1med', 'd2mean', 'd2med', 'd3mean', 'd3med']
y_axis = [mean(data1), median(data1), mean(data2), median(data2), mean(data3), median(data3)]
plt.xticks(rotation=40)
plt.bar(x_axis, y_axis)
plt.title('Random Data', y=.96, fontsize=9)  
 
 
# Show the figure. 
plt.show()
