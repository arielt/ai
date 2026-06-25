from transformers import pipeline
import pprint

## ------------------------------------------------------------------------- ##

print("\n --- Named entity recognition")
ner = pipeline("ner", grouped_entities=True)
result = ner("My name is Ariel and I work at Pure in Santa Clara.")
print("\n --- Result")
pprint.pprint(result)

## ------------------------------------------------------------------------- ##

# https://huggingface.co/models

print("\n --- Named entity recognition POS model")
ner = pipeline(
    "ner", model="QCRI/bert-base-multilingual-cased-pos-english", grouped_entities=True
)
result = ner("My name is Ariel and I work at Pure in Santa Clara.")
print("\n --- Result")
pprint.pprint(result)
