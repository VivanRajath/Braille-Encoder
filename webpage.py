
import requests, io
from bs4 import BeautifulSoup
from PIL import Image
from image_caption import generate_caption

def process_webpage(url: str) -> str:
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    output = ""

    for elem in soup.find_all(["p","h1","h2","h3","img"]):
        if elem.name == "img" and elem.get("src"):
            try:
                img_url = elem["src"]
                if not img_url.startswith("http"):
                    img_url = requests.compat.urljoin(url, img_url)
                img = Image.open(io.BytesIO(requests.get(img_url).content)).convert("RGB")
                caption = generate_caption(img)
                output += f"[Image: {caption}]\n"
            except:
                continue
        else:
            text = elem.get_text().strip()
            if text:
                output += text + "\n"
    return output.strip()
