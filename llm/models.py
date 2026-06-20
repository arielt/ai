# https://huggingface.co/learn/llm-course/chapter2/3

import pprint
import torch

from transformers import AutoModel
from transformers import AutoTokenizer

# model
model = AutoModel.from_pretrained("bert-base-cased")

print("\n --- Tokenizer")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
encoded_input = tokenizer("Hello, I'm a single sentence!")
pprint.pprint(encoded_input)

print("\n --- Decode")
pprint.pprint(tokenizer.decode(encoded_input["input_ids"]))

print("\n --- Encode multiple sentences with tensors")
encoded_input = tokenizer(
    ["How are you?", "I'm fine, thank you!"], padding=True, return_tensors="pt"
)
pprint.pprint(encoded_input)

print("\n --- Truncate input")
encoded_input = tokenizer(
    "This is a very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long sentence.",
    truncation=True,
)
pprint.pprint(encoded_input["input_ids"])

print("\n --- Truncate and pad")
encoded_input = tokenizer(
    ["How are you?", "I'm fine, thank you!"],
    padding=True,
    truncation=True,
    max_length=5,
    return_tensors="pt",
)
pprint.pprint(encoded_input)

print("\n --- Tensors to models")
sequences = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
encoded_input = tokenizer(
    sequences,
    padding=True,
    truncation=True,
    max_length=5,
    return_tensors="pt",
)
pprint.pprint(encoded_input)

model_inputs = torch.tensor(encoded_input["input_ids"])
output = model(model_inputs)
pprint.pprint(output)
