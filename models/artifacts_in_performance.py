from database import db


class ArtifactsInPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artifact = db.Column(db.Integer, db.ForeignKey('artifact.id',
                                                   onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    performance = db.Column(db.Integer, db.ForeignKey('performance.id',
                                                      onupdate='RESTRICT', ondelete='CASCADE'), nullable=False)
    performances = db.relationship('Performance')
    artifacts = db.relationship('Artifact')