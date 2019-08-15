from Base.SeleniumDriver import seleniumDriver
import Utilities.customLogger as cl
import logging

class LoginPO(seleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _userNameTxtBx = "//input[@name='username']"
    _pwdTxtBx = "//input[@name='pwd']"
    _login_Btn = "//div[contains(text(),'Login')]"
    _error_msg_txt = "//span[@class='errormsg']"
    def sendUsername(self,username="admin"):
        self.send(self._userNameTxtBx,username,locatortype="xpath")
        self.log.info("Entered user name "+username)

    def sendpwd(self,pwd="manager"):
        self.send(self._pwdTxtBx,pwd,locatortype="xpath")
        self.log.info("Entered password " + pwd)

    def clickLoginBtn(self):
        self.click(self._login_Btn,locatortype="xpath")
        self.log.info("Clicked on login btn")

    def invalid_errormsg(self):
        self.hardwait(5)
        errormsg = self.getText(self._error_msg_txt,locatortype="xpath")
        print("Got error msg = "+errormsg)
        if "Username or Password is invalid. Please try again. fghf" == errormsg:
            return True
        else:
            return False

