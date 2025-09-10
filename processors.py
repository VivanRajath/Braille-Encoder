# pdf_processor.py
import pdfplumber
from PIL import Image
from image_caption import generate_caption

def process_pdf(pdf_path: str) -> str:
    output = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Extract text
            text = page.extract_text()
            if text:
                output += f"\n--- Page {page_num} ---\n{text}\n"

            # Extract images
            for img in page.images:
                try:
                    x0, y0, x1, y1 = img["x0"], img["y0"], img["x1"], img["y1"]
                    pil_img = page.crop((x0, y0, x1, y1)).to_image(resolution=150).original
                    caption = generate_caption(pil_img)
                    output += f"[Image: {caption}]\n"
                except:
                    continue
    return output.strip()
