from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.core.files.uploadedfile import SimpleUploadedFile
import django.core.files
import os
import TutoBasics
from uploadfiles.forms import UploadFileForm
from datetime import date


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()



    def check_upload_file_ok(self,name,description):
        file_element = self.browser.find_element_by_id('id_file')
        file_element.send_keys(os.path.join(TutoBasics.settings.BASE_DIR,'documents',name))
        desc_element = self.browser.find_element_by_id('id_description')
        desc_element.send_keys(description)
        self.browser.find_element_by_id('upload_submit').click()
        # She gets a message confirming correct upload
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Congrats',header_text)

        # Chooses to return to uploads
        self.browser.find_element_by_id('return_uploader').click()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_load_file_and_display_content(self):
        
        #Manuela visits page and loads correctly
        self.browser.get(self.live_server_url+'/uploadfiles')

        #She is glad to see that contents of the site are descriptive
        self.assertIn('Data Loader', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Data Loader', header_text)

        #She is invited to select a file from her computer and describe it
        file_element = self.browser.find_element_by_id('id_file')
        file_element = self.browser.find_element_by_id('id_description')
     

        #She upload her wonderful csv
        #She can describe the file
        #When she selects the file she gets a message that the loading was ok        
        name1 = 'prueba.csv'
        description1 = 'My first description'
        name2 = 'prueba2.csv'
        description2 = 'Look! I described again'
        self.check_upload_file_ok(name1,description1)
        self.check_upload_file_ok(name2,description2)

        # She can see the list of files she has uploaded
        self.check_for_row_in_list_table(description1)        
        self.check_for_row_in_list_table(description2)
        
        # She can see options to remove or load the files
        
        remove_btn = self.browser.find_elements_by_class_name('remove_item')
        if len(remove_btn)==0:
            print('No remove_item found')
            raise ValueError('No remove item!')

        
        load_btn = self.browser.find_elements_by_class_name('load_item')        
        if len(load_btn)==0:
            raise ValueError('No load item!')

        # She can select a file and load its content

        # If the file is too large only a sample is displayed

        # She gets the option to visualize the table graphically

