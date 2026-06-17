from transformers import pipeline
import pprint

## ------------------------------------------------------------------------- ##

from transformers import pipeline

print("\n --- Translation")
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
result = translator("Ce cours est produit par Hugging Face.")

print("\n --- Result")
pprint.pprint(result)
