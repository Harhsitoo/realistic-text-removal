import os
import cv2
import pytesseract
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import platform

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    font_path = "C:\\Windows\\Fonts\\arial.ttf"
else:
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"

input_path = "IMG_4483.jpeg"
output_dir = "realistic_output"
os.makedirs(output_dir, exist_ok=True)

image = cv2.imread(input_path)
if image is None:
    print("❌ Failed to load image.")
    exit()

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
ocr_data = pytesseract.image_to_data(rgb_image, output_type=pytesseract.Output.DICT)

mask = np.zeros(image.shape[:2], dtype=np.uint8)
for i in range(len(ocr_data['text'])):
    try:
        if float(ocr_data['conf'][i]) > 60 and ocr_data['text'][i].strip():
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    except ValueError:
        continue

inpainted = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)
inpainted_path = os.path.join(output_dir, "inpainted_clean.jpg")
cv2.imwrite(inpainted_path, inpainted)

pil_image = Image.fromarray(cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_image)
font = ImageFont.truetype(font_path, 18)

for i in range(len(ocr_data['text'])):
    try:
        if float(ocr_data['conf'][i]) > 60 and ocr_data['text'][i].strip():
            text = ocr_data['text'][i]
            x, y = ocr_data['left'][i], ocr_data['top'][i]
            draw.text((x + 1, y + 1), text, font=font, fill=(0, 0, 0, 100))
            draw.text((x, y), text, font=font, fill=(0, 0, 0))
    except ValueError:
        continue

final_path = os.path.join(output_dir, "realistic_retextured.jpg")
pil_image.save(final_path)

print("✅ Done!")
print("🔹 Clean image without text:", inpainted_path)
print("🔹 Restored image with natural-looking text:", final_path)
