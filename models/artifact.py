from os import path as op
import os

from sqlalchemy.event import listens_for

from database import db
import config


class Artifact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    geological_period = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Float, nullable=False)
    date_found = db.Column(db.Date)
    location_found = db.Column(db.String(200))
    insured = db.Column(db.Enum('YES', 'NO', 'PENDING'), default='NO')
    active = db.Column(db.Boolean, nullable=False, default=False)

    def __unicode__(self):
        return self.name


@listens_for(Artifact, 'after_delete')
def del_file(mapper, connection, target):
    if target.image:
        try:
            os.remove(op.join(config.ARTIFACT_PATH, target.image))
            os.remove(op.join(config.ARTIFACT_PATH, target.image[:3]+'_thumb,jpg'))
        except OSError:
            # Don't care if was not deleted because it does not exist
            pass