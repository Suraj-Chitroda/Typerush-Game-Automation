import pyscreenshot as psc #pip install pyscreenshot
import pytesseract #pip install pytesseract
import keyboard
import time

# Install Pytesseract according to your operating system and set your path
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def get_text():
	
	time.sleep(0.3)
	img = psc.grab(bbox=(320, 585, 950, 615)) #bbox = (x1, y1, x2, y2) 
	
	#save image to verify your cordinates
	#img.save('img/get.jpg')
	
	text = pytesseract.image_to_string(img)
	print(text)
	return text

def type(text):
	text += " "
	for x in text:
		time.sleep(.04)
		keyboard.write(x)

while True:
	print("GETTING TEXT")
	tt = get_text()
	if tt != "":
		print("Typing")
		type(tt)
	else:
		break	
print("TASK IS DONE")
