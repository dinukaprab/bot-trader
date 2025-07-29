import time
import threading
from user.mt5_user_inputs import get_mt5_user_inputs
from integrations.mt5_login import connect_mt5_account
from utils.terminal import hide_cursor, show_cursor, clear_console
from ui.loader import show_loading_spinner, stop_spinner
from config.credentials import MT5_ACCOUNT
from colors.ansi import GREEN, RED, BLUE, RESET
from live.mt5_price_tracker import live_price_tracker

def main():
    clear_console()     # Clear the terminal
    hide_cursor()       # Hide the blinking cursor

    try:
        # Get timeframe, pairs, lot size, and trade limit from user
        tf, pairs, lot, limit = get_mt5_user_inputs()
        
        # Attempt to connect to MetaTrader 5 account
        if connect_mt5_account(MT5_ACCOUNT):
            show_loading_spinner("Preparing trading environment...")
            time.sleep(1)
            stop_spinner()
            
            print(f"\r{GREEN}✔ System ready for trading{RESET}")
            time.sleep(1)
            clear_console()

            # Start live price tracker
            threading.Thread(target=live_price_tracker, args=(pairs,), daemon=True).start()

            while True:
                time.sleep(1)
            
        else:
            print(f"\r{RED}❌ Failed to connect to MT5. Exiting...{RESET}")
            time.sleep(2)
            return False

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print(f"\r{BLUE}⚠ Operation cancelled by user{RESET}")
        stop_spinner() 
    except Exception as e:
        # Catch any unexpected errors
        print(f"\r{RED}❌ An error occurred: {e}{RESET}")
        stop_spinner()
    finally:
        # Always restore cursor and say goodbye
        show_cursor()
        print(f"\r{BLUE}Goodbye! 👋{RESET}")

if __name__ == "__main__":
    main()