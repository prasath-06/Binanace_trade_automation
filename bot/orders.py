def build_order_params(args):
    params = {
        "symbol": args.symbol.upper(),
        "side": args.side,
        "type": args.order_type,
        "quantity": args.quantity
    }

    if args.order_type == "LIMIT":
        params["price"] = args.price
        params["timeInForce"] = "GTC"

    return params
