import time
import unittest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass
class test_Lonin(unittest.TestCase,BaseClass):
    def test_UserLogIn(self):
        log = self.getLogger()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        homepage = HomePage(self.driver)
        homepage.LoginButton()
        log.info("Going the Login Page")
        time.sleep(2)
        logging = LoginPage(self.driver)
        logging.getEmail().send_keys("akashahmed@gmail.com")
        logging.getPassword().send_keys("ABC")
        logging.getLogInButton().click()
        log.info("Login into the System")
        assert logging.getMyOrder().is_displayed()
        log.info("Logged In")





