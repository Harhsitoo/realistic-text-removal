# Realistic Text Removal & Restoration

A cross-platform Python script that removes embedded text from images using AI-powered inpainting, and then re-adds the text in a natural-looking way.

## 🔧 Features
- Detects text using Tesseract OCR
- Masks and inpaints text areas to look untouched
- Rewrites the original text naturally using PIL
- Works on both macOS and Windows

## 🖥 Requirements
- Python 3.8+
- Tesseract OCR
  - macOS: `/opt/homebrew/bin/tesseract`
  - Windows: `C:\Program Files\Tesseract-OCR\tesseract.exe`

## 📦 Installation
```bash
git clone https://github.com/YOUR_USERNAME/realistic-text-removal.git
cd realistic-text-removal
pip install -r requirements.txt
```

## 🚀 Usage
Place your input image in the folder and rename it to `IMG_4483.jpeg`, or modify the path in the script:

```bash
python realistic_text_removal.py
```

Output will be saved to the `realistic_output/` folder:
- `inpainted_clean.jpg`: object with no text
- `realistic_retextured.jpg`: cleanly restored version

## 🙌 Author
Made by Harshit — feel free to fork and enhance!
