import config
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, abort
from flask import Flask, request
from models.database import db
from models.ticket import Ticket
from inflection import underscore
from controllers.performance import  PerformanceController

class PerformanceApi(restful.Resource):

    controller = PerformanceController()

    def get(self, page_id=None):
        if page_id:
            return self.controller.performance_to_json(self.controller.get_performance(page_id))
        else:
            performances = self.controller.get_all_performances()
            performance_json = []
            for performance in performances:
                performance_json.append(self.controller.performance_to_json(performance))
            return performance_json


    def post(self):
        print "post"