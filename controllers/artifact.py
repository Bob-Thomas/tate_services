from models.database import db
from models.artifact import Artifact
from models.insurer import Insurer
from models.quotation import Quotation
from models.request import Request



class ArtifactController():

    @staticmethod
    def insure_artifact( artifact_id):
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
                db.session.add(Quotation(information="Ik ga graag akkoord voor de prijs van 100 euro", artifact=artifact.id, request=request.id, price=100.00))
                db.session.commit()
                print "artifact insurance requested"
                artifact.insured = "PENDING"
                db.session.commit()

        else:
            print 'no artifact'