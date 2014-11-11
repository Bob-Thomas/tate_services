from database import db
from werkzeug import security


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    groups = db.relationship('UserGroups', lazy='dynamic')
    activated = db.Column(db.Boolean)

        # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    # def __init__(self, email, password, firstname, lastname):
    #     self.email = email
    #     self.password = security.generate_password_hash(password, method='pbkdf2:sha256:2000', salt_length=8)
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.activated = False

    def check_password(self, password):
        return security.check_password_hash(self.password, password)

    def __unicode__(self):
        return self.first_name + " " + self.last_name