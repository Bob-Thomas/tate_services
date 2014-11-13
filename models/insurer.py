from database import db


class Insurer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    artifacts = db.relation('InsuredArtifacts')
    # def __init__(self, name=None, email=None):
    #     self.name = name
    #     self.email = email

    def __unicode__(self):
        return self.company
