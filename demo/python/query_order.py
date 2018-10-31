import json
import time
from datetime import datetime

import websocket
import traceback

from trader import Trader

addr = "127.0.0.1:8001"


# addr = "127.0.0.1:8002"


class TraderInsertOrder(Trader):
    def __init__(self):
        Trader.__init__(self)

        self.qry_id = "1"

    def on_qryorder(self, msg):
        if msg['error_id'] != 0:
            print("query error: " + msg['error_id'])
            return

        qry_result = msg['data']['data']
        for data in qry_result:
            print('====================')
            print("status: " + str(data['status']))
            print("order: " + str(data['order']))

if __name__ == '__main__':
    trader = TraderInsertOrder()

    ts = time.time()
    trader.query_order(
        qry_id=trader.qry_id,
        user_id="weidaizi",
        outside_id="",
        market="ctp",
        exchange="SHFE",
        type="future",
        symbol="rb",
        contract="1901",
        contract_id="1901"
    )

    trader.message_loop()