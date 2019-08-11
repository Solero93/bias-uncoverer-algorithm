import json
from typing import Generator

import pika

from src.domain.AnalysisQuery import AnalysisQuery
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource


def get_message() -> Generator[AnalysisQuery, None, None]:
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    parameters = pika.ConnectionParameters(credentials=credentials)
    connection = pika.BlockingConnection(parameters=parameters)  # TODO Change to poll every so many seconds
    channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

    for method_frame, properties, body in channel.consume('test', auto_ack=True):
        analysis_query_dict: dict = json.loads(body)
        yield AnalysisQuery(
            data_set_source=DataSetSource(analysis_query_dict['data_set_source']),
            bias_code=BiasCode(analysis_query_dict['bias_code']),
            algorithm_code=AlgorithmCode(analysis_query_dict['algorithm_code'])
        )

    # Close the channel and the connection
    channel.close()
    connection.close()
