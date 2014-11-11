from database import db
from models.artifact import Artifact
from sqlalchemy.event import listens_for


class InsuredArtifacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    insurer = db.Column(db.Integer, db.ForeignKey('insurer.id',
                                                    onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    artifact = db.Column(db.Integer, db.ForeignKey('artifact.id',
                                                   onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    insurers = db.relationship('Insurer')
    artifacts = db.relationship('Artifact')
    request_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __unicode__(self):
        return self.id
