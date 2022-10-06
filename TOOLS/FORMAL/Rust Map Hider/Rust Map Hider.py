from pynput import keyboard
import pyautogui,time

print("Please open obs and set an image over where the map is. Open settings, go to keybinds and set show and hide for that image to a key.")

topress = input("Please input that key you set in obs (default: F6): ")
if topress == "": topress = "F6"
mapkeybind = input("Please input your map keybind in rust (default: g): ")
if mapkeybind == "": mapkeybind = "g"

print(f"When you hold '{mapkeybind}' the image should appear. When you release it, it should disappear.\nThe current keybind is set to: '{topress}'")


PRESSKEYS = [
    keyboard.KeyCode(char=mapkeybind.lower()),
    keyboard.KeyCode(char=mapkeybind.upper()),
    keyboard.KeyCode(char='\x07'), # CTRL + G
]

ignore = False

def on_press(key):
    global ignore
    if key in PRESSKEYS:
        if not ignore:
            ignore = True
            pyautogui.keyDown(topress)
            pyautogui.keyUp(topress)
            
def on_release(key):
    global ignore
    if key in PRESSKEYS:
        ignore = False
        time.sleep(0.2)
        pyautogui.keyDown(topress)
        pyautogui.keyUp(topress)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: listener.join()