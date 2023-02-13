import pytesseract
import sys
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

if sys.argv > 1:
    print("drag and drop the image file on to this file")
else:
    droppedFile = sys.argv[1]
    text = pytesseract.image_to_string(droppedFile)
    if text == "":
        print("No text was found in this image")
    else:
        print(text)
        pyperclip.copy(text)
        print("sucsessfuly copied image text")


input("Press Enter to continue...")