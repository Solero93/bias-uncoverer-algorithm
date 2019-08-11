import pika


def get_connection() -> pika.BlockingConnection:
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    parameters = pika.ConnectionParameters(credentials=credentials)
    return pika.BlockingConnection(parameters=parameters)  # TODO Change to poll every so many seconds
