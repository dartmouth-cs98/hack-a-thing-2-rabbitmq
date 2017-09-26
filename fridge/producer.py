import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task-queue', durable=True)

foods = ['candy', 'orange', 'apple', 'tomato', 'banana', 'rice', 'chicken', 'beef', 'pork', 'pork chop', 'snickers', 'soda', 'sprite', 'dr. pepper', 'bread', 'rolls', 'doritos', 'cheetos', 'tea', 'lemonade', 'gum', 'pepsi', 'coke', 'ice cream', 'mint gum']
try:
    counter = 0

    while True:
        for food in foods:
            message = food

            channel.basic_publish(exchange='',
                                  routing_key='task-queue',
                                  body=message)

            print('I put {} on the counter'.format(food))

            time.sleep(1)
            counter += 1

except:
    connection.close()
