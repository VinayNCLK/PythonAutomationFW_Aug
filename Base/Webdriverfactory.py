from selenium import webdriver
import os
import Utilities.customLogger as cl
import logging

class WebdriverFactory():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,browser):
        self.chrome_api_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW_Aug\\browserapis\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = self.chrome_api_location
        self.ff_api_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW_Aug\\browserapis\\geckodriver.exe"
        os.environ["webdriver.gecko.driver"] = self.ff_api_location
        self.ie_api_location = "C:\\Users\\shekar\\PycharmProjects\\AutomationFW_Aug\\browserapis\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = self.ie_api_location
        self.appurl = "http://localhost/login.do"
        self.browser = browser


    def getWebdriverInstance(self):
        if self.browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=self.chrome_api_location)
            self.log.info("Execution will start in chrome browser")
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=self.ff_api_location)
            self.log.info("Execution will start in firefox browser")
        elif self.browser == "ie":
            self.driver = webdriver.Ie(executable_path=self.ie_api_location)
            self.log.info("Execution will start in ie browser")
        else:
            self.log.error("Please provide the valid browser name")
            return False

        self.driver.get(self.appurl)
        self.log.info("Enter url "+self.appurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        return self.driver


