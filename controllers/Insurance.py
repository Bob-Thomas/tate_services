from models.database import db
from models.artifact import Artifact
from models.agreement import Agreement
from models.insurer import Insurer
from models.quotation import Quotation
from models.request import Request
from models.insured_artifacts import InsuredArtifacts
from datetime import datetime
from datetime import date


def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year=d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))


class InsuranceController():
    def __init__(self):
        pass

    def get_quation_from_artifact(self, artifact_id):
        artifact = Artifact.query.filter_by(id=artifact_id).first()
        if artifact:
            quotation = Quotation.query.filter_by(artifact=artifact.id).first()
            request = Request.query.filter_by(artifact=artifact.id).first()
            if quotation and request:
                insurer = Insurer.query.filter_by(id=request.insurer).first()
                if insurer:
                    print "create agreement"
                    agreement = Agreement(information=request.information, quotation=quotation.id,
                                          request=request.id, artifact=artifact.id,
                                          insurer=insurer.id, price=quotation.price)
                    db.session.add(agreement)
                    artifact.insured = "YES"
                    insured_artifact = InsuredArtifacts(insurer=insurer.id, artifact=artifact.id,
                                                        request_date=datetime.now().strftime("%Y-%m-%d"),
                                                        end_date=add_years(datetime.now(), 4).strftime("%Y-%m-%d"))
                    db.session.add(insured_artifact)
                    print "artifact agreement created and insured"
                    db.session.commit()
