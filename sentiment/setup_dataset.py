"""Quotes dataset basics and stats."""

import kagglehub
import pandas as pd

path = kagglehub.dataset_download("manann/quotes-500k")
print("Path to dataset:", path)

df = pd.read_csv(path + '/quotes.csv')

# set column names
df.columns = ['Quote', 'Author', 'Tags']

# stats
print('')
print('Count: ' + str(len(df)))
print(str(df.dtypes))

# authors
authors = df.groupby(
    by = 'Author',
    as_index = False
).count().sort_values(
    by = 'Quote',
    ascending = False
)

print('\nAuthors')
print(authors)
print('--- Unique authors (mixed with book titles): ' + str(len(authors)))

# tags
tags = df['Tags'].str.split(',') # list of tags per row
exploded_tags = tags.explode() # one tag per row
unique_tags = exploded_tags.unique()
print('\nTags')
print(tags)
print('--- Unique tags: ' + str(len(unique_tags)))
