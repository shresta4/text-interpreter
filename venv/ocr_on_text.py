from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Shresta\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'

def get_text(img_path):
	converted_text = pytesseract.image_to_string(Image.open(img_path))
	return converted_text
#img_path = 'historytest.png'