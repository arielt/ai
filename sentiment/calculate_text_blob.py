""" TextBlob sentiment analysis. """

import kagglehub
import pandas as pd
from tqdm import tqdm

from textblob import TextBlob

def calculate_sentiment(s):
    """Sentiment calculation."""
    tb = TextBlob(str(s.Quote))
    s['Sentiment'] = tb.sentiment
    s['Polarity'] = tb.sentiment.polarity
    s['Subjectivity'] = tb.sentiment.subjectivity
    return s

path = kagglehub.dataset_download("manann/quotes-500k")

df = pd.read_csv(path + '/quotes.csv')
# set column names
df.columns = ['Quote', 'Author', 'Tags']

tqdm.pandas()
df_out = df.progress_apply(calculate_sentiment, axis=1)

# for testing, use subset
# df_out = df.iloc[:5].progress_apply(calculate_sentiment, axis=1)

# save results
df_out.to_csv('./data/text-blob-sentiment.csv')
