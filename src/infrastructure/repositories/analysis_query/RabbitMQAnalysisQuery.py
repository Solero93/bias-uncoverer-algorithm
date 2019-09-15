import json

import pika

from src.domain.AnalysisQuery import AnalysisQuery
from src.domain.repositories.AnalysisQueryRepository import AnalysisQueryRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.AnalysisID import AnalysisID
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.infrastructure.rabbitmq.connection import get_connection


class RabbitMQAnalysisQuery(AnalysisQueryRepository):
    def get_query(self) -> AnalysisQuery:
        connection: pika.BlockingConnection = get_connection()
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

        method_frame, properties, body = channel.consume(queue='test', auto_ack=True).__next__()
        analysis_query_dict: dict = json.loads(body)

        connection.close()

        return AnalysisQuery(
            analysis_id=AnalysisID(analysis_query_dict['analysis_id']),
            data_set_source=DataSetSource(analysis_query_dict['data_set_source']),
            bias_code=BiasCode(analysis_query_dict['bias_code']),
            algorithm_code=AlgorithmCode(analysis_query_dict['algorithm_code'])
        )
