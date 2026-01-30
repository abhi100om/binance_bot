import sys
from src.client import BinanceFuturesClient
from src.validators import (
    validate_side,
    validate_quantity,
    validate_price,
    validate_symbol
)

def main():
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL BUY/SELL QUANTITY PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    price = float(sys.argv[4])

    validate_symbol(symbol)
    validate_side(side)
    validate_quantity(quantity)
    validate_price(price)

    client = BinanceFuturesClient()

    order = client.place_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    print("✅ Limit Order Placed Successfully")
    print(f"Order ID: {order['orderId']}")
    print(f"Status: {order['status']}")

if __name__ == "__main__":
    main()
