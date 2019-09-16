from typing import List

import pandas
from pandas import DataFrame

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory


class PopularityDataBias(DataBiasStrategy):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory

    def run(self, strategy_context: DataBiasStrategyContext) -> Graph:
        data_set_source = strategy_context.data_set_source
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))

        # TODO See how to obtain this programatically, without hardcoding column
        items: pandas.Series = data_set['item_id']
        number_of_ratings_per_item: pandas.Series = items.value_counts(sort=False)
        number_of_ratings_per_rating: pandas.Series = number_of_ratings_per_item.value_counts(sort=False).sort_index()
        graph_points: List[GraphPoint] = [
            GraphPoint(x=k, y=v) for k, v in number_of_ratings_per_rating.to_dict().items()
        ]  # TODO optimize if necessary
        return Graph(points=graph_points)
