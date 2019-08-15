
import pytest
import unittest
from Pages.LoginPO import LoginPO
from Pages.HomePO import HomePO


@pytest.mark.usefixtures("setup","onetime_setup")
class Test_Case1(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self):
        print("Class level setup")
        self.lp = LoginPO(self.driver)
        self.hp = HomePO(self.driver)

    def test_validloginAndLogout(self):
        self.lp.sendUsername("admin")
        self.lp.sendpwd("manager")
        self.lp.clickLoginBtn()
        self.hp.clickLogoutBtn()



