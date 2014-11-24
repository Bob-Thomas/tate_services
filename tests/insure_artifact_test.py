from controllers.Insurance import InsuranceController
from models.agreement import Agreement
from models.insured_artifacts import InsuredArtifacts
from models.artifact import Artifact
from models.database import db
from controllers.artifact import ArtifactController
from models.quotation import Quotation
from models.request import Request

__author__ = 'bob'

import unittest


class ArtifactInsureTest(unittest.TestCase):
    def setUp(self):
        #setup mock artifact
        self.artifact = Artifact(name='Leeuw', reason="Zag er prachtig uit in goede staat", geological_period="Krijt",
                                 value='2900.30', image='leeuw.png', insured="NO", active=True)
        #add artifact to the database
        db.session.add(self.artifact)
        db.session.commit()

        self.controller = InsuranceController()

    def tearDown(self):
        #cleanup test artifact
        db.session.delete(self.artifact)
        db.session.commit()


    def test_insure_artifact_completed(self):
        print ""
        print "Test full insurance"
        print "-------------------------------------"
        #request insurance for artifact
        #call class method to request insurance
        ArtifactController.insure_artifact(self.artifact.id)
        #check if insurance is pending
        self.assertEquals(self.artifact.insured, "PENDING", "not requested")
        #get the created insurance quotation
        self.controller.get_quation_from_artifact(self.artifact.id)
        #check if it exists
        self.assertEquals(self.artifact.insured, "YES", "not insured")
        #query the newly created insured artifact
        insured_artifact = InsuredArtifacts.query.filter_by(artifact=self.artifact.id).first()
        #check if artifact is in the table insured artifacts
        self.assertTrue(insured_artifact, "Not in insurance")
        #remove all the test data
        db.session.delete(insured_artifact)
        db.session.delete(Agreement.query.filter_by(artifact=self.artifact.id).first())
        db.session.delete(Quotation.query.filter_by(artifact=self.artifact.id).first())
        db.session.delete(Request.query.filter_by(artifact=self.artifact.id).first())
        print "END full insurance"

    def test_insure_artifact_pending(self):
        print ""
        print "Test pending insurance"
        print "-------------------------------------"
        #request insurance for artifact
        ArtifactController.insure_artifact(self.artifact.id)
        #make sure its pending
        self.assertEquals(self.artifact.insured, "PENDING", "not requested")
        print "END pending insurance"

    def test_insure_insured_artifact(self):
        #test if you can insure an artifact twice
        print ""
        print "Test insuring the same artifact twice"
        print "-------------------------------------"
        #try to insure first time
        ArtifactController.insure_artifact(self.artifact.id)
        self.assertEquals(self.artifact.insured, "PENDING", "not requested")
        #try to insure second time
        ArtifactController.insure_artifact(self.artifact.id)
        self.assertEquals(self.artifact.insured, "PENDING")
        print "END double insurance"


if __name__ == '__main__':
    unittest.main()
