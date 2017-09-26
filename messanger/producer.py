import pika
import time
import sys


connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='pub-sub', exchange_type='fanout')

channel.queue_declare(queue='task-queue', durable=True)


try:
    counter = 0
    while True:
        line = sys.stdin.readline()

        message = line

        channel.basic_publish(exchange='pub-sub', routing_key='', body=message,
            properties=pika.BasicProperties(
                delivery_mode = 2,
                ))

        print('Published... {}'.format(message))

        time.sleep(1)
        counter += 1

except:
    connection.close()
