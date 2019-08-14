import numpy as np

from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class RandomRecommender(RecommenderAlgorithmStrategy):
    def run(self, strategy_context: RecommenderAlgorithmStrategyContext) -> np.ndarray:
        # TODO See how to obtain these column names automatically
        all_items: np.ndarray = strategy_context.data_set['movie_id']
        all_users: np.ndarray = strategy_context.data_set['user_id']
        all_recommendations: np.ndarray = np.random.choice(
            all_items, size=(all_users.size, strategy_context.number_of_recommendations)
        )
        return all_recommendations
