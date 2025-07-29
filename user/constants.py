# user/constants.py
import MetaTrader5 as mt5

# ----- TIMEFRAME MAP -----
MT5_TIMEFRAMES = {
    "1m": mt5.TIMEFRAME_M1,
    "5m": mt5.TIMEFRAME_M5,
    "15m": mt5.TIMEFRAME_M15,
    "30m": mt5.TIMEFRAME_M30,
    "1h": mt5.TIMEFRAME_H1,
}

# ----- FOREX PAIRS -----
FOREX_PAIRS = [
    "XAUUSD", "EURUSD", "GBPUSD", "USDJPY", "USDCHF", "AUDUSD",
]

# ----- LOT SIZES -----
LOT_SIZES = ["0.01", "0.05", "0.1", "0.2", "0.5", "1"]
