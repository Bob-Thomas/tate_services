from database import db


class Agreement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    information = db.Column(db.Text, nullable=False)

    quotation = db.Column(db.Integer, db.ForeignKey('quotation.id', onupdate='RESTRICT', ondelete='CASCADE'),
                          nullable=False)

    request = db.Column(db.Integer, db.ForeignKey('request.id', onupdate='RESTRICT', ondelete='CASCADE'),
                        nullable=False)

    artifact = db.Column(db.Integer, db.ForeignKey('artifact.id',
                                                   onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    insurer = db.Column(db.Integer, db.ForeignKey('insurer.id', onupdate='RESTRICT', ondelete='CASCADE'),
                        nullable=False)
    price = db.Column(db.Float, nullable=False)

    # def __init__(self, information=None, artifact=None, price=None):
    # self.information = information
    # self.artifact = artifact
    # self.price = price

    def __unicode__(self):
        return self.id