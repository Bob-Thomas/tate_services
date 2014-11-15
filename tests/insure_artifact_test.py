from models.insured_artifacts import InsuredArtifacts
from models.artifact import Artifact
from models.database import db
from controllers.artifact import ArtifactController
__author__ = 'bob'

import unittest


class ArtifactInsureTest(unittest.TestCase):

    def setUp(self):
        self.artifact = Artifact(name='Leeuw', reason="Zag er prachtig uit in goede staat", geological_period="Krijt", value='2900.30', image='leeuw.png', insured="NO", active=True)
        db.session.add(self.artifact)
        db.session.commit()

    def tearDown(self):
        db.session.delete(self.artifact)
        db.session.commit()

    def test_insure_artifact(self):
        ArtifactController.insure_artifact(self.artifact.id)
        self.assertEquals(self.artifact.insured, "PENDING", "not requested")




if __name__ == '__main__':
    unittest.main()
