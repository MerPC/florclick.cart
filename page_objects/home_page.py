from selenium.webdriver.common.by import By


class HomePage:
    FIRST_PRODUCT_XPATH = '//*[@id="inicio"]/section[2]/div/div[2]/div/div[1]'
    SECOND_PRODUCT_XPATH = '//*[@id="inicio"]/section[2]/div/div[2]/div/div[2]'
    CART_BUTTON_XPATH = '/html/body/div[1]/header/div/div/div[3]/div/nav/ul/li[12]/div/a/i'

    def __init__(self, driver, test_context_obj):
        self.driver = driver
        self.test_context_obj = test_context_obj

    def click_to_first_product(self):
        self.driver.find_element(By.XPATH, self.FIRST_PRODUCT_XPATH).click()

    def click_to_second_product(self):
        self.driver.find_element(By.XPATH, self.SECOND_PRODUCT_XPATH).click()

    def go_to_cart(self):
        self.driver.find_element(By.XPATH, self.CART_BUTTON_XPATH).click()

