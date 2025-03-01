# Sentiment analysis

## Quotes dataset
https://www.kaggle.com/datasets/manann/quotes-500k
```shell
python setup_dataset.py
```

```
Count: 499709
Quote     object
Author    object
Tags      object
dtype: object

Authors
                                                Author  Quote  Tags
31308                                  Debasish Mridha   6601  6601
67745                               Lailah Gifty Akita   5384  5384
105072                                  Sunday Adelaja   4911  4911
67750       Lailah Gifty Akita, Think Great: Be Great!   3059  3059
77173                                Matshona Dhliwayo   2258  2258
...                                                ...    ...   ...
47677                       Holly Smale, Sunny Side Up      1     1
47673   Holly Shumas, Five Things I Can't Live Without      1     1
47671                                  Holly Schindler      1     1
47666                                    Holly Pierlot      1     1
117295                                              티아      1     1

[117296 rows x 3 columns]
--- Unique authors (mixed with book titles): 117296

Tags
0         [attributed-no-source,  best,  life,  love,  m...
1         [dance,  heaven,  hurt,  inspirational,  life,...
2         [attributed-no-source,  dreams,  love,  realit...
3                  [friend,  friendship,  knowledge,  love]
4         [darkness,  drive-out,  hate,  inspirational, ...
                                ...                        
499704                             [Past,  Believe,  Help ]
499705                            [Team,  Humility,  Know ]
499706                                               [Now ]
499707                          [Life,  My Life,  Servant ]
499708                           [God,  Promises,  Bright ]
Name: Tags, Length: 499709, dtype: object
--- Unique tags: 175998
```

## TextBlob sentiment analysis
https://textblob.readthedocs.io/

Calculate sentiment analysis with TextBlob. The output file will be data/text-blob-sentiment.csv, containing Sentiment object and
separated out Polarity and Objectivity metrics. 

```shell
python calculate_text_blob.py
```

```shell
python text_blob_stats.py
```

```
Positive quotes: 79.25%
Objective quotes: 51.79%
```
