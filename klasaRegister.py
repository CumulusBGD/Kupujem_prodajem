class Register():

    def __init__(self, driver):
        self.driver = driver

    def findUlogujteSe(self):
        return self.driver.find_element_by_xpath("//a[@href='https://www.kupujemprodajem.com/user.php?action=login']")


    def findRegistracija(self):
        return self.driver.find_element_by_xpath("//input[contains(@value,'Registracija')]")

    def findEmail(self):
        return self.driver.find_element_by_xpath("//input[@style='width: 70%; font-size: 120%;']")
    def setEmail(self, pwd):
        self.findEmail().send_keys(pwd)
    def findLozinka (self):
        return self.driver.find_element_by_xpath("//input[@id='inputPassword']")
    def setLozinka(self,pwd):
        self.findLozinka().send_keys(pwd)

    def findLozinka2(self):
            return self.driver.find_element_by_xpath("//input[@id='inputRepeatPassword']")

    def setLozinka2(self, pwd):
            self.findLozinka2().send_keys(pwd)

    def find15(self):
        self.driver.find_element_by_xpath("//input[contains(@id,'terms_yes')]").click()


    def find16(self):
        self.driver.find_element_by_xpath("//input[contains(@id,'older16_yes')]").click()


    def posalji(self):
        self.driver.find_element_by_xpath("//input[@class='submit']").click()






