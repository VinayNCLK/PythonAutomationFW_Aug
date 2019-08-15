
import pytest
import unittest
from Pages.LoginPO import LoginPO
import Utilities.customLogger as cl
import logging


@pytest.mark.usefixtures("setup","onetime_setup")
class Test_Case2(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    @pytest.fixture(autouse=True)
    def classSetup(self):
        print("Class level setup")
        self.lp = LoginPO(self.driver)

    def test_invalidlogin(self):
        self.lp.sendUsername("admin1")
        self.lp.sendpwd("pwd1")
        self.lp.clickLoginBtn()
        assert self.lp.invalid_errormsg() == True
        self.log.info("Validated the error message successfully")



