import random
import pika


# Set Connection
cred = pika.PlainCredentials('bugs', 'bugs01')
params = pika.ConnectionParameters('localhost', 5672, '/', cred)
connection = pika.BlockingConnection(params)

# Create Channel
channel = connection.channel()
# Setup the confirm delivery to mitigate broker disconnections
channel.confirm_delivery()

# Create exchange
# Durable, makes it easier to recreate the exchange with all bindings when the broker restarts
channel.exchange_declare(exchange="system_exchange", exchange_type="direct", durable=True)

# create messages
# The try except is for the delivery confirmation 
try:
    channel.basic_publish(
        exchange="system_exchange",
        routing_key="message",
        body="holis",
        # set up properties
        properties=pika.BasicProperties(
                delivery_mode=2 # Make message persistent, needed with the queue_dechare(durable=True)
            )
        )
    print(f"[*] Sent message -> holis")
except pika.exceptions.ChannelClosed:
    print("Channel closed")
except pika.exceptions.ConnectionClosed:
    print("Channel closed")


channel.exchange_delete(exchange="system_exchange", if_unused=False)

# Close connection
channel.close()
