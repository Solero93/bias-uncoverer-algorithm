from src.domain.value_objects.DataSetSource import DataSetSource
from src.infrastructure.parse.ReadDataFrameFromCSV import ReadDataFrameFromCSV
from src.infrastructure.parse.ReadDataFrameFromDataSetStrategy import ReadDataFrameFromDataSetStrategy


class ReadDataFrameFromDataSetStrategyFactory:
    def create(self, data_set_source: DataSetSource) -> ReadDataFrameFromDataSetStrategy:
        if data_set_source.isCSV():
            return ReadDataFrameFromCSV()

        return None
