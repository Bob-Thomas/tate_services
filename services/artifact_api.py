from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse
from flask import Flask, request
import time
from models.database import db
from models.artifact import Artifact
from inflection import underscore
import re
from controllers.ticket import TicketController
from controllers.artifact import ArtifactController


class ArtifactApi(restful.Resource):
    parser = reqparse.RequestParser()

    ticket_controller = TicketController()

    def get(self, action=None, artifact_id=None):
        if artifact_id:
            return ArtifactController.get_artifact_in_json(artifact_id)
        else:
            artifacts = []
            for artifact in Artifact.query.filter_by(active=True, insured='YES').all():
                artifacts.append(ArtifactController.get_artifact_in_json(artifact.id))
            return artifacts

    def post(self):
        return "whoopy"
