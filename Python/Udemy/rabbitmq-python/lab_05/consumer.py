import os
import sys
import time
import threading
import pika

def main():
    # Set Connection
    cred = pika.PlainCredentials('bugs', 'bugs01')
    params = pika.ConnectionParameters('localhost', 5672, '/', cred)
    connection = pika.BlockingConnection(params)

    # Create Channel
    channel = connection.channel()

    # Create the exchange
    # Durable, recreate the exchange
    channel.exchange_declare(exchange="system_exchange", exchange_type="direct", durable=True)

    # Create queue
    # durable, persist the messages marked to be persisted
    channel.queue_declare(queue="task_queue", durable=True)

    # Bind queue to exchange
    channel.queue_bind(exchange="system_exchange", queue="task_queue", routing_key="message")

    # set up the consume
    def callback(ch, method, properties, body):
        print(f"[x] Message -> {body}")
        time.sleep(5)
        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    # The queue will not send more than one message until it receives an ack
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="task_queue", on_message_callback=callback)

    # Start consuming
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
