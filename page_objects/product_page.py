
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class ProductPage:
    ADD_TO_CART_XPATH = '//*[@id="product-page"]/div/div/div[2]/div[2]/div/form/button'
    COMPLEMENT_XPATH = '//section[@id="complementos"]/div/div/button/span[text() = "Continuar"]'
    DEDICATORY_XPATH = '//*[@id="dedicatoria"]/div[4]/div/button[1]/span'
    DEDICATORY_ALERT_XPATH = '/html/body/div[5]/div[7]/div/button'
    PRODUCT_PRICE_XPATH = '//div[@class="col-md-7"]//div[@class="p-price"]'

    def __init__(self, driver, test_context_obj):
        self.driver = driver
        self.test_context_obj = test_context_obj

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.ADD_TO_CART_XPATH).click()

    def get_price(self, number):
        price_product = float((self.driver.find_element(By.XPATH, self.PRODUCT_PRICE_XPATH)).text.replace('€', ''))
        if number == '1':
            self.test_context_obj.set_product_price_1(price_product)
        elif number == '2':
            self.test_context_obj.set_product_price_2(price_product)

    def select_complement(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((ec.element_to_be_clickable(self.driver.find_element(By.XPATH, self.COMPLEMENT_XPATH)))).click()

    def add_dedicatory(self):
        self.driver.find_element(By.XPATH, self.DEDICATORY_XPATH).click()
        self.driver.find_element(By.XPATH, self.DEDICATORY_ALERT_XPATH).click()
