import json

from configparser import ConfigParser
from confluent_kafka import Producer, Consumer
from producto import Producto

config_parser = ConfigParser(interpolation=None)
config_file = open('config.properties', 'r')
config_parser.read_file(config_file)
producer_config = dict(config_parser['kafka_client'])
consumer_config = dict(config_parser['kafka_client'])
consumer_config.update(config_parser['consumer'])
store_producer = Producer(producer_config)

order_warmer = {"valor":[]}

def load_orders():
    product_consumer = Consumer(consumer_config)
    product_consumer.subscribe(['store-product'])
    while True:
        event = product_consumer.poll(1.0)
        if event is None:
            pass
        elif event.error():
            print(f'Bummer - {event.error()}')
        else:
            product = json.loads(event.value())
            a = order_warmer["valor"]
            a.append(product)


def send_product(name):
    producto = Producto(name)
    store_producer.produce('store-name', value=producto.toJSON())
    store_producer.flush()
    return "Send"

def launch_consumer():
    print("before_first_request")
    '''t = Thread(target=store_service.load_orders)
    t.start()'''
