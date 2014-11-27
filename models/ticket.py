from database import db


class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    birth_date = db.Column(db.Date)
    postal_code = db.Column(db.String(6))
    residence = db.Column(db.String(200))
    city = db.Column(db.String(200))
    price = db.Column(db.Float)
    purchase_date = db.Column(db.Date, nullable=False)
    visit_date = db.Column(db.Date)
    email = db.Column(db.String(200), nullable=False)
    paid = db.Column(db.Boolean, default=False)

    # def __init__(self, first_name, last_name, birth_date, postal_code, residence, price, _date):
    # self.first_name = first_name
    # self.last_name = last_name
    # self.birth_date = birth_date
    # self.postal_code = postal_code
    #     self.residence = residence
    #     self.price = price
    #     self._date = _date

    def __unicode__(self):
        return self.first_name + " " + self.last_name