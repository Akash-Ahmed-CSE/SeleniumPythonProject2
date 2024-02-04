
import time

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
class TestHomePage(BaseClass):
    def test_formSubmission(self):
        log = self.getLogger()
        page_title = self.driver.title
        assert ("Shoplover Ltd" in page_title)
        time.sleep(2)
        homepage = HomePage(self.driver)
        homepage.getSearchInox().send_keys("Bag")
        log.info("Searching for Bag")
        homepage.getSearchButton().click()
        time.sleep(5)
        Iteams = self.driver.find_elements(By.XPATH, "//div[@class='flex flex-col gap-2 p-3']")
        if Iteams:
            # Click on the first item
            Iteams[4].click()
        else:
            print("No items found")
        log.info("One Iteam selected")
        time.sleep(5)
        homepage.getAddToCartButton().click()
        time.sleep(5)
        alert = homepage.getAlert().text
        #p = self.driver.find_element(By.XPATH,"//div[contains(text(),'Please select a valid option')]").text
        assert ("Please select a valid option 1" in alert)
