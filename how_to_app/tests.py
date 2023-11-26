from django.test import TestCase, LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Create your tests here.
class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "how_to_app/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "<h1>Home Page for How to Fix it</h1>")
        self.assertNotContains(response, "Not on the page")

class Hosttest(LiveServerTestCase):
    
    def testhomepage(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        time.sleep(2)

        assert "How To Fix it" in driver.title

class LoginFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://localhost:8000/accounts/login/')

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.NAME, 'password')
        submit = driver.find_element(By.ID, 'submit')

        user_name.send_keys('asdfasdf')
        user_password.send_keys('Cheer2015')

        time.sleep(2)

        submit.send_keys(Keys.RETURN)

        time.sleep(3)
