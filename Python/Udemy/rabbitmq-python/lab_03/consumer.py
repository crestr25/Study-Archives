import os
import sys
import threading
import pika



def main(log_level1, log_level2):

    # Setup connection
    credentials = pika.PlainCredentials('bugs', 'bugs01')
    params = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(params)

    # Create Channel
    channel = connection.channel()

    # Create Exchange
    channel.exchange_declare(exchange="logs_exchange", exchange_type="direct")

    # Create queue
    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    # Bind queue to exchange, one for each routing_key
    channel.queue_bind(exchange="logs_exchange", queue=queue_name, routing_key=log_level1)
    channel.queue_bind(exchange="logs_exchange", queue=queue_name, routing_key=log_level2)
    channel.queue_bind(exchange="logs_exchange", queue=queue_name, routing_key="OK")

    # create callback
    def callback(ch, method, properties, body):
        print(f"[*] {queue_name} There is a new error: {body}")

    # start consuming
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        T1 = threading.Thread(target=main, args=("ERROR", "WARN"))
        T2 = threading.Thread(target=main, args=("INFO", "DEBUG"))
        T1.start()
        T2.start()
        T1.join()
        T2.join()
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
