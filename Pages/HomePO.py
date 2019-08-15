from Base.SeleniumDriver import seleniumDriver
import Utilities.customLogger as cl
import logging

class HomePO(seleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _logoutBtn = "//a[contains(text(),'Logout')]"

    def clickLogoutBtn(self):
        self.hardwait(15)
        self.click(self._logoutBtn,locatortype="xpath")
        self.log.info("Clicked on logout btn")
