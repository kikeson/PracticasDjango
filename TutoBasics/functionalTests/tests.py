from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_load_file_and_display_content(self):
        #Manuela visits page and loads correctly
        self.browser.get(self.live_server_url)

        #She is glad to see that contents of the site are descriptive
        self.assertIn('Data Loader', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Data Loader', header_text)

        #She is invited to select a file from her computer
        element = self.browser.find_element_by_id('SubirCSV')
        element.sendKeys("C:\\Users\\Enrique\\Desktop\\testfile.txt");

        #She upload her wonderful csv

        #When she selects the file she gets a message that the loading was ok

        #She gets the option to visualize a table with the contents

        #If the file is too large only a sample is displayed

