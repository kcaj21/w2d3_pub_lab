import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Dog and Trumpet", 100.00, ["beer", "wine"])
        self.customer = Customer("Randolph", 100.00, 21, 5)
        self.drink = Drink("beer", 5.00, 4)

    def test_pub_has_name(self):
        self.assertEqual("The Dog and Trumpet", self.pub.name)

    def test_pub_has_till_value(self):
        self.assertEqual(100.00, self.pub.till)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(["beer", "wine"], self.pub.drinks)

    def test_take_from_wallet(self):
        self.customer.reduce_wallet_amount(5.00)
        self.assertEqual(95.00, self.customer.wallet)

    def test_find_drink_price(self):
        self.drink.get_drink_price(self.drink.price)
        self.assertEqual(5.00, self.drink.price)

    def test_check_age(self):
        self.assertEqual(True, self.customer.check_customer_age(21))

    # def test_drunkeness_level(self):
    #     self.customer.check_drunkeness(self.customer.drunkeness)
    #     self.assertEqual(5, self.customer.drunkeness)

    def test_customer_can_buy_drink(self):
        self.customer.check_customer_age(21)
        while self.customer.drunkeness <= 10:
            self.drink.get_drink_price(self.drink.price)
            self.customer.reduce_wallet_amount(self.customer.wallet)
            self.pub.increase_till(self.drink.price)
            self.customer.drunkeness.add_drunkeness(self.drink.strength)
        if self.customer.drunkeness > 10:
            break

    # [ {"drink": "beer", "price": 5.00}, {"drink": "wine", "price": 4.00} ])