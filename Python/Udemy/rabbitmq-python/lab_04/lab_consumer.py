import os
import sys
import pika



def main():
    # 1. Create connection
    credentials = pika.PlainCredentials('bugs', 'bugs01')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    # 2. Create Channel to communicate with exchange
    channel = connection.channel()

    # 3.Create Exchange if it does not exists
    channel.exchange_declare(exchange="Alerts", exchange_type="topic")

    # 4 Create the queue if it does not exists.
    channel.queue_declare(queue="Alert System")

    # 5. Define Callback function for pull reading
    def callback(ch, method, properties, body):
        alert_type = body.split(b":")[0].lower().strip().decode("utf-8")
        alert_priority = body.split(b":")[1].lower().strip().decode("utf-8")
        channel.basic_publish(exchange="Alerts", routing_key=f"{alert_type}.{alert_priority}", body=body)
        print(f"-> New Alert: Routing to {alert_type}.{alert_priority}...")

    # Associate callback with the message queue
    # auto_ack acknowledges the message on read and deletes it
    channel.basic_consume(queue="Alert System", on_message_callback=callback, auto_ack=True)

    print("[*] Waiting for messages...")
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
