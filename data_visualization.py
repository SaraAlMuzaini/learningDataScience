import matplotlib.pyplot as plt

plt.style.use('ggplot')

# arrow will point to the location given by xy
# the text will appear at the location given by xytext
plt.annotate('setosa', xy=(5.0,3.5), xytext=(4.25,4.0), arrowprops={'color':'red'})


plt.show()

# seaborn is built on top of matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data is the Pandas DataFrame
tips = sns.load_dataset('tips')
#this plots a linear regression showing the 95% confidence interval
sns.lmplot(x='total_bill', y='tip', data=tips)
#For multiple categorical variables on the same graph: the hue argument specifies which categorical variable by which to group data observations
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palatte='Set1')

#Residuals:
sns.residplot(x='age', y='fare',data=tips,color='indianred')

#################################################################
### Univariate Distributions

#Strip plots
# Strip plot is a vertical representation, jitter will horizontally displace the points
sns.stripplot(x='day', y='tip', data=tip, size=4, jitter=True)

#Swarm plots
# Swarm plots automatically horizontally displace themselves so counts are easier to see
# orient ='h' makes plot horizontal. hue will change the colors of each plot according to the categorical variable used
sns.swarmplot(x='day', y='tip', data=tip, hue='sex', orient='h')

#With large sets of data, box plots and violin plots are better

#Combining violin plot and strip plots:
# argument inner set to None will disable the inner box plot in the violin plot
sns.violinplot(x='day', y='tip', data=tips, inner=None, color='lightgray')
sns.stripplot(x='day', y='tip', data=tips, size=4, jitte=True)


###################################################################
### Multivariate Distributions

#Joint plots are scatterplots with histograms on the far axis to further help visualize. Also comes with r value and p value
sns.jointplot(x='total_bill', y='tip', data=tips)
# Kind can be changed to change what kind of visual is use to display data. the following is like a filled contour map
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde') # kde = kernel density estimate

#Different kinds of joint plots:
# scatter - uses scatter plot
# reg - uses regression plot with default order 1
# ressid - uses a residual plot
# kde - uses a kernel density estimate
# hex - uses a hexbin plot

#Pair plot is a matrice of plots
# only uses numerical columns of the DataFrame - the only argument.
sns.pairplot(tips)

# Heatmaps are generally used to visualize covariance matrices for hundreds+ variables, like stocks
sns.heatmap(covariance)



sns.pairplot(tips, hue='sex')

plt.show()
