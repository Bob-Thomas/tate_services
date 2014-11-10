from database import db


class InsuredArtifacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artifact = db.Column(db.Integer, db.ForeignKey('artifact.id',
                                                   onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    insurance = db.Column(db.Integer, db.ForeignKey('insurance.id',
                                                      onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)