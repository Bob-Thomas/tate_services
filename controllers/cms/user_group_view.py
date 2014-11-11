from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login


class UserGroupsView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()

    column_auto_select_related = True
    column_filters = ('user', 'group')
    column_list = ('user', 'group')
    form_columns = ('user', 'group')