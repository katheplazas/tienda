from flask import Flask
from threading import Thread
import json
import store_service
import asyncio

rest_port = 5000
app = Flask(__name__)
order_warmer = None


@app.route('/product/<name>', methods=['POST'])
async def name_product(name):
    print(f'order warmer 1: {order_warmer}')
    product_id = await store_service.send_product(name)
    print(f'order warmer 2: {order_warmer}')
    return product_id


@app.route('/product/list', methods=['GET'])
def list_product():
    return json.dumps(store_service.order_warmer)


if __name__ == '__main__':
    t = Thread(target=store_service.load_orders)
    t.start()
    app.run(host='0.0.0.0', port=rest_port)

    # @app.before_first_request
    # def launch_consumer():
    # print("before_first_request")
    '''t = Thread(target=store_service.load_orders)
    t.start()'''
