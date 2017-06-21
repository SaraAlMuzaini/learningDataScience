# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#line plot
plt.plot(year, pop)

#scatterplot:
plt.scatter(x,y)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

#histogram bins is set to 10 as default if not specified
plt.hist(year, bins=5)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

#The following will create a scatterplot that has circles that have a size corresponding to the value of the datapoint
#pop is a list of values
plt.scatter(x,y, s = pop)

#Add grid
plt.grid(True)

#python is lazy so you have to tell it to show
plt.show()
