""" TextBlob sentiment analysis. """

import kagglehub
import pandas as pd
from tqdm import tqdm

from textblob import TextBlob

def calculate_sentiment(text):
    """Sentiment calculation."""
    return TextBlob(str(text)).sentiment

path = kagglehub.dataset_download("manann/quotes-500k")

df = pd.read_csv(path + '/quotes.csv')
# set column names
df.columns = ['Quote', 'Author', 'Tags']

tqdm.pandas()
df['Sentiment'] = df['Quote'].progress_apply(calculate_sentiment)

# save results
df.to_csv('./data/text-blob-sentiment.csv')
