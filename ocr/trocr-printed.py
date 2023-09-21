from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image


print('--- loading image')
path = './img/printed_1.png'
print(path)
image = Image.open(path).convert("RGB")

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')

print('--- prepare image')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

print('--- generate and decode')
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print('--- results')
print(generated_text)


