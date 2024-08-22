#final_ocr.py
import cv2
from PIL import Image
import pytesseract

def extract_text_from_scene(image_path):
# def extract_text_from_scene():
    image_path = '/home/austine/Desktop/final_proj/captured_image.jpg'

    try:
        img = cv2.imread(image_path)
        if img is None:
            raise Exception("Error: Unable to load the image. Check if the file exists and is a valid image.")

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresholded_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        extracted_text = pytesseract.image_to_string(
            Image.fromarray(thresholded_img),
            lang='eng',
            config='--psm 3 --oem 3'
        )
        print(extracted_text.strip())
        return extracted_text.strip()
    except Exception as e:
        return str(e)
    
# if __name__ == "__main__":
#     extract_text_from_scene()
