import json

import pika

from src.domain.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository


class RabbitMQAnalysisResult(AnalysisResultRepository):
    def store(self, analysis_result: AnalysisResult) -> None:
        credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
        parameters = pika.ConnectionParameters(credentials=credentials)
        connection = pika.BlockingConnection(parameters=parameters)  # TODO Change to poll every so many seconds
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()
        channel.confirm_delivery()

        channel.basic_publish(
            exchange='test2',
            routing_key='test2',
            body=json.dumps(analysis_result.serialize()),
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=1
            ),
            mandatory=True
        )
