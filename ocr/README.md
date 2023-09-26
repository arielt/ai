# OCR

OCR (Optical Character Recognition) is a long-standing research problem. Existing approaches
are based on CNN (Convolutional Neural Network) for image understanding and RNN (Recurrent Neural Network)
for char-base processing.

[TrOCR](https://arxiv.org/abs/2109.10282) offers end-to-end text recognition approach with Transformer
archictecture for both image understanding and wordpiece-level text generation.

Good overview of TrOCR models: https://github.com/microsoft/unilm/blob/master/trocr/README.md

# Handwritten recognition
```
python ocr/trocr-handwritten.py
```

| Model | Model Size | Results |
| --- | :---: | :---: |
| [TrOCR Small Handwritten](https://huggingface.co/microsoft/trocr-small-handwritten/tree/main) | 246 MB | 1/3 |
| [TrOCR Base Handwritten](https://huggingface.co/microsoft/trocr-base-handwritten/tree/main) | 1.33 GB | 3/3 |

# Printed recognition
```
python ocr/trocr-printed.py
```

| Model | Model Size | Results |
| --- | :---: | :---: |
| [TrOCR Base Printed](https://huggingface.co/microsoft/trocr-base-printed/tree/main) | 1.33 GB | TBD |

# Image preparation
```
python ocr/split-image.py
```

Rotate tilted image, find lines, split to one-line images.

# Tesseract

[Tesseract requires MacPorts to be installed on M1 silicon](https://sammybams.hashnode.dev/how-to-install-tesseract-ocr-on-macos).
```
sudo port install tesseract-eng
sudo port install tesseract-deu # German

python ocr/tesseract-deu.py # german receipt experiment
```

# Receipt scanner
```
python ocr/scan-receipt.py --debug --image ocr/img/safeway2.png
```

# References
  - [SROIE Dataset](https://www.kaggle.com/datasets/urbikn/sroie-datasetv2)
  - [OpenCV: split text lines in a scanned document](https://stackoverflow.com/questions/34981144/split-text-lines-in-scanned-document)
  - [OpenCV: save splitted text lines](https://stackoverflow.com/questions/67991036/save-splited-text-lines-opencv)
  - [Image segmentation](https://www.kaggle.com/code/dmitryyemelyanov/receipt-ocr-part-1-image-segmentation-by-opencv) 
- [Tesseract](https://pyimagesearch.com/2021/10/27/automatically-ocring-receipts-and-scans/)
- [Tesseract - German](https://nanonets.com/blog/receipt-ocr/)
