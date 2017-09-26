# Hack-a-thing Rabbitmq

## Description
I just tried to figure out how to create a messanging back-end. I messed around with the rabbitMQ tutorials and figured out the different types of exchanges and queues and how each one of them work. https://www.rabbitmq.com/getstarted.html  

Fridge uses a task-queue. A bunch of messages are published to an exchange. Those messages remain in the exchange until a consumer is activated. The consumer is consume all the messages that is in the queue. If multiple consumers are activated, they will take turns consuming the messages in the queue. 

Messanger imitates a messanging backend. It uses a pub-sub type design. This is a bit different than the fridge. With the fridge, the producer created the single exchange while with messanger, each consumer creates it own exchange and attaches itself to the producer. 

## Responsibilities
I originally was working with Barry on a Chrome extension. But we soon realized that there wasn't enough work for the both of us on the hack-a-thing so I split off to explore a messanging broker. 

## What you learned
I learned about how a messanging broker works and what it can be used for. I created an elementary backend for a messanging back-end. 

## What didn't work
With the fridge, the producer can be running for a long time and when a consumer attached itself to the exchange, it will consume all the messages in that exchange. However, when it came to the messanger, because multiple consumers can be attached, each consumer had to create its own exchange on the fly. As a result, whenever a consumer was attached, it would only get the messages that were published after it was attached. To get around this some more complicated logic is required with storing all the previous messages and publishing them all at once whenever a new exchange is attached.
