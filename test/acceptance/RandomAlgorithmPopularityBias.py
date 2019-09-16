import json
import unittest

import pika

from src.infrastructure.rabbitmq.connection import get_connection
from test.acceptance.MainRunOnlyOnce import MainRunOnlyOnce


class RandomAlgorithmPopularityBiasTest(unittest.TestCase):
    def test_stuff(self):
        fixture = {
            "analysis_id": "1",
            "data_set_source": "fixtures/ratings.csv",
            "algorithm_code": "Random Recommender",
            "bias_code": "Popularity"
        }

        connection: pika.BlockingConnection = get_connection()
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

        channel.confirm_delivery()
        channel.basic_publish(
            exchange='test',
            routing_key='test',
            body=json.dumps(fixture),
            properties=pika.BasicProperties(
                content_type='application/json',
                delivery_mode=1
            ),
            mandatory=True
        )

        channel.close()
        connection.close()

        MainRunOnlyOnce().main()

        connection: pika.BlockingConnection = get_connection()
        channel: pika.adapters.blocking_connection.BlockingChannel = connection.channel()

        method_frame, properties, body = channel.basic_get('test2', auto_ack=True)

        channel.close()
        connection.close()

        with open("fixtures/popularity_random_ratings_result.json", "r") as fixture_file:
            # TODO Fails because random recommender is RANDOM, so the result is always different
            self.assertDictEqual(
                json.loads(body),
                json.load(fixture_file),
            )


if __name__ == '__main__':
    unittest.main()
