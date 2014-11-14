import qrcode
import time
import config
import hashlib


class BarcodeGenerator():
    date = time.strftime("%d-%m-%Y")
    name = None
    img = None
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    hasher = hashlib.md5()

    def __init__(self, order, name):
        self.name = config.QR_PATH + '\\' + name + "-" + self.date + "-" + str(order)
        self.hasher.update(name)
        self.hash = self.hasher.hexdigest()
        self.qr.add_data('http://tate.bmthomas.nl/ticket/'+str(self.hash) + "ebo" + str(order) + "la" + str(self.hash))
        self.img = self.qr.make_image()
        self.qr.clear()
        print self.img
        self.img.save(self.name+'.png')

    def get_file_name(self):
        return self.name

    def get_code(self):
        return str(self.hash)

    def get_base(self):
        with open(self.get_file_name()+".png", "rb") as f:
            data = f.read()
            return data.encode("base64")

