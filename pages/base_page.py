from urllib.parse import urlparse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import base_url

class BasePage(object):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.driver.implicitly_wait(timeout)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Not found{locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f'Not found{locator}')

    def get_current_url(self):
        return self.driver.current_url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path