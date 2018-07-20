import pyqrcode                         # pip install pyqrcode
from pyzbar.pyzbar import decode        # pip install pyzbar
from PIL import Image                   # pip install pillow
import re                               # pip install pypng


def createQR(pathToSave, imgName, qrText):
    q = pyqrcode.create(qrText)
    q.png(pathToSave + str(imgName) + ".png", scale=8)
    print('QR-code has been created')


def decodedQR(photo):
    x = decode(Image.open(photo))
    return re.findall(r'=b\'(.+?)\'', str(x[0]))
