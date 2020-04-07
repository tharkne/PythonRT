# Testing functionality made with help from Arun Ravindran (https://www.youtube.com/channel/UCj7bqdW_FLpzUIzlSbXLp_A)
import unittest
from vector import vec3

class TestVectors(unittest.TestCase):


    def setUp(self):
        self.v1 = vec3(1.0, -2.0, -2.0)
        self.v2 = vec3(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assetEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        self.v1 + self.v2
        self.assertEqual(getattr(sum, "x"), 4.0)

if __name__ == "__main__":
    unittest.main()
