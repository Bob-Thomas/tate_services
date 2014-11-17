from flask import render_template
from mail_gun import mailer
from pdf import create_pdf
from controllers.ticket import TicketController


class Mail():

    ticket_controller = TicketController()

    def send_ticket(self, order):
        data = {}
        file_name = "order-" + str(int(order['information']['ticketId']))
        data['subject'] = "Order drawin museum - " + str(int(order['information']['ticketId']))
        data['receiver'] = order['information']['email']
        data['content'] = "Ticket zit in de pdf"
        path = create_pdf(render_template('ticket.html', order=order), file_name)
        mailer.send_simple_html_message(data, [path,])


