import unittest
from lib.car import Car
from lib.stock import Stock

car1 = Car(1, "punto", "fiat", 3, "SUV")
car2 = Car(2, "v40", "volvo", 5, "SUV")
car3 = Car(3, "Model 3", "Tesla", 3, "SUV")
stock = Stock(2)

class StockTestCase(unittest.TestCase) : 

    def test_astock_add(self) : 
        """Test du add du stock"""
        self.assertEqual(stock.add(car1), 0)
        self.assertEqual(stock.get_cars(), [car1])
        self.assertEqual(stock.add(car2), 1)
        self.assertEqual(stock.get_cars(), [car1, car2])
        self.assertRaises(ValueError, stock.add, car1)
        self.assertRaises(ValueError, stock.add, "car1")
        self.assertRaises(ValueError, stock.add, car3)

    def test_bstock_rent(self) : 
        """Test du rent du stock"""
        self.assertEqual(stock.rent(car1), 0)
        self.assertEqual(stock.rent(car2), 1)
        self.assertRaises(ValueError, stock.rent, car1)
        self.assertRaises(ValueError, stock.rent, car3)
        self.assertRaises(ValueError, stock.rent, "car1")

    def test_cstock_send_back(self) : 
        """Test du send_back du stock"""
        self.assertEqual(stock.send_back(car1), 0)
        self.assertEqual(stock.send_back(car2), 1)
        self.assertRaises(ValueError, stock.send_back, car3)
        self.assertRaises(ValueError, stock.send_back, "car1")

    def test_dstock_remove(self) : 
        """Test du remove du stock"""
        self.assertEqual(stock.remove(car1), 0)
        self.assertEqual(stock.remove(car2), 1)
        self.assertRaises(ValueError, stock.remove, car3)
        self.assertRaises(ValueError, stock.remove, "car1")

    def test_estock_get_rentable(self) : 
        """Test du remove du stock"""
        stock.add(car1)
        self.assertEqual(stock.get_rentable(), [car1])
        stock.add(car2)
        self.assertEqual(stock.get_rentable(), [car1, car2])

    def test_fstock_get_rented(self) : 
        """Test du remove du stock"""
        self.assertEqual(stock.get_rented(), [])
        stock.rent(car1)
        self.assertEqual(stock.get_rented(), [car1])

    def test_gstock_get_cars(self) : 
        """Test du remove du stock"""
        self.assertEqual(stock.get_cars(), [car1, car2])
        stock.add(car3)
        self.assertEqual(stock.get_cars(), [car1, car2, car3])



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    