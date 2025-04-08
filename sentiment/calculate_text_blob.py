"""
Sentiment analysis with TextBlob.
"""

import kagglehub
import pandas as pd
from tqdm import tqdm

from textblob import TextBlob

def calculate_sentiment(columns: pd.DataFrame.columns) -> pd.DataFrame.columns:
    """
    Calculates sentiment, adding new columns to existing DataFrame columns.

    Args:
        columns: DataFrame columns.

    Returns:
        Updated dataframe columns.
    """
    quote = TextBlob(str(columns.Quote))
    columns['Sentiment'] = quote.sentiment
    columns['Polarity'] = quote.sentiment.polarity
    columns['Subjectivity'] = quote.sentiment.subjectivity
    return columns

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
