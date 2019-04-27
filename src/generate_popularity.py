from typing import Dict

from pandas import DataFrame


def generate_popularity(data_frame: DataFrame) -> Dict:
    return data_frame['movie'].value_counts().to_dict()
