#QR
import qrcode

data = input("Enter text or URL: ")

img = qrcode.make(data)
img.show()
