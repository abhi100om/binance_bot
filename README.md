# Binance Futures Trading Bot (USDT-M Testnet)

## Overview
This project is a **CLI-based Python trading bot** built for **Binance USDT-M Futures Testnet**.  
It supports **Market and Limit orders**, includes **input validation**, **structured logging**, and follows a **clean, modular code structure** suitable for extension to advanced order types.

The bot is designed for **testing and learning purposes** using Binance Futures **Testnet**, not real money.

---

## Features
- Place **Market Orders**
- Place **Limit Orders**
- Supports **BUY** and **SELL**
- Command-line interface (CLI)
- Input validation (symbol, side, quantity, price)
- Structured logging to `bot.log`
- Secure API authentication using environment variables
- Modular, reusable code structure

---

## Tech Stack
- Python 3.x
- Binance Futures API (Testnet)
- `python-binance`
- `python-dotenv`

---

## Project Structure
binance_bot/
│
├── src/
│ ├── init.py
│ ├── client.py # Binance Futures client wrapper
│ ├── validators.py # Input validation logic
│ ├── market_orders.py # Market order CLI
│ ├── limit_orders.py # Limit order CLI
│ └── advanced/ # (Optional) Advanced order strategies
│
├── bot.log # API request/response logs
├── README.md
├── requirements.txt
└── .env # API keys (not committed)


---

## Setup Instructions

### 1. Prerequisites
- Python 3.9+
- Binance Futures **Testnet** account  
  👉 https://testnet.binancefuture.com

---

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
4. API Key Configuration
Create a .env file in the project root:

BINANCE_API_KEY=your_futures_testnet_api_key
BINANCE_API_SECRET=your_futures_testnet_secret_key
⚠️ Notes:
API keys must be generated from Binance Futures Testnet
Use System-generated (HMAC) keys
Do NOT hardcode keys in code

Usage
All commands must be run from the project root.

Market Order
python -m src.market_orders BTCUSDT BUY 0.002
Arguments:

SYMBOL – Trading pair (e.g. BTCUSDT)

BUY / SELL

QUANTITY

Limit Order
python -m src.limit_orders BTCUSDT SELL 0.002 70000
Arguments:

SYMBOL

BUY / SELL

QUANTITY

PRICE

Logging
All API requests, responses, and errors are logged to:

bot.log
The log file includes:

Timestamps

Order parameters

Binance API responses

Error traces (if any)

Validation & Error Handling
The bot validates:

Trading symbol

Order side (BUY / SELL)

Quantity > 0

Price > 0 (for limit orders)

Invalid inputs are rejected before API calls.

Notes & Assumptions
This bot uses Binance Futures Testnet (fake money).

Minimum order notional on testnet is 100 USDT.

Market orders may show status NEW briefly due to testnet latency.

Advanced orders (Stop-Limit, OCO, TWAP, Grid) can be added easily due to modular design.

Future Improvements
Add advanced order types (Stop-Limit / OCO / TWAP)

Unified CLI using argparse or Typer

Strategy-based order execution

Backtesting support

Author
Abhishek Singh
