from flask import Flask
from threading import Thread
import json
import store_service

rest_port = 5000
app = Flask(__name__)


@app.route('/product/<name>', methods=['POST'])
def name_product(name):
    product_id = store_service.send_product(name)
    return json.dumps(store_service.order_warmer)


@app.route('/product/list', methods=['GET'])
def list_product():
    return json.dumps(store_service.order_warmer)


if __name__ == '__main__':
    t = Thread(target=store_service.load_orders)
    t.start()
    app.run(host='0.0.0.0', port=rest_port)


#@app.before_first_request
#def launch_consumer():
    #print("before_first_request")
    '''t = Thread(target=store_service.load_orders)
    t.start()'''
