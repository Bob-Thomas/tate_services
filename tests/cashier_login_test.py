import os
import config

from controllers.cashier_controller import CashierController
from controllers.loginLogger import LoginLogger
from models.cashier import Cashier
from models.database import db


__author__ = 'endargon'

import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.user = Cashier(email='cashiertest@tate.com', first_name='Wouter', last_name='Dijkstra')
        db.session.add(self.user)
        db.session.commit()
        self.user_controller = CashierController(self.user)
        self.login_logger = LoginLogger()

    def tearDown(self):
        db.session.delete(self.user)
        db.session.commit()

    def test_blocker(self):
        # check if the test cashier has no tries
        #tries to login 3 times
        self.assertEqual(self.user.tries, 1, "tries found")
        self.user_controller.faulty_login()
        self.assertEqual(self.user.tries, 2, "tries found")
        self.user_controller.faulty_login()
        self.assertEqual(self.user.tries, 3, "tries found")
        self.user_controller.faulty_login()
        self.assertEqual(self.user.tries, 4, "tries found")
        #if it tried to login wrongly block the user
        self.assertTrue(self.user_controller.is_user_blocked())

    def test_logger(self):
        # login once
        self.assertEqual(self.user.tries, 1, "tries found")
        self.user_controller.faulty_login()
        #check if the logfile is created
        log_file = os.path.exists(config.LOG_PATH + config.DIVIDER + 'verkopers.log')
        self.assertTrue(log_file)


if __name__ == '__main__':
    unittest.main()
