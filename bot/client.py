import logging
from binance.client import Client


class BinanceFuturesClient:
    """
    Wrapper around Binance Futures Testnet client.
    """
    TESTNET_URL = "https://testnet.binancefuture.com"
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = self.TESTNET_URL
        
    def set_leverage(self, symbol, leverage=1):
        self.client.futures_change_leverage(
        symbol=symbol,
        leverage=leverage
    )
            
    def place_order(self, order_params):
        logging.info(f"Placing order: {order_params}")
        response = self.client.futures_create_order(**order_params)
        logging.info(f"Order response: {response}")
        return response
