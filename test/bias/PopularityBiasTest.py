import unittest
from typing import Dict

from pandas import DataFrame

from src.bias.PopularityBias import PopularityBias


class PopularityBiasTest(unittest.TestCase):
    def test_execute(self):
        # GIVEN
        input_data_frame: DataFrame = DataFrame(data={'user': [2, 2, 1], 'movie': [2, 3, 2], 'rating': [1, 2, 3]})
        popularity_bias: PopularityBias = PopularityBias()

        # WHEN
        actual: Dict = popularity_bias.execute(input_data_frame)

        # THEN
        expected: Dict = {2: 2, 3: 1}
        self.assertDictEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()