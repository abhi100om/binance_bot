# Binance Futures Trading Bot (USDT-M Testnet)

## 🚀 Overview
This is a **CLI-based Python trading bot** built for **Binance USDT-M Futures Testnet**.  
It supports **Market and Limit orders**, with proper **input validation**, **structured logging**, and **secure API handling**.

This bot is designed for **testing & evaluation** using Binance Futures **Testnet** (no real money involved).

---

## 🧠 Features
- Place **Market Orders**
- Place **Limit Orders**
- Support for **BUY / SELL**
- **Command-line interface**
- Input validation (symbol, side, quantity, price)
- **Structured logging** to file
- Secure authentication via **environment variables**
- Clean, modular, extensible code structure

---

## 🛠️ Tech Stack
- **Python 3.x**
- Binance USDT-M Futures API (Testnet)
- Libraries:
  - `python-binance`
  - `python-dotenv`
- Tools: Git & GitHub

---

## 📁 Project Structure
```
binance_bot/
├── src/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── validators.py # Input validation
│ ├── market_orders.py # Market order CLI
│ ├── limit_orders.py # Limit order CLI
│ └── advanced/ # (Optional) advanced order strategies
├── bot.log # Logs: requests, responses, errors
├── README.md
├── requirements.txt
└── .env # API keys (excluded from Git)

```
---

## 📦 Setup Instructions

### 1. Prerequisites
- Python 3.9 or higher
- Binance Futures **Testnet account**
  👉 https://testnet.binancefuture.com

---

### 2. Clone the Repository
```bash
git clone https://github.com/abhi100om/binance_bot.git
cd binance_bot
```
### 3. Create & Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```
### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. API Key Configuration
```

Create a .env file in the project root:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

```
### ⚠️ Important

Use Futures Testnet keys only
Use HMAC (System Generated) keys

Never commit .env to GitHub

▶️ Usage
📌 Market Order
```
python -m src.market_orders BTCUSDT BUY 0.002
```

### Arguments

SYMBOL → BTCUSDT
SIDE → BUY / SELL
QUANTITY → Order size

📌 Limit Order
```
python -m src.limit_orders BTCUSDT SELL 0.002 70000
```
Arguments
SYMBOL
SIDE
QUANTITY
PRICE

### 🧾 Logging

All bot activity is logged in:
```
bot.log
```

Logs include:

⏱️ Timestamps

📡 API requests

📬 API responses

❌ Errors (if any)

## ⚠️ Validation & Error Handling

### The bot validates:

✅ Symbol format

✅ BUY / SELL side

✅ Quantity > 0

✅ Price > 0 (limit orders)

🚫 Invalid input = No API call

### 📝 Notes & Assumptions

Operates only on Binance Futures Testnet

Minimum order notional: ≥ 100 USDT

Market orders may temporarily show NEW status (Testnet behavior)

## 💡 Future Enhancements

Stop-Loss & Take-Profit orders

OCO / TWAP strategies

Unified CLI using Typer or argparse

Strategy backtesting engine

Docker support 🐳

Web dashboard (FastAPI + React)


## 📝 License

This project is licensed under the [MIT License](LICENSE).
