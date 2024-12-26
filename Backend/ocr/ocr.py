import pyocr
from PIL import Image
import pyocr.builders
import pyocr.tesseract
import cv2
import numpy as np
from matplotlib import cm


# Change TESSERACT path
pyocr.tesseract.TESSERACT_CMD = r"/usr/bin/tesseract"
tools = pyocr.get_available_tools()
tool = tools[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=6)


import pyocr
from PIL import Image
import pyocr.builders
import pyocr.tesseract
import cv2
import numpy as np
from matplotlib import cm

# Configure Tesseract
pyocr.tesseract.TESSERACT_CMD = r"/usr/bin/tesseract"
tools = pyocr.get_available_tools()
tool = tools[0]
builder = pyocr.builders.TextBuilder(tesseract_layout=4)  # Adjust layout as needed

def OCR(img, is_plain_document=False):
    def getText(img: Image):
        global tool
        return tool.image_to_string(img, lang="kor", builder=builder)

    def preprocess_image(img, is_plain_document):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        if is_plain_document:
            processed_img = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        else:
            gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=20)
            processed_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            processed_img = cv2.medianBlur(processed_img, 3)
        
        return processed_img

    processed_cv2_img = preprocess_image(img, is_plain_document)
    
    processed_img = Image.fromarray(processed_cv2_img)
    
    texts = getText(processed_img)

    text_list = [text.strip() for text in texts.strip().split("\n") if text.strip()]
    
    return text_list
