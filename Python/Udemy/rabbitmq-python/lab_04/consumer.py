import os
import sys
import threading
import pika

def main(routing_key):
    # Set Connection
    cred = pika.PlainCredentials('bugs', 'bugs01')
    params = pika.ConnectionParameters('localhost', 5672, '/', cred)
    connection = pika.BlockingConnection(params)

    # Create Channel
    channel = connection.channel()

    # Create the exchange
    channel.exchange_declare(exchange="system_exchange", exchange_type="topic")

    # Create queue
    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    # Bind queue to exchange
    channel.queue_bind(exchange="system_exchange", queue=queue_name, routing_key=routing_key)

    # set up the consume
    def callback(ch, method, properties, body):
        print(f"[x] {routing_key} Message -> {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    # Start consuming
    channel.start_consuming()

if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=main, args=("#.A3.#",))
        t2 = threading.Thread(target=main, args=("#.#.C2",))
        t3 = threading.Thread(target=main, args=("E.#",))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
