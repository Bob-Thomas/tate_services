from wtforms import form, fields, validators

from controllers.cashier_controller import CashierController
from models.cashier import Cashier
from models.cashier_login import CashierLogin
from models.database import db
from models.user import User


class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()
        print user
        if user['data'] is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if user['role'] is 'normal':
            if not user['data'].password == self.password.data:
                # to compare plain text passwords use
                # if user.password != self.password.data:
                raise validators.ValidationError('Invalid password')
        else:
            cashier_controller = CashierController(user['data'])
            login_information = CashierLogin.query.filter_by(cashier=user['data'].user_id).first()
            if cashier_controller.is_user_blocked() or user['data'].tries >= 3:
                raise validators.ValidationError("Dit acccount is geblokeerd")
            if not login_information.password == self.password.data:
                cashier_controller.faulty_login()
                raise validators.ValidationError(
                    'Ongeldig wachtwoord je mag nog ' + str(3 - user['data'].tries) + " keer proberen")

    def get_user(self):
        user = db.session.query(User).filter_by(email=self.login.data).first()
        if user:
            return {'role': 'normal', 'data': user}
        else:
            return {'role': 'cashier', 'data': db.session.query(Cashier).filter_by(email=self.login.data).first()}
