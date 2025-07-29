import time
import MetaTrader5 as mt5
from colors.ansi import RED, RESET, GREEN
from ui.loader import show_loading_spinner, stop_spinner
from utils.terminal import clear_console

def connect_mt5_account(account_info):
    # Extract login credentials from the passed dictionary
    login = account_info["login"]
    password = account_info["password"]
    server = account_info["server"]

    # Show spinner while initializing MT5
    clear_console()
    show_loading_spinner("Connecting to MetaTrader 5...")
    time.sleep(1)

    # Initialize MT5 terminal connection
    if not mt5.initialize():
        stop_spinner()
        print(f"{RED}❌ Initialization failed: {mt5.last_error()}{RESET}")
        print(f"{RED}Restart your MT5 Terminal and try again.{RESET}")
        return False

    # Initialization successful
    stop_spinner()
    print(f"{GREEN}✔ Successfully connected to MetaTrader 5{RESET}")
    show_loading_spinner("Logging into your account...")
    time.sleep(1)

    # Attempt to log in to the trading account
    if not mt5.login(login, password=password, server=server):
        stop_spinner()
        print(f"{RED}❌ Login failed: {mt5.last_error()}{RESET}")
        print(f"{RED}Restart your MT5 Terminal and try again.{RESET}")
        return False   

    # Login successful
    stop_spinner()
    print(f"{GREEN}✔ Successfully logged into your Account{RESET}")
    return True