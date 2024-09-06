import unittest
from pb_rater_example import rater

class TestCalculations(unittest.TestCase):

    def test_rate_calculation(self):
        json_input = {"Asset Size": 1_200_000, "Limit": 5_000_000, "Retention": 1_000_000, "Industry": "Hazard Group 2"}
        
        self.assertEqual(rater.execute(json_input), 4343, 'The rate is wrong.')

if __name__ == '__main__':
    unittest.main()