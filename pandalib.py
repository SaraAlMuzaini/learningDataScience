import pandas as pd

dict = {"Name":["Aaron", "Bobby", "Chad", "David"], "Age":[12,13,14,15]}
#the following takes a dictionary and turns it into a rectangular data set, or dataframe
friends = pd.DataFrame(dict)

#panda can also import data from a csv file
friends = pd.read_csv("file/path")

#to tell panda that the first column contains the row labels:
friends = pd.read_csv("file/path", index_col = 0)
#or, alrenatively:
friends.index = row_labels
