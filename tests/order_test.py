__author__ = 'bob'

import unittest
from models.ticket import Ticket
from models.insured_artifacts import InsuredArtifacts
from models.database import db
from controllers.ticket import TicketController
from controllers.barcode_generator import BarcodeGenerator


class CreateTicketTest(unittest.TestCase):
    def setUp(self):
        #This is a json init variable its an empty dictionairy
        self.json = {}
        # set the json variable firstname to test
        self.json['firstName'] = "test"
        # set the json variable lastname to test
        self.json['lastName'] = "test"
        # set the json variable birthDate to 1995-01-30
        self.json['birthDate'] = "1995-01-30"
        # set the json variable email to test@test.nl
        self.json['email'] = "test@test.nl"
        # set the json variable zipCode to 3445 AG
        self.json['zipCode'] = "3445 AG"
        # set the json variable residence to Woerden
        self.json['residence'] = "Woerden"
        # set the json variable city to Utrecht
        self.json['city'] = "Utrecht"
        # create an empty ticket variable
        self.ticket = None
        # set the controller to the new TicketController()
        self.controller = TicketController()
        # show in the console that it's setting up the test
        print "setting up"

    def tearDown(self):
        print "opruimen"  # clean up print to show that the test ended

    def test_create_ticket(self):
        # create a ticket from the test json variable
        self.controller.create_ticket_from_json(self.json)
        # check if order is created
        # set the ticket to the first order result
        self.ticket = Ticket.query.filter_by(ticket_id=self.controller.orders[0]).first()
        # check if the ticket exist
        self.assertTrue(self.ticket, "order creation failed")
        #delete ticket
        self.controller.orders.remove(self.ticket.ticket_id)
        # remove order
        db.session.delete(self.ticket)
        db.session.commit()

    def test_get_information(self):
        #create ticket from test json variable
        self.controller.create_ticket_from_json(self.json)
        # set the ticket to the first order result
        self.ticket = Ticket.query.filter_by(ticket_id=self.controller.orders[0]).first()
        #check if the ticket exists
        self.assertTrue(self.ticket, "order creation failed")
        #retrieve order information json
        information = self.controller.get_ticket_information(self.ticket.ticket_id)
        # check if user information is available
        #check if the information is filled
        self.assertNotEqual(information['information'], "", "no user information")
        #check if the barcode exist
        self.assertNotEqual(information['barCode'], "", "no barCode")
        #delete test ticket
        self.controller.orders.remove(self.ticket.ticket_id)
        #remove the order
        db.session.delete(self.ticket)
        db.session.commit()


