from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.infrastructure.recommender_algorithms.BiasRatingRecommender import BiasRatingRecommender
from src.infrastructure.recommender_algorithms.ItemAverageRecommender import ItemAverageRecommender
from src.infrastructure.recommender_algorithms.KNNItemToItemRecommender import KNNItemToItemRecommender
from src.infrastructure.recommender_algorithms.KNNUserToUserRecommender import KNNUserToUserRecommender
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
        if algorithm_code == AlgorithmCode('knn-user-to-user'):
            return KNNUserToUserRecommender()
        if algorithm_code == AlgorithmCode('knn-item-to-item'):
            return KNNItemToItemRecommender()
        if algorithm_code == AlgorithmCode('bias-rating'):
            return BiasRatingRecommender()

        # TODO Raise exception or default strategy?
        return None
