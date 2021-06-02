import json
import unittest
from time import sleep

from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_login import PageLogin
def get_date():
    date = []
    with open("../date/login.json", "r", encoding="utf-8")as f:
        all = json.load(f)
        for all in all.values():
            username = all["username"]
            password = all["password"]
            # verify_code = all["verify_code"]
            # result = all["result"]
            # status = all["status"]
            date.append((username, password))
    return date


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = PageLogin(GetDriver().get_driver())
    def tearDown(self):
        sleep(5)
        GetDriver().quit_driver()

    @parameterized.expand(get_date())
    def test_login(self, username, password):
        self.login.page_login(username, password)
