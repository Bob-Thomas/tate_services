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


class ArtifactApi(restful.Resource):

    parser = reqparse.RequestParser()

    ticket_controller = TicketController()

    def get(self, action, id):
        print action
        print str(id)
        artifact = Artifact.query.filter_by(id=id).first()
        if artifact:
            if artifact.insured == "PENDING":
                return "already requested"
            elif artifact.insured == "YES":
                return "already insured"
            elif artifact.insured == "NO":
                return "requesting insurrance"
        else:
            return "no artifact fouund"

    def post(self):
        return "whoopy"
