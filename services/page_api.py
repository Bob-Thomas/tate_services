import config
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, abort
from flask import Flask, request
from models.database import db
from models.ticket import Ticket
from inflection import underscore
from controllers.page import PageController


class PageApi(restful.Resource):

    controller = PageController()

    def get(self, page_id=None):
        if page_id:
            return self.controller.page_to_json(self.controller.get_page(page_id))
        else:
            pages = self.controller.get_all_pages()
            page_json = []
            for page in pages:
                page_json.append(self.controller.page_to_json(page))
            return page_json
