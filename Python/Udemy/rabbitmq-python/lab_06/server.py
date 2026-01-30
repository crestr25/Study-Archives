import pika

## Function ##

def fact(n):
    if n <= 1:
        return 1

    return n + fact(n-1)

def on_request(ch, method, props, body):
    reply_queue_name = props.reply_to
    corr_id = props.correlation_id
    n = int(body)
    print(f"called fact({n})")
    response = fact(n)
    ch.basic_publish(exchange='', routing_key=reply_queue_name, properties=pika.BasicProperties(correlation_id=corr_id), body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)


# Setup Connection
creds = pika.PlainCredentials('bugs', 'bugs01')
params = pika.ConnectionParameters('localhost', 5672, '/', creds)
connection = pika.BlockingConnection(params)

# Create Channel
channel = connection.channel()

# Create Queue
queue_name = "rpc_server_queue"
channel.queue_declare(queue=queue_name, durable=True)

# Consume
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name, on_message_callback=on_request)

print("Awaiting RPC requests...")
channel.start_consuming()
