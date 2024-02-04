from selenium.webdriver.common.by import By
class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "email_or_phone")
    password = (By.ID,"password")
    logInButton = (By.XPATH,"//button[normalize-space()='Login']")
    myOrders = (By.XPATH, "//h1[normalize-space()='Recent Orders']")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)
    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogInButton(self):
        return self.driver.find_element(*LoginPage.logInButton)

    def getMyOrder(self):
        return self.driver.find_element(*LoginPage.myOrders)
