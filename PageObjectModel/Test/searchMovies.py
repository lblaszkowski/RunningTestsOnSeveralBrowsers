import unittest
from selenium import webdriver
import os
import time

from selenium.webdriver import DesiredCapabilities

url = "http://sweetsoundtrack.com/"


class SearchMovies(unittest.TestCase):

    def setUp(self, browser="ie"):
        if browser == "chrome" or browser == "ch":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_75/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
            print("Start testu")
        elif browser == "mozilla" or browser == "ff":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        elif browser == "phantomjs" or browser == "ph":
            self.driver = webdriver.PhantomJS(executable_path=r'../Drivers/Phantomjs_2_1_1/phantomjs.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        elif browser == "internet" or browser == "ie":
            self.driver = webdriver.Ie(executable_path=r'../Drivers/IE_11/IEDriverServer.exe')
            self.driver.maximize_window()
            IE_Brows = os.path.dirname(__file__)
            ie_driver_path = IE_Brows + "../Drivers/IE_11/IEDriverServer.exe"
            self.driver.get(url)
        # elif browser == "opera" or browser == "op":
        #     self.driver = webdriver.Opera(executable_path=r'../Drivers/Opera_60/operadriver.exe')
        #     self.driver.maximize_window()
        #     self.driver.get(url)
        # elif browser == "edge " or browser == "ed":
        #     self.driver = webdriver.Edge(executable_path=r'../Drivers/Edge_17134/MicrosoftWebDriver.exe')
        #     self.driver.maximize_window()
        #     self.driver.get(url)
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def test_songinaMovie(self):
        searchSonginaFromMovies = self.driver.find_element_by_xpath("//*[@class ='form-inline']//input[@class ='form-control']")
        searchSonginaFromMovies.click()
        searchSonginaFromMovies.send_keys("Singin' in the Rain")
        linkSonginaFromMovies = self.driver.find_element_by_xpath("//*[@class='form-inline']//*[text()='Search']")
        linkSonginaFromMovies.click()
        clickSonginaFromMovies = self.driver.find_element_by_xpath('//*[@class="list-unstyled"]//*[text()="Singin\' in the Rain"]')
        clickSonginaFromMovies .click()
        print(self.driver.find_element_by_xpath('//*[@class="centersmall"]').text)
        assert self.driver.find_element_by_xpath('//*[@class="centersmall"]').text == "Singin' in the Rain (1952)"




