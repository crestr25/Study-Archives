import pika

# 1. Create connection
credentials = pika.PlainCredentials('bugs', 'bugs01')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

# 2. Create Channel to communicate with exchange
channel = connection.channel()

# 3. [optional] Create an exchange and specify bindings
# 3.1 Create the queue if it does not exists.
channel.queue_declare(queue="Alert System")

# Publish message
print("-> Alert System")
message = input("-> What is your emergency: ")

channel.basic_publish(exchange="", routing_key="Alert System", body=message)
print("[*] Alert Sent!")

# Close the connection
channel.close()
