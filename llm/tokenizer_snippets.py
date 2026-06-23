# https://huggingface.co/learn/llm-course/chapter2/4

import pprint

print("\n --- Tokenizer: split words")
tokenized_text = "Jim Henson was a puppeteer".split()
pprint.pprint(tokenized_text)


print("\n --- Tokenizer: BERT")
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
sequence = "Using a Transformer network is simple"

print("\n --- tokenizer")
rv = tokenizer(sequence)
pprint.pprint(rv)

print("\n --- tokens")
tokens = tokenizer.tokenize(sequence)
pprint.pprint(tokens)

print("\n --- ids")
ids = tokenizer.convert_tokens_to_ids(tokens)
pprint.pprint(ids)

# tokenizer.save_pretrained("tokenizer_folder")


print("\n --- Decoding")
decoded_string = tokenizer.decode([7993, 170, 11303, 1200, 2443, 1110, 3014])
pprint.pprint(decoded_string)
