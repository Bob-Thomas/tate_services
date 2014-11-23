from database import db


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    information = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    starting_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    # def __init__(self, name=None, information=None):
    # self.name = name
    # self.information = information

    def __unicode__(self):
        return self.name