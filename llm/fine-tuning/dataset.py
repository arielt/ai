import pprint

from datasets import load_dataset

print("\n --- Load MRPC dataset")

raw_datasets = load_dataset("nyu-mll/glue", "mrpc")
pprint.pprint(raw_datasets)

raw_train_dataset = raw_datasets["train"]
pprint.pprint(raw_train_dataset.features)
pprint.pprint(raw_train_dataset[15])
pprint.pprint(raw_train_dataset[87])


print("\n --- Tokenize dataset")
from transformers import AutoTokenizer

checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
pprint.pprint(raw_datasets["train"]["sentence1"])

inputs = tokenizer("This is the first sentence.", "This is the second one.")
pprint.pprint(inputs)
pprint.pprint(tokenizer.convert_ids_to_tokens(inputs["input_ids"]))

# have to add list to raw datasets
tokenized_dataset = tokenizer(
    list(raw_datasets["train"]["sentence1"]),
    list(raw_datasets["train"]["sentence2"]),
    padding=True,
    truncation=True,
)

print("\n --- Apply tokenization function")


def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)


tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
pprint.pprint(tokenized_datasets)


print("\n --- Dynamic padding")

from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

samples = tokenized_datasets["train"][:8]
samples = {
    k: v for k, v in samples.items() if k not in ["idx", "sentence1", "sentence2"]
}
[len(x) for x in samples["input_ids"]]

batch = data_collator(samples)
{k: v.shape for k, v in batch.items()}
pprint.pprint(batch)
