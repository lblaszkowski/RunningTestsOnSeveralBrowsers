
import unittest
from selenium import webdriver


url = "http://sweetsoundtrack.com/"


class SearchMovies(unittest.TestCase):

    def setUp(self, browser="mozilla"):
        if browser == "chrome" or browser == "ch":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_75/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        elif browser == "mozilla" or browser == "ff":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        # elif browser == "internet" or browser == "ie11":
        #     self.driver = webdriver.Firefox(executable_path=r'../Drivers/IE_11/IEDriverServer.exe')
        #     self.driver.maximize_window()
        #     self.driver.get(url)
        # elif browser == "opera" or browser == "op":
        #     self.driver = webdriver.Firefox(executable_path=r'../Drivers/Opera_60/operadriver.exe')
        #     self.driver.maximize_window()
        #     self.driver.get(url)
        # elif browser == "phantomjs" or browser == "ph":
        #     self.driver = webdriver.Firefox(executable_path=r'../Drivers/Phantomjs_2_1_1/phantomjs.exe')
        #     self.driver.maximize_window()
        #     self.driver.get(url)
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


    def songinaMovie(self):
        self.driver.find_element_by_class_name("searchString").send_keys("Singin' in the Rain")
