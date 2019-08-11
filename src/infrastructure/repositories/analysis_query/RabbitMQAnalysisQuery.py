import json
from typing import Generator

import pika

from src.infrastructure.rabbitmq.connection import get_connection
from src.domain.AnalysisQuery import AnalysisQuery
from src.domain.repositories.AnalysisQueryRepository import AnalysisQueryRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.AnalysisID import AnalysisID
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource


class RabbitMQAnalysisQuery(AnalysisQueryRepository):
    def wait_and_get(self) -> Generator[AnalysisQuery, None, None]:
        connection: pika.BlockingConnection = get_connection()
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

        for method_frame, properties, body in channel.consume('test', auto_ack=True):
            analysis_query_dict: dict = json.loads(body)
            yield AnalysisQuery(
                analysis_id=AnalysisID(analysis_query_dict['analysis_id']),
                data_set_source=DataSetSource(analysis_query_dict['data_set_source']),
                bias_code=BiasCode(analysis_query_dict['bias_code']),
                algorithm_code=AlgorithmCode(analysis_query_dict['algorithm_code'])
            )

        channel.close()
        connection.close()
