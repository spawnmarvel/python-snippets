import ssl
import pika
import logging

# logging.basicConfig(level=logging.INFO)

# https://stackoverflow.com/questions/72306332/python3-deprecationwarning-ssl-protocol-tlsv1-2-is-deprecated-sslcontext-ssl
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('C:/testca/ca_certificate.pem')

# https://pika.readthedocs.io/en/stable/modules/parameters.html
credential = pika.PlainCredentials("baduser", "wXaY0X5c94fV")
# create the vhost at rabbitmq
# http://localhost:15672/#/vhosts

conn_parameters = pika.ConnectionParameters(host="hostname-for-rabbitmq",virtual_host="clienthost", ssl_options=pika.SSLOptions(context), credentials=credential)

conn = pika.BlockingConnection(conn_parameters)
print("\n"+ str(conn))
ch = conn.channel()
ch.queue_declare(queue="ssl-queue", durable=True)
ch.queue_bind("ssl-queue", exchange="amq.direct", routing_key="ssl-q")

ch.basic_publish(exchange="amq.direct", routing_key="ssl-q", body="ssl message",  properties=pika.BasicProperties(content_type='text/plain',delivery_mode=pika.DeliveryMode.Transient))
get_queue_info = ch.basic_get("ssl-queue")
print("\n"+ str(get_queue_info))
conn.close()

# works 

