import sys
import time
import itertools
import threading
from colors.ansi import WHITE, RESET

# Event flag to control spinner state
spinner_running = threading.Event()

def show_loading_spinner(message):
    # Set flag to start spinner
    spinner_running.set()

    def spinner():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if not spinner_running.is_set():
                break
            
            # Display the spinner with the message
            sys.stdout.write(f"\r{WHITE}{message} {c}{RESET}")
            sys.stdout.flush()
            time.sleep(0.1)

        # Clear the spinner line after stopping    
        sys.stdout.write("\r\033[K")

    # Run spinner in a background thread
    threading.Thread(target=spinner, daemon=True).start()

# Clear the flag to stop spinner
def stop_spinner():
    spinner_running.clear()
    time.sleep(0.1)
