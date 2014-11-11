from database import db


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # def __init__(self, name=None, content=None):
    #     self.name = name
    #     self.content = content

    def __unicode__(self):
        return self.name