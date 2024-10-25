from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Login:
    link_login_page= (By.XPATH, "//a[normalize-space()='Log in']")
    textbox_email= (By.ID, "email")
    textbox_password= (By.NAME, "password")
    button_login= (By.XPATH, "//button[normalize-space()='Log in']")
    reservation= (By.XPATH, "//a[normalize-space()='Reservations']")
    button_menu= (By.XPATH, "//button[normalize-space()='Menu']")
    button_logout= (By.XPATH, "//button[normalize-space()='Log out']")

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)

    def openLoginPage(self):
        self.wait.until(EC.element_to_be_clickable(self.link_login_page)).click()

    def setEmail(self, email):
        self.wait.until(EC.presence_of_element_located(self.textbox_email)).clear()
        self.wait.until(EC.presence_of_element_located(self.textbox_email)).send_keys(email)

    def setPassword(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.textbox_password))
        password_field.send_keys(Keys.CONTROL + "a")  # Select all text
        password_field.send_keys(Keys.DELETE)  # Delete the selected text
        password_field.send_keys(password)  # Now enter the password

    def clickLogin(self):
        self.wait.until(EC.element_to_be_clickable(self.button_login)).click()

    def clickMenu(self):
        self.wait.until(EC.element_to_be_clickable(self.button_menu)).click()

    def clickLogout(self):
        self.wait.until(EC.element_to_be_clickable(self.button_logout)).click()

    def isReservationPagePresent(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.reservation))
            return True
        except TimeoutException:
            return False
