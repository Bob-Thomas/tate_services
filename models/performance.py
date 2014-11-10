from database import db


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    information = db.Column(db.Text, nullable=False)

    def __init__(self, name=None, information=None):
        self.name = name
        self.information = information