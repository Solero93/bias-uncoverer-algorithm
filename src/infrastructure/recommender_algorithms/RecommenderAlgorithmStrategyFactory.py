from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.infrastructure.recommender_algorithms.RandomRecommender import RandomRecommender
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy


class RecommenderAlgorithmStrategyFactory:
    def create(self, algorithm_code: AlgorithmCode) -> RecommenderAlgorithmStrategy:
        if algorithm_code == AlgorithmCode('random'):
            return RandomRecommender()

        return None  # TODO See what to do here
