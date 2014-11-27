import config

from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login
from flask.ext.admin.form import FileUploadField

import login_role


class PerformanceView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin', 'performancemaster'])

    column_auto_select_related = True

    form_overrides = {
        'image': FileUploadField
    }

    form_args = {
        'image': {
            'base_path': config.PERFORMANCE_PATH
        }
    }



