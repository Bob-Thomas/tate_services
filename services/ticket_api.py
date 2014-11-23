from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, abort
from flask import Flask, request
import time
from controllers.barcode_generator import BarcodeGenerator
from models.database import db
from models.ticket import Ticket
from inflection import underscore
import re
from controllers.ticket import TicketController
from controllers.mail import Mail


class TicketApi(restful.Resource):

    parser = reqparse.RequestParser()

    ticket_controller = TicketController()

    mailer = Mail()

    def get(self, action=None, id=None):
        if action == 'order':
            tickets = []
            orders = self.ticket_controller.orders
            print orders
            for ticket in orders:
                tickets.append(self.ticket_controller.get_ticket_information(ticket))
                self.mailer.send_ticket(self.ticket_controller.get_ticket_information(ticket))
            self.ticket_controller.orders = []
            return tickets
        elif action == 'get':
            if id:
                ticket = Ticket.query.filter_by(ticket_id=id).first()
                if ticket:
                    return self.ticket_controller.get_ticket_information(ticket.ticket_id)
                else:
                    return "no ticket found"
            else:
                return "no id given"
        return abort(404)

    def post(self):
        form = request.get_json(force=True)
        for user in form['data']:
            del user['error']
            self.ticket_controller.create_ticket_from_json(user)
        return "whoopy"