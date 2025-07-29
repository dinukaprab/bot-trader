import os
import sys

# Hide cursor
def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

# Show cursor
def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

# Clear console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
