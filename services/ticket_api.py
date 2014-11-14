from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from flask import Flask, request
import time
from models.database import db
from models.ticket import Ticket
from inflection import underscore
import re
from controllers.ticket import TicketController


class TicketApi(restful.Resource):

    parser = reqparse.RequestParser()

    ticket_controller = TicketController()

    def get(self):
        tickets = []
        print self.ticket_controller.orders
        for ticket in self.ticket_controller.orders:
            print ticket
            tickets.append(self.ticket_controller.get_ticket_information(ticket))
        return tickets

    def post(self):
        self.ticket_controller = TicketController()
        form = request.get_json(force=True)
        for user in form['data']:
            del user['error']
            self.ticket_controller.create_ticket_from_json(user)
        print form['data']


        return "whoopy"