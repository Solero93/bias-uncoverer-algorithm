from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.infrastructure.recommender_algorithms.ItemAverageRecommender import ItemAverageRecommender
from src.infrastructure.recommender_algorithms.KNNRecommender import KNNRecommender
from src.infrastructure.recommender_algorithms.MostPopularRecommender import MostPopularRecommender
from src.infrastructure.recommender_algorithms.RandomRecommender import RandomRecommender
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy


class RecommenderAlgorithmStrategyFactory:
    def create(self, algorithm_code: AlgorithmCode) -> RecommenderAlgorithmStrategy:
        if algorithm_code == AlgorithmCode('random'):
            return RandomRecommender()
        if algorithm_code == AlgorithmCode('most-popular'):
            return MostPopularRecommender()
        if algorithm_code == AlgorithmCode('item-average'):
            return ItemAverageRecommender()
        if algorithm_code == AlgorithmCode('knn'):
            return KNNRecommender()

        # TODO Raise exception or default strategy?
        return None
