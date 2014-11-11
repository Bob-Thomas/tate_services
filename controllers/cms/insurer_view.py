from models.database import db
from models.insurer import Insurer
from flask.ext.admin.contrib.sqla import ModelView
from custom_filters import MyBobFilter
from flask.ext import login


class InsurerView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

    column_auto_select_related = True
    column_list = ('name', 'email', 'company')
