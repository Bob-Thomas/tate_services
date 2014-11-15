from flask.ext.admin.contrib.sqla import ModelView
from wtforms import Form, BooleanField, StringField, validators, PasswordField, SelectField
from flask.ext import login
import login_role
import time

class TicketView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin', 'cashier'])

    column_auto_select_related = True
    column_list = ('first_name', 'last_name', 'email', 'purchase_date', 'city')
    column_searchable_list = ('first_name', 'last_name', 'email')
    column_filters = ('first_name', 'last_name', 'email', 'purchase_date', 'residence', 'city', 'visit_date')
    form_excluded_columns = ('first_name', 'last_name', 'birth_date')
    form_args = {
        'postal_code': {
            'default': "3445 AG"
        },
        'residence': {
            'default': 'Woerden'
        },
        'city': {
            'default': "Utrecht"
        },
        'purchase_date': {
            'default': time
        },
        'visit_date': {
            'default': time
        },
        'email': {
            'default': 'tate-cashier@tate.com'
        }
    }
