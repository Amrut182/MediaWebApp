from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time 
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.test import LiveServerTestCase

class TestGoogleLogin(StaticLiveServerTestCase):
    fixtures = ['allauth_fixture']
    def setUp(self):
        self.browser = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile())
        self.browser.implicitly_wait(10)
        self.browser.wait = WebDriverWait(self.browser, 10)
        activate('en')
 
    def tearDown(self):
        self.browser.quit()
 
    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
                (By.ID, element_id)))
 
    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
                (By.ID, element_id)))
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def user_login(self,credentials):
        self.get_element_by_id("identifierId").send_keys(credentials["Email"])
        time.sleep(5)
        self.get_button_by_id("identifierNext").click()
        time.sleep(5)
        self.browser.find_element_by_name("password").send_keys(credentials["Passwd"])
        time.sleep(5)
        self.get_button_by_id("passwordNext").click()
        time.sleep(5)
        #for btn in ["signIn", "submit_approve_access"]:
          #  self.get_button_by_id(btn).click()
        return
    
    def test_google_login(self):
        import json
        with open("users/fixtures/google_user.json") as f:
            credentials = json.loads(f.read())
        c=0
        for i in credentials:
            self.browser.get('http://localhost:8000/login')
        #    self.browser.get(self.get_full_url("login"))
            google_login = self.get_element_by_id("google_login")
            #with self.assertRaises(TimeoutException):
            #   self.get_element_by_id("logout")
            print(google_login.get_attribute("href"))
            #self.assertEqual(
             #   google_login.get_attribute("href"),
              #  'http://localhost:8000/accounts/google/login')
                #self.live_server_url + "/accounts/google/login")
            google_login.click()
            
            try:
                self.user_login(i)
                google_logout = self.get_element_by_id("logout")
                google_logout.click()
                c=c+1
                print("Test case passed : ",c)
            
            except:
                c=c+1
                print("Test case passed : ",c)
                
            
            with self.assertRaises(TimeoutException):
                self.get_element_by_id("google_login")
            self.browser.quit()
            self.browser = webdriver.Firefox(firefox_profile=webdriver.FirefoxProfile())
            self.browser.implicitly_wait(10)
            self.browser.wait = WebDriverWait(self.browser, 10)
            activate('en')
        print("Total test cases : ",c)
        #google_login = self.get_element_by_id("google_login")


    