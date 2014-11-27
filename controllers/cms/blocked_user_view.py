from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login

from models.cashier import Cashier


class BlockedUserView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated() and 'admin' in login.current_user.get_roles()

    column_auto_select_related = True
    column_list = ('id', 'cashier')

    def on_model_delete(self, model):
        user = Cashier.query.filter_by(user_id=model.user).first()
        user.tries = 0


