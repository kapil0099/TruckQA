import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SingUp:
    link_signup_page = (By.XPATH, "//a[normalize-space()='Sign up']")
    txt_first_name = (By.NAME, "first-name")
    txt_last_name = (By.NAME, "last-name")
    txt_phone_num = (By.XPATH, "//input[@placeholder='+(123) 456-7890']")
    txt_email = (By.NAME, "email")
    txt_confirm_email = (By.NAME, "confirm-email")
    txt_password = (By.NAME, "password")
    drp_signup_source = (By.XPATH, "//form[contains(@class,'_content_y68oo_77')]//select")
    txt_other_signup_source = (By.XPATH, "//input[contains(@placeholder,'Provide an option')]")
    btn_signup = (By.XPATH, "//button[normalize-space()='Sign up']")

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 10)

    def openSignUpPage(self):
        self.wait.until(EC.element_to_be_clickable(self.link_signup_page)).click()

    def enterFirstName(self, first_name):
        self.wait.until(EC.presence_of_element_located(self.txt_first_name)).send_keys(first_name)

    def enterLastName(self, last_name):
        self.wait.until(EC.presence_of_element_located(self.txt_last_name)).send_keys(last_name)

    def enterPhoneNumber(self, phone_number):
        self.wait.until(EC.presence_of_element_located(self.txt_phone_num)).send_keys(phone_number)

    def enterEmail(self, email):
        self.wait.until(EC.presence_of_element_located(self.txt_email)).send_keys(email)

    def enterConfirmEmail(self, confirm_email):
        self.wait.until(EC.presence_of_element_located(self.txt_confirm_email)).send_keys(confirm_email)

    def enterPassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.txt_password)).send_keys(password)

    def select_signup_source(self, signup_source):
        signup_source_dropdown = self.wait.until(EC.presence_of_element_located(self.drp_signup_source))
        for option in signup_source_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == signup_source:
                option.click()
        print(f"Warning: Signup source '{signup_source}' not found.")

    def clickSignupButton(self):
        time.sleep(10)
        self.wait.until(EC.element_to_be_clickable(self.btn_signup)).click()
        time.sleep(10)