from database import db


class Page(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    image = db.Column(db.String(200))

    def __unicode__(self):
        return self.name
