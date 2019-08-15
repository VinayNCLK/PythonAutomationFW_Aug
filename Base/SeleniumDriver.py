
import Utilities.customLogger as cl
import logging
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class seleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatortype="id"):
        locatortype = locatortype.lower()
        if locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "id":
            return By.ID
        elif locatortype == "name":
            return By.NAME
        elif locatortype == "classname":
            return By.CLASS_NAME
        elif locatortype == "link":
            return By.LINK_TEXT
        elif locatortype == "partiallink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Please provide the valid locator")
            return False



    def getElement(self,locatorvalue,locatortype="id"):
        element = None
        try:
            bytype = self.getByType(locatortype)
            element = self.driver.find_element(bytype, locatorvalue)
            self.log.info("Identified element with locator "+locatortype+
                          "Locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Element is not identified "+e)
        return element

    def getElements(self, locatorvalue, locatortype="id"):
        listofelements = None
        try:
            bytype = self.getByType(locatortype)
            listofelements = self.driver.find_elements(bytype, locatorvalue)
            self.log.info("Identified elements with locator " + locatortype +
                          "Locator value " + locatorvalue)
        except Exception as e:
            self.log.error("Elements is not identified " + e)
        return listofelements

    def isElementPresent(self,locatorvalue,locatortype="id"):
        element = self.getElement(locatortype,locatorvalue)
        if element is not None:
            self.log.info("Element is present")
            return True
        else:
            self.log.error("Element is not present")
            return False

    def click(self,locatorvalue,locatortype="id"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            element.click()
            self.log.info("Clicked on Element with locator "+locatortype+
                          "locator value "+locatorvalue)
        except Exception as e:
            self.log.error("Unable to Click on Element with locator " + locatortype +
                          "locator value " + locatorvalue)

    def send(self,locatorvalue,value,locatortype="id"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            element.send_keys(value)
            self.log.info("Sent data on Element with locator "+locatortype+
                          "locator value "+locatorvalue+ " value "+value)
        except Exception as e:
            self.log.error("Unable to Send data on Element with locator " + locatortype +
                          "locator value " + locatorvalue+ " value "+value)


    def maximizewindow(self):
        self.driver.maximize_window()

    def minimizewindow(self):
        self.driver.minimize_window()

    def setbrowseractions(self,action = "back"):
        if action == "back":
            self.driver.back()
        elif action == "forward":
            self.driver.forward()
        elif action == "refresh":
            self.driver.refresh()

    def getTitle(self):
        currenttitle = self.driver.title
        return currenttitle

    def getText(self,locatorvalue,locatortype="id"):
        element = self.getElement(locatorvalue, locatortype)
        return element.text

    def getPageSource(self):
        pagesource = self.driver.page_source
        return pagesource

    def hardwait(self,timesec=50):
        time.sleep(timesec)

    def closewindow(self):
        self.driver.close()

    def selectoptionfromdrpdwn(self,locatorvalue,visbletext="India",locatortype="id"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            sel = Select(element)
            sel.select_by_visible_text(visbletext)
            self.log.info("Selected option "+visbletext+" in drp dwn")
        except Exception as e:
            self.log.error("Unble to Select option " + visbletext + " in drp dwn"+e)


    def deselectoptionfromdrpdwn(self,locatorvalue,visbletext="India",locatortype="id"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            sel = Select(element)
            sel.deselect_by_visible_text(visbletext)
            self.log.info("DeSelected option "+visbletext+" in drp dwn")
        except Exception as e:
            self.log.error("Unble to DeSelect option " + visbletext + " in drp dwn"+e)

    def handleFrame(self,locatorvalue,locatortype="id"):
        try:
            element = self.getElement(locatorvalue,locatortype)
            self.driver.switch_to.frame(element)
            self.log.info("Switched to iframe")
        except Exception as e:
            self.log.error("Unble to switch ti iframe" + e)

    def switchToParentFrame(self):
        self.driver.switch_to.parent_frame()


    def mouseover(self,locatorvalue,locatortype="id"):
        try:
            action = ActionChains(self.driver)
            element = self.getElement(locatorvalue,locatortype)
            action.move_to_element(element).perform()
            self.log.info("Successfull mouse over on element"+locatortype+" "+locatorvalue)
        except Exception as e:
            self.log.error("UnSuccessfull mouse over on element" + locatortype + " " + locatorvalue)

    def scrollPage(self,startindex=0,endindex=1000):
        self.driver.execute_script("window.scrollBy("+startindex+","+endindex+");")

    def mouseclickAndHold(self,locatorvalue,locatortype="id"):
        try:
            action = ActionChains(self.driver)
            element = self.getElement(locatorvalue,locatortype)
            action.click_and_hold(element).perform()
            self.log.info("Successfull mouse click and hold on element"+locatortype+" "+locatorvalue)
        except Exception as e:
            self.log.error("UnSuccessfull mouse click and hold on element" + locatortype + " " + locatorvalue+" "+e)

    def getParentwindowid(self):
        parentwindowid = self.driver.current_window_handle
        return parentwindowid

    def getAllWindowids(self):
        listofwindowids = self.driver.window_handles
        return listofwindowids

    def switchToWindow(self,windowid=""):
        self.driver.switch_to.window(windowid)

    def switchToAlert(self,value="accept"):
        try:
            if value == "accept":
                self.driver.switch_to.alert.accept()
                self.log.info("Accepted the alert button")
            elif value == "dismiss":
                self.driver.switch_to.alert.dismiss()
                self.log.error("Dismissed the alert button")
        except Exception as e:
            self.log.error("Unable to switch to alert"+e)

    def webdriverwait_elementclickable(self, locatorvalue, time=10,pollfrequency=2,locatortype="id"):
        try:
            wait = WebDriverWait(self.driver, time, poll_frequency=pollfrequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
            element = self.getElement(locatorvalue,locatortype)
            wait.until(EC.element_to_be_clickable(element))
            self.log.info("Successfully waited for element with time "+time)
        except Exception as e:
            self.log.error("unSuccessfully in waiting for element with time " + time +e)
