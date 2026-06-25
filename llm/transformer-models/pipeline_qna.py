from transformers import pipeline
import pprint

## ------------------------------------------------------------------------- ##

from transformers import pipeline

print("\n --- Question answering")
question_answerer = pipeline("question-answering")
result = question_answerer(
    question="Where do I work?",
    context="My name is Ariel and I work at Pure in Santa Clara.",
)
print("\n --- Result")
pprint.pprint(result)
