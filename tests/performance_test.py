from models.database import db

__author__ = 'bob'

import unittest
from models.performance import Performance


class PerformanceTest(unittest.TestCase):
    def test_create_performance(self):
        performance = Performance(name="test voorstelling", information="dit is een test voorstelling",
                                  starting_date="2016-01-30", end_date="2017-01-30")
        db.session.add(performance)
        db.session.commit()
        # retrieve new performance
        new_performance = Performance.query.filter_by(id=performance.id).first()
        self.assertIsNotNone(new_performance, "no new performance added")

        db.session.delete(performance)
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
