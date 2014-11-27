from database import db


class Cashier(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    tries = db.Column(db.Integer, default=1)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_roles(self):
        roles = []
        for group in self.groups:
            roles.append(group.group.lower())
        return roles

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def __unicode__(self):
        return self.first_name + " " + self.last_name