import os
import logging
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# ✅ Official Futures Testnet URL
FUTURES_TESTNET_URL = "https://testnet.binancefuture.com"

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

class BinanceFuturesClient:
    def __init__(self):
        if not API_KEY or not API_SECRET:
            raise ValueError("❌ API keys not found in .env")

        # ✅ testnet=True is CRITICAL
        self.client = Client(
            API_KEY,
            API_SECRET,
            testnet=True
        )

        # ✅ Override futures endpoint explicitly
        self.client.FUTURES_URL = FUTURES_TESTNET_URL

        logging.info("✅ Binance Futures Testnet client ready")

    def place_order(self, **order_params):
        try:
            logging.info(f"Placing order: {order_params}")

            response = self.client.futures_create_order(
                **order_params,
                recvWindow=5000
            )

            logging.info(f"Order response: {response}")
            return response

        except Exception as e:
            logging.error(str(e), exc_info=True)
            raise
