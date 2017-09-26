import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pub-sub', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='pub-sub', queue=queue_name)


def callback(ch, method, properties, body):
    print(body)


try:
    print('Consuming...')

    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()

except:
    connection.close()
