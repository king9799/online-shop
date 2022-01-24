from PIL import Image
from pytesseract import pytesseract


def img_to_text(image_path):
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    return text[:-1]

print(img_to_text(r'C:\d.jpg'))