from transformers import pipeline
import pprint

print("\n --- Sentiment analysis")
inp = ["Transfomers library is awesome.", "I hate this so much!"]

classifier = pipeline("sentiment-analysis")
result = classifier(inp)

print("\n --- Input")
print(inp)
print("\n --- Result")
pprint.pprint(result)

## ------------------------------------------------------------------------- ##

print("\n --- Zero shot classification")
classifier = pipeline("zero-shot-classification")
result = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)
print("\n --- Result")
pprint.pprint(result)

## ------------------------------------------------------------------------- ##

print("\n --- Text generation")
generator = pipeline("text-generation")
result = generator("In this course, we will teach you how to")
print("\n --- Result")
pprint.pprint(result)

## ------------------------------------------------------------------------- ##

print("\n --- Text generation with the most compact model")
generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M")
result = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
)
print("\n --- Result")
pprint.pprint(result)

## ------------------------------------------------------------------------- ##

print("\n --- Mask filling")
unmasker = pipeline("fill-mask")
result = unmasker("This course will teach you all about <mask> models.", top_k=2)
print("\n --- Result")
pprint.pprint(result)
