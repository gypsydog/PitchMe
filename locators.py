from selenium.webdriver.common.by import By


class MainPageLocators(object):
    CANDIDATES = (By.XPATH, "//html[@id='html']//div[@id='gatsby-focus-wrapper']"
                            "//div[@class='ContentContainer-sc-1dy0npt-0 iSpLvl']"
                            "/div/nav[@class='DesktopHeader__StyledNav-sc-1nyqt2b-5 eCsHfx']//a[@href='/candidates']")


class CandidatesPageLocators(object):
    FIND_A_JOB = (By.XPATH,
                  "//html[@id='html']//section[@id='what-is-it']"
                  "//div[@class='ContentContainer-sc-1dy0npt-0 MainSection___StyledContentContainer-sc-12uaysy-1 YxMJ']"
                  "/div[2]//a[@href='/signup/candidate']")


class SignUpPageLocators(object):
    VIA_EMAIL = (By.XPATH, "/html/body[@class='show-cookie-policy']"
                           "//form[@action='#']/div[1]/div[3]/"
                           "button[@type='button']/p[.='Via email']")
    FIRST_NAME = (By.XPATH, "/html/body[@class='show-cookie-policy']/div[2]/div"
                            "//form[@action='#']//input[@name='first_name']")
    LAST_NAME = (By.XPATH, "/html/body[@class='show-cookie-policy']/div[2]/div"
                           "//form[@action='#']//input[@name='last_name']")
    EMAIL = (By.XPATH, "/html/body[@class='show-cookie-policy']/div[2]/div"
                       "//form[@action='#']//input[@name='email']")
    PASSWORD = (By.XPATH, "/html/body[@class='show-cookie-policy']/div[2]/div"
                          "//form[@action='#']//input[@name='password']")
    GET_STARTED = (By.XPATH, "/html/body[@class='show-cookie-policy']/div[2]"
                             "//form[@action='#']//button[@type='submit']")


class OnBoardingPageLocators(object):
    CHOOSE_ROLE = (By.XPATH, "/html//input[@id='mui-6']")
