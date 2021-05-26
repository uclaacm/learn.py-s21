import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
import datetime as datetime

import os

# importing the module
import csv

# creating empty lists
sponge_dates = []
sponge_scores = []
paw_dates = []
paw_scores = []
  
# open the file in read mode
with open('sponge_vs_paw.csv', 'r') as file:
    # iterating over each row and append
    # values to empty list
    csv_reader = csv.DictReader(file)
    for col in csv_reader:
        sponge_dates.append(col['Month'])
        sponge_scores.append((float)(col['spongebob: (Worldwide)']))
        paw_dates.append(col['Month'])
        if col['paw patrol: (Worldwide)'] == '<1':
            paw_scores.append(0)
        else:
            paw_scores.append((float)(col['paw patrol: (Worldwide)']))

# changing date strings to datetimes
for date in sponge_dates:
    date = datetime.datetime.strptime(date, '%Y-%m')

for date in paw_dates:
    date = datetime.datetime.strptime(date, '%Y-%m')

# changing ticks to every 12 and rotated 40 degrees
plt.xticks(np.arange(0, len(sponge_dates)+1, 12), rotation=40)

# plotting both lines
plt.plot_date(sponge_dates, sponge_scores, 'b-', xdate=True, ydate=False, color="gold", label="Spongebob", linewidth=2)
plt.plot_date(paw_dates, paw_scores, 'b-', xdate=True, ydate=False, color="blue", label="Paw Patrol", linewidth=2)

# adding margins, legend, title, axes labels, fill in color, grid, etc.
plt.margins(x=0)
plt.legend()
plt.title("Spongebob versus Paw Patrol Google Searches")
plt.ylabel("Relative Popularity Score Out of 100")
plt.xlabel("Date (Year-Month)")
plt.fill_between(sponge_dates, sponge_scores, color='yellow', alpha=.5)
plt.fill_between(paw_dates, paw_scores, color='teal', alpha=.5)
plt.grid()

# displaying graph
plt.show()