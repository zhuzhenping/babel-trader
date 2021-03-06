import time

from trader import Trader


class TraderCancelOrder(Trader):
    def __init__(self, addr):
        Trader.__init__(self, addr=addr)

    def on_confirmorder(self, msg):
        if 'error_id' in msg:
            error_id = msg['error_id']
        else:
            error_id = 0

        outside_id = msg['data']['outside_id']
        order_id = msg['data']['order_id']

        if error_id != 0:
            print("order error: {0} - upstream error id:({1})".format(order_id, error_id))
            return

        if outside_id == "":
            print("order error: {0}".format(order_id))
            return

        self.cancel_order(
            user_id="weidaizi",
            outside_id=outside_id,
            market=msg['data']['market'],
            exchange=msg['data']['exchange'],
            type=msg['data']['type'],
            symbol=msg['data']['symbol'],
            contract=msg['data']['contract'],
            contract_id=msg['data']['contract_id']
        )


def TestInsertOrder_CTP(trader):
    ts = time.time()
    trader.insert_order(
        user_id="weidaizi",
        market="ctp",
        exchange="SHFE",
        type="future",
        symbol="rb",
        contract="1901",
        contract_id="1901",
        order_type="limit",
        order_flag1="speculation",  # speculation, hedge, arbitrage
        dir="open_long",  # [action: open, close, close_today, close_yesterday; dir: long, short] or [buy, sell]
        price=3800,
        amount=1,
        total_price=0,
        ts=ts
    )


def TestInsertOrder_XTP(trader):
    ts = time.time()
    trader.insert_order(
        user_id="weidaizi",
        market="xtp",
        exchange="SSE",
        type="spot",
        symbol="600519",
        contract="",
        contract_id="",
        order_type="limit",
        order_flag1="",  # speculation, hedge, arbitrage
        dir="buy",  # [action: open, close, closetoday, closehistory; dir: long, short] or [buy, sell]
        price=535,
        amount=600,
        total_price=0,
        ts=ts
    )


if __name__ == '__main__':
    # ctp test
    addr = "127.0.0.1:8001"
    fn = TestInsertOrder_CTP

    # xtp test
    # addr = "127.0.0.1:8002"
    # fn = TestInsertOrder_XTP

    trader = TraderCancelOrder(addr)
    fn(trader)

    trader.message_loop()
