'''
    File: hw1_LoganBowers.py
    Author: Logan Bowers
    NetID: lbower10
    Class: COSC 370
    Date: 7/9/23
'''

from numpy import arange
import matplotlib.pyplot as plt

xData = arange(1,32)    # Ranges for x and y axes must match
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]

# CALCULATE A RUNNING MONTHLY AVERAGE AND PRINT IT OUT IN A TABLE
avg = [86.]
for i in range(2, len(tData) + 1):
    daily_average = sum(tData[:i]) / i # calculate avg up to current index / # items so far
    avg.append(daily_average)

print("Day\t\tMonthly Average\n--------------------------------")
for i, avg_temp in enumerate(avg):
    print(f"August {i + 1}\t\t{avg_temp:.2f}")

# PLOT RED POINTS WITH BLUE LINE & SHOW CHANGE IN AVERAGE HIGH WITH GREEN DASHED LINE
plt.plot(xData, tData, 'ro')
plt.plot(xData, tData, 'blue', linestyle='-')
plt.plot(xData, avg, 'g--')

# SET DISPLAY RANGES FOR X AND Y AXES
plt.xlim(0, 32)
plt.ylim(70, 95)

plt.grid(True, linestyle='dashed')  # ENABLE GRID DISPLAY

# LABEL AXES AND SET TITLE
plt.xlabel('Day')
plt.ylabel('High Temp')
plt.title('High Temperatures for Knoxville, TN - August 2013')

plt.text(15, 86, 'Monthly Avg', color='g')  # LABEL THE MONTHLY AVERAGE LINE
plt.show()