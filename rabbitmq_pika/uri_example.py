import pika
import urllib

connection = pika.BlockingConnection(pika.URLParameters("amqps://baduser:wXaY0X5c94fV@hostname-for-rabbitmq:5671/clienthost"))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print(" [x] Sent 'Hello World!'")
connection.close()
# works 