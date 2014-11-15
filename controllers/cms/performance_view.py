from flask import url_for
from flask.ext.admin.contrib.sqla import ModelView
from markupsafe import Markup
from models.database import db
from models.artifact import Artifact
from models.performance import Performance
from models.artifacts_in_performance import ArtifactsInPerformance
from flask.ext.admin.actions import action
from flask.ext import login
import login_role


class PerformanceView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin', 'performancemaster'])

    column_auto_select_related = True

