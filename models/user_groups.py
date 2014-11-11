from database import db


class UserGroups(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    group = db.Column(
        db.Enum('Admin', 'Cashier', 'PerformanceMaster', 'Room', 'Artifacts', 'Pages', 'Tickets', 'Manager'
                ), primary_key=True)
    user = db.relationship('User', backref=db.backref('usertogroups', lazy='dynamic'))

    def __unicode__(self):
        return self.group