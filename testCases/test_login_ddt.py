import pytest
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger=LogGen.log()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login **************")
        self.logger.info("************** Verifying Login Test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.openLoginPage()

        self.rows = XLUtils.gerRowCount(self.path,'Sheet1')
        print("Number of row in a Excel:", self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.Email = XLUtils.readData(self.path,'Sheet1',r,1)
            self.Password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.Result = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setEmail(self.Email)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)
            if self.lp.isReservationPagePresent():
                if self.Result=="Pass":
                    self.logger.info("********** Passed ********")
                    self.lp.clickMenu()
                    self.lp.clickLogout()
                    self.lp.openLoginPage()
                    lst_status.append("Pass")
                elif self.Result=="Fail":
                    self.logger.info("********** Failed ********")
                    self.lp.clickMenu()
                    self.lp.clickLogout()
                    self.lp.openLoginPage()
                    lst_status.append("Fail")
            else:
                if self.Result=="Pass":
                    self.logger.info("********** Failed ********")
                    lst_status.append("Fail")
                elif self.Result=="Fail":
                    self.logger.info("********** Passed ********")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT test passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT test Failed ******")
            self.driver.close()
            assert False

        self.logger.info("*********** End of Login DDT test *********")
        self.logger.info("*********** Completed Test_002_DDT_Login *********")