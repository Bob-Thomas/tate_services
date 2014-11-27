from database import db


class BlockedUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.ForeignKey('cashier.user_id', onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    cashier = db.relationship('Cashier')

    def __unicode__(self):
        return id