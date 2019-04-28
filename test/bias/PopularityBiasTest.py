import unittest
from collections import Counter
from typing import Dict

from pandas import Series

from src.bias.PopularityBias import PopularityBias


class PopularityBiasTest(unittest.TestCase):
    def test_analyze(self):
        # GIVEN
        input_data = [2, 3, 2, 2, 1]
        series: Series = Series(data=input_data)
        popularity_bias: PopularityBias = PopularityBias()

        # WHEN
        actual: Dict = popularity_bias.analyze(series)

        # THEN
        expected: Dict = Counter(input_data)
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
