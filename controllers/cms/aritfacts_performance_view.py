from flask.ext.admin.contrib.sqla import ModelView

from flask.ext import login

import login_role


class ArtifactsInPerformanceView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin', 'performancemaster'])

    column_auto_select_related = True

