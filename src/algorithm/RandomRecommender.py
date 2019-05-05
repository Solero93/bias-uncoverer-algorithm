from typing import List

import numpy as np
from pandas import DataFrame

from src.algorithm.RecommenderStrategy import RecommenderStrategy


class RandomRecommender(RecommenderStrategy):
    def analyze(self, input_data: DataFrame) -> List[int]:
        all_movies: np.ndarray = np.unique(input_data['movieId'].get_values())
        all_users: np.ndarray = np.unique(input_data.index.get_values())
        all_recommendations: np.ndarray = np.random.choice(all_movies, size=(all_users.size, 10))
        _, frequency_of_recommendations = np.unique(all_recommendations.flatten(), return_counts=True)
        return (-np.sort(-frequency_of_recommendations)).tolist()
