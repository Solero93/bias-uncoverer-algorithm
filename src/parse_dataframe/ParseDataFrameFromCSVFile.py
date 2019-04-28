from typing import Text

from pandas import DataFrame

from src.parse_dataframe.ParseDataFrameStrategy import ParseDataFrameStrategy


class ParseDataFrameFromCSVFile(ParseDataFrameStrategy):
    def parse(self, input_data: Text) -> DataFrame:
        return DataFrame.from_csv(input_data)
