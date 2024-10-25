import pytest
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SignupPage import SingUp
from testCases.conftest import setup
import random


# Lists of possible first and last names
first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Eve', 'Grace', 'Oscar', 'Lily', 'Noah']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
# Generate a random number
random_phone_number = random.randint(3050000000, 9050000000)
random_number = random.randint(1, 100)

class Test_003_SignUp:
    baseURL = ReadConfig.getApplicationURL()
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    email = f"test+auto{random_number}@ozandac.com"
    phone = f"{random_phone_number}"
    signup_source = "Google/web search"

    logger=LogGen.log()

    @pytest.mark.sanity
    def test_signUp(self, setup):
        self.logger.info("*********** Test_003_SignUp ************")
        self.logger.info("************** Starting Signing Up **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.sp=SingUp(self.driver)
        self.lp=Login(self.driver)
        self.sp.openSignUpPage()
        self.sp.enterFirstName(self.first_name)
        self.sp.enterLastName(self.last_name)
        self.sp.enterPhoneNumber(self.phone)
        self.sp.enterEmail(self.email)
        self.sp.enterConfirmEmail(self.email)
        self.sp.enterPassword("Eight1@2")
        self.sp.select_signup_source(self.signup_source)
        self.sp.clickSignupButton()
        self.logger.info("*************** Saving user info ***************")
        if self.lp.isReservationPagePresent():
            print("SignUp is Success")
            self.logger.info("************** SignUp Test is Passed **************")
            assert True
        else:
            print("SignUp Failed")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SignUP.png")
            self.logger.error("************** SignUp Test is Failed **************")
            assert False

        self.driver.close()


