import config
from models.database import db
from models.performance import Performance
from models.page import Page
from models.artifact import Artifact
from models.artifacts_in_performance import ArtifactsInPerformance
from artifact import ArtifactController
from models.insured_artifacts import InsuredArtifacts


class PageController():

    def get_all_pages(self):
        return Page.query.all()

    def get_page(self, id):
        return Page.query.filter_by(id=id).first()

    def page_to_json(self, page):
        json = {}
        if page:
            json['id'] = page.id
            json['name'] = page.name
            json['title'] = page.title
            json['content'] = page.content
            json['image'] = self.get_page_image_base64(page)
        return json

    def get_page_image_base64(self, page):
        if page:
            with open(config.PERFORMANCE_PATH + config.DIVIDER + page.image, "rb") as f:
                data = f.read()
            return data.encode("base64")

    def __init__(self):
        pass


