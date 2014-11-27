from flask.ext.admin.contrib.sqla import ModelView
from flask.ext import login

import login_role
from models.artifact import Artifact
from models.database import db


class ArtifactsInPerformanceView(ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated() and login_role.check_roles(['admin', 'performancemaster'])

    column_auto_select_related = True


    def on_model_change(self, form, model, is_created):
        if is_created:
            artifact = Artifact.query.filter_by(id=model.id).first()
            artifact.insured = "PENDING"
            db.session.commit()

