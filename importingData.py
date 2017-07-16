from urllib.request import urlretrieve
import requests json
import pandas as pd

# This retrieves a document not the data from a website
url = 'http://www.basketball-reference.com/players/e/embiijo01.html'
urlretrieve(url,'joel_embiid.csv')

#Read file into a DataFrame and print its head
df = pd.read_csv('joel_embiid.csv', sep=';')

#The following also works, don't need to save data locally either
# df = pd.read_csv(url, sep=';')
print df.head()



r = requests.get(url)
text = r.text

json_data = r.json()
