
import pytest
import unittest
from Pages.LoginPO import LoginPO
import Utilities.customLogger as cl
import logging
from ddt import ddt,unpack,data
from Utilities.getCsvData import getcsvdata

@pytest.mark.usefixtures("setup","onetime_setup")
@ddt
class Test_Case3(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    @pytest.fixture(autouse=True)
    def classSetup(self):
        print("Class level setup")
        self.lp = LoginPO(self.driver)

    @data(*getcsvdata("C:\\Users\\shekar\\PycharmProjects\\"
                      "AutomationFW_Aug\\testdata.csv"))
    @unpack
    def test_invalidlogin(self,userName,Password):
        try:
            self.lp.sendUsername(userName)
            self.lp.sendpwd(Password)
            self.lp.clickLoginBtn()
            assert self.lp.invalid_errormsg() == True
            self.log.info("Validated the error message successfully")
        except:
            self.driver.get_screenshot_as_file("C:\\Users\\shekar\\PycharmProjects\\AutomationFW_Aug\\Screenshots\\test_invalidlogin.png")


