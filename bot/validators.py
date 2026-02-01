def validate_inputs(args):
    """
    Validate CLI inputs before placing an order.
    """
    if args.side not in ("BUY", "SELL"):
        raise ValueError("side must be BUY or SELL")

    if args.order_type not in ("MARKET", "LIMIT"):
        raise ValueError("order_type must be MARKET or LIMIT")

    if args.quantity <= 0:
        raise ValueError("quantity must be greater than 0")

    if args.order_type == "LIMIT" and args.price is None:
        raise ValueError("price is required for LIMIT orders")
