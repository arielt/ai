# OCR

OCR (Optical Character Recognition) is a long-standing research problem. Existing approaches
are based on CNN (Convolutional Neural Network) for image understanding and RNN (Recurrent Neural Network)
for char-base processing.

[TrOCR](https://arxiv.org/abs/2109.10282) offers end-to-end text recognition approach with Transformer
archictecture for both image understanding and wordpiece-level text generation.

Good overview of TrOCR models: https://github.com/microsoft/unilm/blob/master/trocr/README.md

# Handwritten recognition

Script: ocr/trocr-handwritten.py

| Model | Model Size | Results |
| --- | :---: | :---: |
| [TrOCR Small Handwritten](https://huggingface.co/microsoft/trocr-small-handwritten/tree/main) | 246 MB | 1/3 |
| [TrOCR Base Handwritten](https://huggingface.co/microsoft/trocr-base-handwritten/tree/main) | 1.33 GB | 3/3 |
