import unittest
from typing import Dict

from pandas import DataFrame

from src.generate_popularity import generate_popularity


class GeneratePopularity(unittest.TestCase):
    def test_generate_popularity(self):
        # GIVEN
        df: DataFrame = DataFrame(data={'user': [2, 2, 1], 'movie': [2, 3, 2], 'rating': [1, 2, 3]})

        # WHEN
        actual: Dict = generate_popularity(df)

        # THEN
        expected: Dict = {2: 2, 3: 1}
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
