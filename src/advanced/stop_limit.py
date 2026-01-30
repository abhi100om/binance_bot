import sys
from src.client import BinanceFuturesClient
from src.validators import validate_side, validate_quantity, validate_price

def main():
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py SYMBOL BUY/SELL QTY STOP_PRICE LIMIT_PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    stop_price = float(sys.argv[4])
    limit_price = float(sys.argv[5])

    validate_side(side)
    validate_quantity(quantity)
    validate_price(stop_price)
    validate_price(limit_price)

    client = BinanceFuturesClient()

    order = client.place_order(
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        stopPrice=stop_price,
        price=limit_price,
        timeInForce="GTC"
    )

    print("✅ Stop-Limit Order Placed")
    print(f"Order ID: {order['orderId']}")

if __name__ == "__main__":
    main()
