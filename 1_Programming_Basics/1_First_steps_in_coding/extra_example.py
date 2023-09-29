import pyqrcode
import png
from pyqrcode import QRCode

adress = 'https://yourdailygerman.com/'
url = pyqrcode.create(adress)
url.png('german.png', scale=8)
