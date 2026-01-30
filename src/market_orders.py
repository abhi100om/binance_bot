import sys
from src.client import BinanceFuturesClient
from src.validators import validate_side, validate_quantity, validate_symbol

def main():
    print("🚀 Market Order Script Started")

    if len(sys.argv) != 4:
        print("Usage: python -m src.market_orders SYMBOL BUY/SELL QUANTITY")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])

    # Validation
    validate_symbol(symbol)
    validate_side(side)
    validate_quantity(quantity)

    print("✅ Input validated")

    client = BinanceFuturesClient()

    order = client.place_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    print("\n🎯 MARKET ORDER PLACED SUCCESSFULLY")
    print("Order ID:", order.get("orderId"))
    print("Status:", order.get("status"))
    print("Executed Qty:", order.get("executedQty"))
    print("Avg Price:", order.get("avgPrice", "N/A"))

if __name__ == "__main__":
    main()
