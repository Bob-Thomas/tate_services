from controllers.loginLogger import LoginLogger
from models.cashier import Cashier
from models.cashier_login import CashierLogin
from models.blocked_user import BlockedUser
from models.database import db


class CashierController():
    #instaniate the logger
    logger = LoginLogger()

    def is_user_blocked(self):
        #checks if the user exist in the blocked users
        blocked = BlockedUser.query.filter_by(user=self.user.user_id).first()
        return blocked

    def block_user(self):
        if not BlockedUser.query.filter_by(user=self.user.user_id).first():
            #if the user logged in to much add it to the block
            db.session.add(BlockedUser(user=self.user.user_id))
            db.session.commit()

    def faulty_login(self):
        #if the user logs in with the wrong password write it to the log and add a strike to the account
        self.logger.write_to_log(self.user.email, "ONGELIDGE LOGIN")
        #check if the user isn't already in the blocked list
        if not BlockedUser.query.filter_by(user=self.user.user_id).first():
            print self.user.tries
            if self.user.tries >= 3:
                #if the user logged in to much add it to the block
                db.session.add(BlockedUser(user=self.user.user_id))
            #add a strike to the account
            self.user.tries += 1
            db.session.commit()

    def __init__(self, user):
        self.user = user