from database import db


class CashierLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cashier = db.Column(db.ForeignKey('cashier.user_id', onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    password = db.Column(db.String(2000), nullable=False)


    def __unicode__(self):
        return self.id