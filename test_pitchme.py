import allure
from selenium import webdriver

import pytest

import page
from gen_data import signup_data
from logger import step

HOST = 'https://pitchme.co/'


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


class TestPitchMe:
    @step('Test checking signup process')
    def test_signup(self, driver):

        driver.get(HOST)
        main_page = page.MainPage(driver)

        candidates_page = main_page.click_candidates()
        signup_page = candidates_page.click_find_a_job()

        signup_page.click_via_email_button()
        signup = signup_data()
        signup_page.set_first_name(signup['first_name'])
        signup_page.set_last_name(signup['last_name'])
        signup_page.set_email(signup['email'])
        signup_page.set_password(signup['password'])
        # Uncomment following lines to allow test to submit signup and check it
        on_boarding_page = signup_page.click_get_started_button()
        on_boarding_page.get_choose_role_element()
        driver.save_screenshot('allure-report/screenshot.png')
        allure.attach.file('allure-report/screenshot.png')
