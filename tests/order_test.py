__author__ = 'bob'

import unittest
from models.ticket import Ticket
from models.database import db
from controllers.ticket import TicketController
from controllers.barcode_generator import BarcodeGenerator


class CreateTicketTest(unittest.TestCase):
    def setUp(self):
        self.json = {}
        self.json['firstName'] = "test"
        self.json['lastName'] = "test"
        self.json['birthDate'] = "1995-01-30"
        self.json['email'] = "test@test.nl"
        self.json['zipCode'] = "3445 AG"
        self.json['residence'] = "Woerden"
        self.json['city'] = "Utrecht"
        self.ticket = None
        self.controller = TicketController()
        print "setting up"

    def tearDown(self):
        print "opruimen"

    def test_create_ticket(self):
        self.controller = TicketController()
        self.controller.create_ticket_from_json(self.json)
        #check if order is created
        self.ticket = Ticket.query.filter_by(ticket_id=self.controller.orders[0]).first()
        self.assertTrue(self.ticket, "order creation failed")

        #delete ticket
        self.controller.orders = []
        db.session.delete(self.ticket)
        db.session.commit()

    def test_get_information(self):
        self.controller = TicketController()
        self.controller.create_ticket_from_json(self.json)
        self.ticket = Ticket.query.filter_by(ticket_id=self.controller.orders[0]).first()
        self.assertTrue(self.ticket, "order creation failed")

        information = self.controller.get_ticket_information(self.ticket.ticket_id)
        #check if user information is available
        self.assertNotEqual(information['information'], "", "no user information")
        #check if the barcode exist
        self.assertNotEqual(information['barCode'], "", "no barCode")
        #delete ticket
        self.controller.orders = []
        db.session.delete(self.ticket)
        db.session.commit()


