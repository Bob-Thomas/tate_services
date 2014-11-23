from sqlalchemy import func

import config
from models.database import db
from models.artifact import Artifact
from models.insurer import Insurer
from models.quotation import Quotation
from models.request import Request


class ArtifactController():
    @staticmethod
    def insure_artifact(artifact_id):
        artifact = Artifact.query.filter_by(id=artifact_id).first()
        insurers = Insurer.query.all()
        if artifact:
            if artifact.insured == "YES":
                return 'already insured'
            elif artifact.insured == "PENDING":
                return 'already pending'
            elif artifact.insured == "NO":
                print "insuring artifact"
                print "sending email to insurers"
                for insurer in insurers:
                    print insurer.name
                    db.session.add(Request(information='Artefact verzekeren', insurer=insurer.id, artifact=artifact.id))
                db.session.commit()
                print insurers[1].name + " answered with lowest price 100"
                print "creating quotation"
                request = Request.query.filter_by(insurer=insurers[1].id).first()
                db.session.add(
                    Quotation(information="Ik ga graag akkoord voor de prijs van 100 euro", artifact=artifact.id,
                              request=request.id, price=100.00))
                db.session.commit()
                print "artifact insurance requested"
                artifact.insured = "PENDING"
                db.session.commit()
        else:
            print 'no artifact'

    @staticmethod
    def get_artifact_in_json(id):
        artifact = Artifact.query.filter_by(id=id).first()
        json = {}
        if artifact:
            json['id'] = id
            json['name'] = artifact.name
            json['reason'] = artifact.reason
            json['geologicalPeriod'] = artifact.geological_period
            json['image'] = ArtifactController.get_base_64_artifact(id)
            json['value'] = artifact.value
            json['insured'] = artifact.insured
            json['active'] = artifact.active
            json['locationFound'] = artifact.location_found
            json['dateFound'] = artifact.date_found.strftime('%d-%m-%Y')
        return json

    @staticmethod
    def get_random_artifact():
        return Artifact.query.order_by(func.rand()).first()


    @staticmethod
    def get_base_64_artifact(id):
        artifact = Artifact.query.filter_by(id=id).first()
        if artifact:
            with open(config.ARTIFACT_PATH + config.DIVIDER + artifact.image, "rb") as f:
                data = f.read()
            return data.encode("base64")

