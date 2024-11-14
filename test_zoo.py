import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)

    # Add your additional test cases here.

    def test_ticket1_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        
    def test_ticket2_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_ticket3_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_ticket4_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_ticket5_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None)
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
        self.assertEqual(self.zoo.get_ticket_price(55), 150)

if __name__ == '__main__':
    unittest.main()