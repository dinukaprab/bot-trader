import sys
import time
import MetaTrader5 as mt5
from datetime import datetime
from colors.ansi import CYAN, RED, YELLOW, RESET
from utils.terminal import clear_console

def check_current_price(symbol):
    tick = mt5.symbol_info_tick(symbol)

    if tick:
        return {
            'bid': tick.bid,
            'ask': tick.ask,
            'last': tick.last
        }
    else:
        clear_console()
        print(f"\r{RED}❌ Failed to get data for {symbol}{RESET}")
        return None
    
def live_price_tracker(pairs):
    while True:
        sys.stdout.write(f"\033[{len(pairs)}F")

        for symbol in pairs:
            price = check_current_price(symbol)  # Fetch current bid/ask price
            sys.stdout.write("\033[K")

            if price:
                # Print timestamp and price data
                time_str = f"{CYAN}[{datetime.now().strftime('%H:%M:%S')}]"
                price_str = f"{YELLOW}{symbol:<10}{RESET} Bid: {price['bid']:<10} | Ask: {price['ask']:<10}"
                print(f"\r{time_str} {price_str}")
            else:
                print(f"\r{CYAN}[{datetime.now().strftime('%H:%M:%S')}] {YELLOW}{symbol:<10}{RESET} price unavailable")
                return
            
        sys.stdout.flush()
        time.sleep(1)