import unittest
from typing import Dict

from pandas import Series

from src.bias.PopularityBias import PopularityBias


class PopularityBiasTest(unittest.TestCase):
    def test_analyze(self):
        # GIVEN
        input_data_frame: Series = Series(data=[2, 3, 2])
        popularity_bias: PopularityBias = PopularityBias()

        # WHEN
        actual: Dict = popularity_bias.analyze(input_data_frame)

        # THEN
        expected: Dict = {2: 2, 3: 1}
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
