import os
import sys
import threading
import pika



def main(routing_key):
    # Create Connection
    credentials = pika.PlainCredentials('bugs', 'bugs01')
    params = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(params)

    # Create the channel
    channel = connection.channel()

    # Create the exchange (if it does not exists)
    channel.exchange_declare(exchange="Alerts", exchange_type="topic")

    # Create the queue and make it client exclusive
    result = channel.queue_declare(queue="", exclusive=True)
    # Access the dynamic queue name
    queue_name = result.method.queue

    # Bind queue with exchange
    channel.queue_bind(exchange="Alerts", queue=queue_name, routing_key=routing_key)

    # Callback function
    def callback(ch, method, properties, body):
        print(f"-> queue: {queue_name}")
        print(f"-> New Alert - Level {routing_key.upper()}")
        print(f"-> Message: {body}")

    # Associate callback with the message queue
    # auto_ack acknowledges the message on read and deletes it
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("[*] Waiting for messages...")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        t1 = threading.Thread(target=main, args=("#.high",))
        t2 = threading.Thread(target=main, args=("alert.#",))
        t3 = threading.Thread(target=main, args=("complaint.high",))
        t4 = threading.Thread(target=main, args=("#.#",))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
