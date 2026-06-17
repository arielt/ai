from transformers import pipeline
import pprint

## ------------------------------------------------------------------------- ##

from transformers import pipeline

print("\n --- Speech recognition")

transcriber = pipeline(
    task="automatic-speech-recognition", model="openai/whisper-large-v3"
)
result = transcriber(
    "https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"
)

print("\n --- Result")
pprint.pprint(result)
