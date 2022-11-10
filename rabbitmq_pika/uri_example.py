import pika
import urllib
import time

connection = pika.BlockingConnection(pika.URLParameters("amqps://baduser:wXaY0X5c94fV@BER-0803:5671/clienthost"))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print(" [x] Sent 'Hello World!'")
time.sleep(60)
connection.close()
# works 