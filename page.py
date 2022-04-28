import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from locators import MainPageLocators, SignUpPageLocators, CandidatesPageLocators, OnBoardingPageLocators
from logger import step


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    @step('Click "Candidates" tab')
    def click_candidates(self):
        element = WebDriverWait(self.driver, timeout=5)\
            .until(method=condition.presence_of_element_located(MainPageLocators.CANDIDATES),
                   message='No "Candidates" tab found on page')
        element.click()
        return CandidatesPage(self.driver)


class CandidatesPage(BasePage):
    @step('Click "Find a job" button')
    def click_find_a_job(self):
        element = WebDriverWait(self.driver, timeout=5)\
            .until(method=condition.presence_of_element_located(CandidatesPageLocators.FIND_A_JOB),
                   message='No "Find a job" button found on page')
        element.click()
        return SignupPage(self.driver)


class SignupPage(BasePage):
    @step('Click "Via email" button')
    def click_via_email_button(self):
        element = WebDriverWait(self.driver, timeout=5)\
            .until(method=condition.presence_of_element_located(SignUpPageLocators.VIA_EMAIL),
                   message='No "Via email" button found on page')
        element.click()

    @step('Set "First name" field')
    def set_first_name(self, first_name):
        element = self.driver.find_element(*SignUpPageLocators.FIRST_NAME)
        element.send_keys(first_name)
        allure.attach(f'Set "{first_name}"')

    @step('Set "Last name" field')
    def set_last_name(self, last_name):
        element = self.driver.find_element(*SignUpPageLocators.LAST_NAME)
        element.send_keys(last_name)
        allure.attach(f'Set "{last_name}"')

    @step('Set "Email" field')
    def set_email(self, email):
        element = self.driver.find_element(*SignUpPageLocators.EMAIL)
        element.send_keys(email)
        allure.attach(f'Set "{email}"')

    @step('Set "Password" field')
    def set_password(self, password):
        element = self.driver.find_element(*SignUpPageLocators.PASSWORD)
        element.send_keys(password)
        allure.attach(f'Set "{password}"')

    @step('Click "Get started" button')
    def click_get_started_button(self):
        element = self.driver.find_element(*SignUpPageLocators.GET_STARTED)
        element.click()
        return OnBoardingPage(self.driver)


class OnBoardingPage(BasePage):
    @step('Get "Choose role" element')
    def get_choose_role_element(self):
        element = WebDriverWait(self.driver, timeout=5)\
            .until(method=condition.presence_of_element_located(OnBoardingPageLocators.CHOOSE_ROLE),
                   message='No "Choose role" element found on page')
        return element
