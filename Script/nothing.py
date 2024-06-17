import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_controller = Controller()

# Define images here
e = "e"
house = "house"

def click_image(image):
    try:
        image = f"{image}.png"
        image_location = pyautogui.locateOnScreen(image, confidence=0.9)
        if image_location:
            x, y = pyautogui.center(image_location)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick(x, y)
            time.sleep(0.2)
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")


def main():
    click_image(house)

def on_press(key):
    try:
        if key.char == 'k':
            main()
    except AttributeError:
        pass


# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Press 'k' to start the script.")

# Keep the script running
listener.join()
