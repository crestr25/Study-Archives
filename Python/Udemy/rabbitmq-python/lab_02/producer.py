import pika


# Create Connection
credentials = pika.PlainCredentials('bugs', 'bugs01')
params = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(params)

# create channel
channel = connection.channel()

# Create fanout exchange (if it does not exist)
channel.exchange_declare(exchange="ch_exchange", exchange_type="fanout")

# publish message, routing key is empty since the type is fanout
channel.basic_publish(exchange="ch_exchange", routing_key="", body="holis")

# delete exchange, if_unused would delete only if there were no queues associated
channel.exchange_delete(exchange="ch_exchange", if_unused=False)

# Close connection
connection.close()
