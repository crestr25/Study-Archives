import random
import pika


# Set Connection
cred = pika.PlainCredentials('bugs', 'bugs01')
params = pika.ConnectionParameters('localhost', 5672, '/', cred)
connection = pika.BlockingConnection(params)

# Create Channel
channel = connection.channel()

# Create exchange
channel.exchange_declare(exchange="system_exchange", exchange_type="topic")

# create messages
severity = ["E", "W", "I"]
priority = ["H", "M", "L"]
action = ["A1", "A2", "A3"]
component = ["C1", "C2", "C3"]

for i in range(10):
    rand_severity = severity[random.randint(0, len(severity)-1)]
    rand_priority = priority[random.randint(0, len(priority)-1)]
    rand_action = action[random.randint(0, len(action)-1)]
    rand_component = component[random.randint(0, len(component)-1)]

    rk = f"{rand_severity}.{rand_priority}.{rand_action}.{rand_component}"
    
    channel.basic_publish(exchange="system_exchange", routing_key=rk, body=f"{rk} - holis")
    print(f"[*] Sent message -> {rk} - holis")

# channel.exchange_delete(exchange="system_exchange", if_unused=False)

# Close connection
channel.close()
