import config
from models.database import db
from models.performance import Performance
from models.artifact import Artifact
from models.artifacts_in_performance import ArtifactsInPerformance
from artifact import ArtifactController
from models.insured_artifacts import InsuredArtifacts


class PerformanceController():
    def get_all_performances(self):
        return Performance.query.all()

    def get_performance(self, id):
        return Performance.query.filter_by(id=id).first()

    def performance_to_json(self, performance):
        json = {}
        if performance:
            json['name'] = performance.name
            json['information'] = performance.information
            json['image'] = self.get_performance_base64_image(performance)
            json['startDate'] = performance.starting_date.strftime('%d-%m-%Y')
            json['endDate'] = performance.end_date.strftime('%d-%m-%Y')
            json['artifacts'] = self.get_artifacts_in_performance(performance)
        return json

    def get_performance_base64_image(self, performance):
        if performance:
            with open(config.PERFORMANCE_PATH + config.DIVIDER + performance.image, "rb") as f:
                data = f.read()
            return data.encode("base64")

    def get_artifacts_in_performance(self, performance):
        if performance:
            artifact_json = []
            artifacts_in_performance = ArtifactsInPerformance.query.filter_by(performance=performance.id).all()
            for temp in artifacts_in_performance:
                artifact = Artifact.query.filter_by(id=temp.artifact).first()
                artifact_json.append(ArtifactController.get_artifact_in_json(temp.artifact))
            return artifact_json


