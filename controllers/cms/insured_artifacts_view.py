from flask import url_for
from flask.ext.admin.contrib.sqla import ModelView
from markupsafe import Markup
from models.database import db
from models.artifact import Artifact
from models.insured_artifacts import InsuredArtifacts
from flask.ext.admin.actions import action
from flask.ext import login


class InsuredArtifactsView(ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()

    def insurer_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (url_for('insurerview.index_view'), model.insurers.company)
        ) if model.insurer else ""

    def artifact_formatter(view, context, model, name):
        return Markup(
            "<a href='%s'>%s</a>" % (url_for('artifactview.index_view'), model.artifacts.name)
        ) if model.artifact else ""

    column_auto_select_related = True
    column_list = ('insurers', 'artifacts', 'request_date', 'end_date')
    column_filters = ('end_date', 'request_date')
    column_formatters = {
        'insurers': insurer_formatter,
        'artifacts': artifact_formatter
    }
    #can_create = False

    def on_model_change(self, form, model, is_created):
        artifact = Artifact.query.filter_by(id=str(form.artifacts).split('"')[7]).first()
        artifact.insured = "PENDING"
        artifact.active = True
        db.session.commit()

    def on_model_delete(self, model):
        artifact = Artifact.query.filter_by(id=model.artifact).first()
        artifact.insured = "NO"
        artifact.active = False
        db.session.commit()