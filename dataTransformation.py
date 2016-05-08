#more populated cities
import pandas as pd
import random
import numpy as np
more_populated_cities=['New York', 'Los Angeles','Chicago','Houston','Philadelphia',\
 'Phoenix','San Antonio','San Diego', 'Dallas', 'San Jose']


#less populated cities
less_populated_cities=['Monowi', 'Centralia', 'Lost Springs', 'Tortilla Flat', 'Picher', \
'Tenney', 'Weeki Wachee', 'Buford', 'Freeport']

destructiveness_df=pd.read_csv("/Users/anupdudani/Documents/NaturalCalamity/destructiveNessOfEarthQuakeUpdated.csv")

destructiveness_df['City'] = np.where(destructiveness_df['Population'] == 'Populated', more_populated_cities[random.randint(0,9)], less_populated_cities[random.randint(0,8)])

"""
	for ele in more_populated_cities:
		destructiveness_df['City']=ele
elif destructiveness_df['Population']=='Unpopulated':
	for ele in less_populated_cities:
		destructiveness_df['City']=ele
"""
print destructiveness_df.head()
print destructiveness_df.tail()
print destructiveness_df

destructiveness_df.to_csv("updated.csv")

