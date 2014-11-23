import platform
import time
import hashlib

import qrcode

import config
from models.ticket import Ticket


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
    linux = 'linux' == platform.system().lower()

    def __init__(self, order, name):
        self.name = config.QR_PATH + config.DIVIDER + name + "-" + self.date + "-" + str(order)
        self.hasher.update(str(order))
        self.hash = self.hasher.hexdigest()
        self.qr.add_data(
            'http://tate.bmthomas.nl/ticket/' + str(self.hash))
        self.img = self.qr.make_image()
        print self.img
        self.img.save(self.name + '.png')
        self.qr.clear()

    def get_file_name(self):
        return self.name

    def get_code(self):
        return str(self.hash)

    def get_base(self):
        with open(self.get_file_name() + ".png", "rb") as f:
            data = f.read()
            return data.encode("base64")

    @staticmethod
    def get_bar_code(ticket_id):
        ticket = Ticket.query.filter_by(ticket_id=ticket_id).first()
        if ticket:
            name = ticket.first_name + "-" + ticket.last_name
            file_name = config.QR_PATH + config.DIVIDER + name + "-" + ticket.purchase_date.strftime(
                "%d-%m-%Y") + "-" + str(ticket.ticket_id)
            with open(file_name + ".png", "rb") as f:
                data = f.read()
                return data.encode("base64")
        else:
            return "no ticket found"

