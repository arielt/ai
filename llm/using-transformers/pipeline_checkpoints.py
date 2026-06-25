import pprint

from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import pipeline

import torch

# print("\n --- Sentiment analysis")
# classifier = pipeline("sentiment-analysis")
# rv = classifier(
#     [
#         "I've been waiting for a HuggingFace course my whole life.",
#         "I hate this so much!",
#     ]
# )
# pprint.pprint(rv)


print("\n --- Checkpoint distilbert-base-uncased-finetuned-sst-2-english")
checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_pretrained(checkpoint)

raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
print("\n --- Raw inputs")
pprint.pprint(raw_inputs)


inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
print("\n --- Model inputs")
pprint.pprint(inputs)

print("\n --- Model outputs")
outputs = model(**inputs)
pprint.pprint(outputs.logits.shape)
pprint.pprint(outputs.logits)


print("\n --- Predictions")
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
pprint.pprint(predictions)
pprint.pprint(model.config.id2label)
