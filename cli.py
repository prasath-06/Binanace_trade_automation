import argparse
import os
import logging

from bot.client import BinanceFuturesClient
from bot.validators import validate_inputs
from bot.orders import build_order_params
from bot.logging_config import setup_logging


def load_api_keys():
    """
    Load API keys from environment variables.
    """
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise EnvironmentError(
            "Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables"
        )

    return api_key, api_secret


def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Simple Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT)")

    args = parser.parse_args()

    try:
        validate_inputs(args)

        api_key, api_secret = load_api_keys()
        client = BinanceFuturesClient(api_key, api_secret)

        order_params = build_order_params(args)

        print("\nOrder Request Summary")
        for key,value in order_params.items():
            print(f"{key}:{value}")

        response = client.place_order(order_params)

        print("\nOrder Placed Successfully")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")

    except Exception as error:
        logging.error(str(error))
        print(f"\nOrder Failed \nReason: {error}")


if __name__ == "__main__":
    main()
