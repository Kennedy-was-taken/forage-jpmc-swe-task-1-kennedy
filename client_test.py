import unittest
from client3 import getDataPoint


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                'top_ask': {'price': 121.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109},
                'id': '0.109974697771', 'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81},
                'id': '0.109974697771', 'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """
        msg = 'they are not equal'
        for quote in quotes:
            print(str(getDataPoint(quote)))

    def test_getDataPoint_calculatePriceNotEquals(self):
        quotes = [
            {
                'top_ask': {'price': 121.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109},
                'id': '0.109974697771', 'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81},
                'id': '0.109974697771', 'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """
        msg = 'they are not equal'
        for quote in quotes:
            self.assertNotEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price'] / 2)), msg)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                'top_ask': {'price': 119.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109},
                'id': '0.109974697771', 'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 123.87, 'size': 81},
                'id': '0.109974697771', 'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        msg = f'bid_price is not greater than ask_price'
        self.assertTrue(bid_price < ask_price, msg)

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculatePriceAskGreaterThanBid(self):
        quotes = [
            {
                'top_ask': {'price': 120.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 119.2, 'size': 109},
                'id': '0.109974697771', 'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 121.68, 'size': 81},
                'id': '0.109974697771', 'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        msg = 'bid_price is greater than ask_price'
        self.assertTrue(bid_price < ask_price, msg)

    def test_getDataPoint_calculatePriceAskEqualsBid(self):
        quotes = [
            {
                'top_ask': {'price': 119.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 119.2, 'size': 109},
                'id': '0.109974697771', 'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 121.68, 'size': 81},
                'id': '0.109974697771', 'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        msg = 'bid_price is not equal to ask_price'
        self.assertEqual(bid_price, ask_price, msg)


if __name__ == '__main__':
    unittest.main()
