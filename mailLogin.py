import unittest
from selenium import webdriver
from KUpujemProdajem.klasaRegister import Register
import time

class MailLoginRight(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()


    def testLoginRight(self):
        self.driver.get("https://www.kupujemprodajem.com/")


        reg=Register(self.driver)

        reg.findUlogujteSe()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.kupujemprodajem.com/user.php?action=welcome")
        self.driver.refresh()

        reg.findRegistracija()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.kupujemprodajem.com/user.php?action=new&return_url=")
        self.driver.refresh()


        reg.findEmail()
        reg.setEmail("mail@yahoo.rs")

        reg.findLozinka()
        reg.setLozinka("jsghdfkjgh")

        reg.findLozinka2()
        reg.setLozinka2("jsghdfkjgh")

        reg.find15()

        reg.find16()

        reg.posalji()
        assert "No result found." not in self.driver.page_source
        time.sleep(4)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

