from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search = (By.XPATH, "//input[@id='search-input']")
    searchButton = (By.XPATH, "//img[@alt='search icon']")
    addToCart = (By.XPATH,"(//button[normalize-space()='Add to Cart'])")
    logIn = (By.LINK_TEXT,"Login")
    alert = (By.XPATH, "//div[contains(text(),'Please select a valid option')]")

    def getSearchInox(self):
        return self.driver.find_element(*HomePage.search)

    def getSearchButton(self):
        return self.driver.find_element(*HomePage.searchButton)

    def getAddToCartButton(self):
        return self.driver.find_element(*HomePage.addToCart)

    def LoginButton(self):
        return self.driver.find_element(*HomePage.logIn).click()
    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)
