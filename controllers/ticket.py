from flask import jsonify
from controllers.barcode_generator import BarcodeGenerator
from models.database import db
from models.ticket import Ticket
import re
import time

class TicketController():

    barcode = None

    orders = []

    def create_ticket_from_json(self, json=None):
            birth_date = str(time.strptime(json['birthDate'], "%Y-%m-%d")[:3])
            birth_date = re.sub(',\s', '-', birth_date)
            birth_date = re.sub('(\(|\))', '', birth_date)
            ticket = Ticket()
            ticket.first_name = json['firstName']
            ticket.last_name = json['lastName']
            ticket.birth_date = birth_date
            ticket.email = json['email']
            ticket.postal_code = json['zipCode'].replace(' ', '')
            ticket.residence = json['residence']
            ticket.city = json['city']
            ticket.purchase_date = time.strftime("%Y-%m-%d")
            ticket.paid = True
            db.session.add(ticket)
            db.session.commit()
            self.orders.append(ticket.ticket_id)

    def get_ticket_information(self, order_id):
        ticket = Ticket.query.filter_by(ticket_id=order_id).first()
        self.barcode = BarcodeGenerator(ticket.ticket_id, ticket.first_name + "-" + ticket.last_name)
        information = {}
        if ticket:
            information['barCode'] = self.barcode.get_base()
            information['information'] = self.create_json_from_ticket(ticket)
        self.barcode = None
        self.orders.pop(self.orders.index(order_id))
        return information

    def create_json_from_ticket(self, ticket):
        json = {}
        json['firstName'] = ticket.first_name
        json['lastName'] = ticket.last_name
        json['birthDate'] = ticket.birth_date.strftime("%d-%m-%Y")
        json['email'] = ticket.email
        json['zipCode'] = ticket.postal_code
        json['residence'] = ticket.residence
        json['city'] = ticket.city
        json['purchaseDate'] = ticket.purchase_date.strftime("%Y-%m-%d")
        json['ticketId'] = ticket.ticket_id
        json['age'] = int(time.strftime("%Y")) - int(ticket.birth_date.strftime("%Y"))

        return json

    def __init__(self):
        print "wee"