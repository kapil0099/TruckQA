import pytest
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger=LogGen.log()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************** Test_001_login **************")
        self.logger.info("************** Verifying Homepage Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Truck Parking Near Me | TruckParkingClub":
            assert True
            self.driver.close()
            self.logger.info("************** Homepage Title Test is Passed **************")
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Homepage Title Test is Failed **************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************** Verifying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.openLoginPage()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.lp.isReservationPagePresent():
            print("Login is success")
            self.logger.info("************** Login Test is Passed **************")
            assert True
        else:
            print("Login Failed")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("************** Login Test is Faild **************")
            assert False

        self.driver.close()