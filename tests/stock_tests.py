import unittest
from lib.car import Car
from lib.stock import Stock

#car1 = Car(1, "punto", "fiat", 3, "SUV")
#car2 = Car(1, "punto", "fiat", 3, "SUV")
stock = Stock(79)

class StockTestCase(unittest.TestCase) : 

    def test_stock_init(self) : 
        """Test de l'initialisation du stock"""

    def test_stock_print(self) : 
        """Test du print de la fraction"""
        self.assertEqual(1,1, "Fraction()" )



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    