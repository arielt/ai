import requests
from PIL import Image

urls = ['https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoolxi9yWGAT5SLZShv8vVd0bz47UWRzQC19fDTeE8GmGv_Rn-PCF1pP1rrUx8kOjA4gg&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNYtTuSBpZPV_nkBYPMFwVVD9asZOPgHww4epu9EqWgDmXW--sE2o8og40ZfDGo87j5w&usqp=CAU']

expected = ['industry, " Mr. Brown commented icily. " Let us have a',
            'Hope you have done it.',
            '" Will you pour your own, please, and'
]

images = []
for url in urls:
    images.append(Image.open(requests.get(url, stream=True).raw).convert("RGB"))

print('--- preparing processor')
from transformers import TrOCRProcessor
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")

print('--- loading model')
from transformers import VisionEncoderDecoderModel
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def process_image(image):
    # prepare image
    pixel_values = processor(image, return_tensors="pt").pixel_values

    # generate (no beam search)
    generated_ids = model.generate(pixel_values)

    # decode
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text

def smile_comp(a,b):
    if a == b:
        return "\U0001F642"
    else:
        return "\U0001F610"

for idx, img in enumerate(images):
    generated_text = process_image(img)
    print("{}. Recognized: {} {}".format(idx + 1, generated_text,  smile_comp(generated_text, expected[idx])))
