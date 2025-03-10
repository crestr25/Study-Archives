import pika


# Setup Connection
credentials = pika.PlainCredentials('bugs', 'bugs01')
params = pika.ConnectionParameters('localhost', 5672, "/", credentials)
connection = pika.BlockingConnection(params)

# Create Channel
channel = connection.channel()

# Create Exchange
channel.exchange_declare(exchange="logs_exchange", exchange_type="direct")

# Publish Message
for log_level in ("ERROR", "INFO", "WARN", "DEBUG", "OK"):
    channel.basic_publish(exchange="logs_exchange", routing_key=log_level, body=f"Log level: [{log_level}]")

# Delete Exchange
channel.exchange_delete(exchange="logs_exchange", if_unused=False)

# Close Connection
channel.close()
