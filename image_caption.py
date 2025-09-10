import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
model.to(device)

def generate_caption(img: Image.Image) -> str:
    pixel_values = processor(images=img, return_tensors="pt").pixel_values.to(device)
    output_ids = model.generate(pixel_values, max_length=50, num_beams=4)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
