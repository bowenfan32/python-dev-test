"""
Using pandas:
    - load the CSV file specified by CSV_FILE
    - using the data in the file, create a plot where 
        - the x axis is time (ascending)
        - the y axis is the number of daily infections (per age group)
    - save the plot to the file "part_2_3.png"

You don't need to get fancy with labelling plot axes or adding titles or anything like that.
If you cannot figure out how to do all of this, then plot something else.
"""
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "data/report_2_3.csv"

# Your code goes here
df = pd.read_csv('data/report_2_3.csv')

group_1 = df.loc[df['age'] == 0]
x1 = group_1['time']
y1 = group_1['daily_infections']
plt.plot(x1, y1, label="age 0")

group_2 = df.loc[df['age'] == 15]
x2 = group_2['time']
y2 = group_2['daily_infections']
plt.plot(x2, y2, label="age 15")

group_3 = df.loc[df['age'] == 30]
x3 = group_3['time']
y3 = group_3['daily_infections']
plt.plot(x3, y3, label="age 30")

group_4 = df.loc[df['age'] == 45]
x4 = group_4['time']
y4 = group_4['daily_infections']
plt.plot(x4, y4, label="age 45")

plt.savefig('part_2_3.png')
plt.show()
