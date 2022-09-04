class TestContext:

    def __init__(self):
        self.product_price_1 = None
        self.product_price_2 = None

    def set_product_price_1(self, price_product):
        self.product_price_1 = price_product

    def set_product_price_2(self, price_product):
        self.product_price_2 = price_product

    def get_suma(self):
        return str(self.product_price_1 + self.product_price_2) + '0 €'
