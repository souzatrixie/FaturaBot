from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

class OCREngine:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text_from_image(self, image_path):
        """Extrai texto de uma imagem usando OCR."""
        try:
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(f"Erro ao processar a imagem {image_path}: {e}")
            return None

    def extract_text_from_pdf(self, pdf_path):
        """Extrai texto de um PDF usando OCR."""
        try:
            images = convert_from_path(pdf_path)
            text = ''
            for image in images:
                text += pytesseract.image_to_string(image)
            return text
        except Exception as e:
            print(f"Erro ao processar o PDF {pdf_path}: {e}")
            return None

    def save_extracted_text(self, text, output_path):
        """Salva o texto extraído em um arquivo."""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
        except Exception as e:
            print(f"Erro ao salvar o texto em {output_path}: {e}")