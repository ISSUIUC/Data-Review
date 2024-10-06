import pandas as pd
import matplotlib.pyplot as plt
"""
import given csv
figure out what we are graphing(some sort of x axis(time?), at least one but potentially
multiple data streams

ideally can do mutliple different plots
on each we need std deviation, best fit lines, some  sort of  ability to define rules
RULES = over certain time frame either data always within(greaterthan/equal to/less than)some thresholld
OR data always fufills some relationship to the next data OR some maximal std  deviation
Need to be able  to define multiple  rules
If rule broken, specifiy which rule broken and where(time wise)

show which csv currently operating on, be able to change out and in(maybe)
"""

#RULE FORMAT
#THRESHOLD
#TH(indicator) T1 - T2(Timestamp 1 to timestamp 2) - could be 0-END x < p1(some value,potentially NA)x > p2(same) x = p3(same)
data = pd.read_csv('')
x, y = data['Time'], data['Thrust']
plt.plot(x,y)


