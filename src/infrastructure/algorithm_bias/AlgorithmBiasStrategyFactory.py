from src.domain.value_objects.BiasCode import BiasCode
from src.infrastructure.algorithm_bias.PopularityAlgorithmBias import PopularityAlgorithmBias


class AlgorithmBiasStrategyFactory:
    def create(self, bias_code: BiasCode):
        if bias_code == BiasCode('popularity'):
            return PopularityAlgorithmBias()

        return None
