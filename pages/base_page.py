import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.driver.current_url
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст элемента")
    def send_keys_to_input(self, locator, keys, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.text
    
    @allure.step("Подождать и проверить, что атрибут элимента содержит текст")
    def wait_for_attribute(self, locator,  attribute, value, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))
    
    @allure.step("Подождать прогрузки страницы")
    def wait_for_page(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_contains(url))    

    @allure.step("Проверка аттрибута у элемента")
    def check_attr(self, locator, attr_name, timeout=TIMEOUT):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attr_name)
    
    @allure.step("Убрать всплывающее окно с куки")
    def click_on_cookie_button(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)
        
    @allure.step("Переход на страницу по индексу")
    def switch_to_window_by_index(self, index: int):
        self.driver.switch_to.window(self.driver.window_handles[index])