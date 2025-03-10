import os
import sys
import pika

def main():
    # Create Connection
    credentials = pika.PlainCredentials('bugs', 'bugs01')
    params = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(params)

    # Create the channel
    channel = connection.channel()

    # Create the exchange (if it does not exists)
    channel.exchange_declare(exchange="ch_exchange", exchange_type="fanout")

    # Create the queue and make it client exclusive
    result = channel.queue_declare(queue="", exclusive=True)
    # Access the dynamic queue name
    queue_name = result.method.queue
    print(f"-> Subscriber exclusive queue name: {queue_name}")

    # Bind queue with exchange
    channel.queue_bind(exchange="ch_exchange", queue=queue_name)

    def callback(ch, method, properties, body):
        print(f"[*] -> Message: {body}")
    
    # Associate callback function with message queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

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
