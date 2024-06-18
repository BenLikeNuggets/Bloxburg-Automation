import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController


mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Images
House = "First_bun.png"

def click_image(image):
    try:
        image_location = pyautogui.locateOnScreen(image, confidence=0.8)
        if image_location:
            x, y = pyautogui.center(image_location)
            pyautogui.moveTo(x, y)
            pyautogui.press('8')
            time.sleep(0.2)
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")


def main():
    click_image(House)

def on_press(key):
    try:
        if key.char == 'k':
            main()
    except AttributeError:
        pass

# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("The script is ready to go.")

# Keep the script running
listener.join()
