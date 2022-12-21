import unittest
from lib.car import Car


class CarTestCase(unittest.TestCase):

    def test_is_rentable(self):
        """Test of the rentability of a car """
        self.assertRaises(TypeError,
                          Car(1, "punto", "fiat", 69, "citadine", "20-12-2021", 0, 0, 0).last_vehicle_safety_insurance)
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 0, 0, 0).is_rentable(), True, "devrait "
                                                                                                             "donner "
                                                                                                             "True")
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2020-12-12", 0, 0, 0).is_rentable(), False, "devrait "
                                                                                                              "donner "
                                                                                                              "False")

    def test_is_rented(self):
        """Test the good value for is ranted is entered"""
        self.assertRaises(ValueError,
                          Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 0, 23, 0).is_rented)
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 0, 1, 0).is_rented(), True, "devrait "
                                                                                                           "donner "
                                                                                                           "True")
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 0, 0, 0).is_rented(), False, "devrait "
                                                                                                            "donner "
                                                                                                            "False")

    def test_is_sold(self):
        """Test the good value for is ranted is entered"""
        self.assertRaises(ValueError,
                          Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 34, 0, 0).is_sold)
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 1, 0, 0).is_sold(), True, "devrait "
                                                                                                         "donner True")
        self.assertEqual(Car(1, "punto", "fiat", 69, "citadine", "2022-12-12", 0, 0, 0).is_sold(), False, "devrait "
                                                                                                          "donner "
                                                                                                          "False")


if __name__ == '__main__':
    unittest.main()
