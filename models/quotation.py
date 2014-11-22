from database import db


class Quotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    information = db.Column(db.Text, nullable=False)
    artifact = db.Column(db.Integer, db.ForeignKey('artifact.id',
                                                   onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    request = db.Column(db.Integer, db.ForeignKey('request.id',
                                                  onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # def __init__(self, information=None, artifact=None):
    # self.information = information
    # self.artifact = artifact

    def __unicode__(self):
        return self.id