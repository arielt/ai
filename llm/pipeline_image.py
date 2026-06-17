from transformers import pipeline
import pprint

## ------------------------------------------------------------------------- ##

from transformers import pipeline

print("\n --- Image classification")

image_classifier = pipeline(
    task="image-classification", model="google/vit-base-patch16-224"
)
result = image_classifier(
    "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/pipeline-cat-chonk.jpeg"
)

print("\n --- Result")
pprint.pprint(result)
