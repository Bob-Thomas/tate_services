from database import db


class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    birth_date = db.Column(db.Integer)
    postal_code = db.Column(db.Text)
    residence = db.Column(db.Text)
    price = db.Column(db.Float)
    _date = db.Column(db.Integer)

    def __init__(self, first_name, last_name, birth_date, postal_code, residence, price, _date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.postal_code = postal_code
        self.residence = residence
        self.price = price
        self._date = _date