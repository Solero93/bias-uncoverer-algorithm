from src.domain.value_objects.BiasCode import BiasCode
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.PopularityDataBias import PopularityDataBias


class DataBiasStrategyFactory:
    def create(self, bias_code: BiasCode) -> DataBiasStrategy:
        if bias_code == BiasCode('popularity'):
            return PopularityDataBias()

        # TODO Raise exception or default strategy?
        return None
