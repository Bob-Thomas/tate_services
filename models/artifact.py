from database import db


class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    geological_period = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, nullable=False)
    insured = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name=None, reason=None, geological_period=None, image=None, value=None, insured=None):
        self.name = name
        self.reason = reason
        self.geological_period = geological_period
        self.image = image
        self.value = value
        self.insured = insured