from typing import List

import pandas

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext


class PopularityDataBias(DataBiasStrategy):
    def run(self, strategy_context: DataBiasStrategyContext) -> Graph:
        # TODO See how to obtain this programatically, without hardcoding column
        items: pandas.Series = strategy_context.data_set['item_id']
        number_of_ratings_per_item: pandas.Series = items.value_counts(sort=False)
        number_of_ratings_per_rating: pandas.Series = number_of_ratings_per_item.value_counts(sort=False).sort_index()
        graph_points: List[GraphPoint] = [
            GraphPoint(x=k, y=v) for k, v in number_of_ratings_per_rating.to_dict().items()
        ]  # TODO optimize if necessary
        return Graph(points=graph_points)
