import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task-queue', durable=True)


def callback(ch, method, properties, body):
    print('Consumed... {}'.format(body))


try:
    print('Consuming...')

    channel.basic_consume(callback, queue='task-queue', no_ack=True)
    channel.start_consuming()

except:
    connection.close()
