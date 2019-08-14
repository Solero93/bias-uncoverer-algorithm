import json

import pika

from src.domain.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository
from src.infrastructure.rabbitmq.connection import get_connection


class RabbitMQAnalysisResult(AnalysisResultRepository):
    def store(self, analysis_result: AnalysisResult) -> None:
        connection: pika.BlockingConnection = get_connection()
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

        channel.close()
        connection.close()