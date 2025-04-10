"""TextBlob stats."""

import pandas as pd

df = pd.read_csv("./data/text-blob-sentiment.csv")

total_count = len(df.Sentiment)

positive_count = (df.Polarity >= 0).sum()
objective_count = (df.Subjectivity < 0.5).sum()

positive_percentage = (positive_count / total_count) * 100
objective_percentage = (objective_count / total_count) * 100

print(f"Positive quotes: {positive_percentage:.2f}%")
print(f"Objective quotes: {objective_percentage:.2f}%")
