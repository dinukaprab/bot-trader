# user/user_inputs.py

import questionary
from user.constants import MT5_TIMEFRAMES, FOREX_PAIRS, LOT_SIZES
from colors.ansi import RED, RESET

def get_mt5_user_inputs():
    print("")
    print("========== Forex Bot Config ( MetaTrader 5 )==========")

    # Timeframe
    tf_input = questionary.select(
        "Select timeframe:",
        choices=list(MT5_TIMEFRAMES.keys())
    ).ask()
    timeframe = MT5_TIMEFRAMES[tf_input]

    # Symbol
    pair = questionary.select(
        "Select a Forex Symbol:",
        choices=FOREX_PAIRS
    ).ask()
    pairs = [pair]

    # Lot Size
    lot_size = questionary.select(
        "Select lot size:",
        choices=LOT_SIZES
    ).ask()

    # Trade Limit
    while True:
        trade_limit = input("Set max open trades (0–100): ")
        if trade_limit.isdigit():
            trade_limit = int(trade_limit)
            if 0 <= trade_limit <= 100:
                break
        print(f"{RED}❌ Invalid input. Enter a number between 0 and 100.{RESET}")

    return timeframe, pairs, float(lot_size), trade_limit
