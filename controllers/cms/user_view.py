from flask.ext.admin.contrib.sqla import ModelView
from wtforms import Form, BooleanField, StringField, validators, PasswordField
from flask.ext import login
from user_group_view import UserGroupsView
from models.user_groups import UserGroups
import login_role

class UserView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin'])
    column_auto_select_related = True
    column_list = ('first_name', 'last_name', 'email', 'activated', 'groups')
    column_searchable_list = ('first_name', 'last_name', 'email')
    column_filters = ('first_name', 'last_name', 'email', 'activated')
    form_columns = ('first_name', 'last_name', 'email', 'password', 'groups', 'activated')
    form_overrides = dict(first_name=StringField, last_name=StringField, email=StringField, password=PasswordField)