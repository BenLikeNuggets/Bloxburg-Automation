import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_controller = Controller()

# Burger costumer
Vegan_beef_1 = "Vegan_beef_1"
Vegan_beef_2 = "Vegan_beef_2"
Cheese_1 = "Cheese_1"
Cheese_2 = "Cheese_2"
Lettuce_1 = "Lettuce_1"
Lettuce_2 = "Lettuce_2"
Normal_beef_1 = "Normal_beef_1"
Normal_beef_2 = "Normal_beef_2"
Onion_1 = "Onion_1"
Onion_2 = "Onion_2"
Tomato_1 = "Tomato_1"
Tomato_2 = "Tomato_2"

# Burger menu
Last_bun = "Last_bun"
Onion = "Onion"
Cheese = "Cheese" 
Vegan_beef = "Vegan_beef"
Normal_beef = "Normal_beef"
Tomato = "Tomato"
Lettuce = "Lettuce"
First_bun = "First_bun"

def click_image(image):
    try:
        image = f"{image}.png"
        image_location = pyautogui.locateOnScreen(image, confidence=0.8)
        if image_location:
            x, y = pyautogui.center(image_location)
            pyautogui.moveTo(x, y)
            time.sleep(0.1)
            pyautogui.leftClick(x, y)
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")

def costumer_click_image_1(costumer, image):
    try:
        costumer = f"{costumer}.png"
        costumer_location = pyautogui.locateOnScreen(costumer, confidence=0.95)
        if costumer_location:
            image = f"{image}.png"
            image_location = pyautogui.locateOnScreen(image, confidence=0.8)
            if image_location:
                x, y = pyautogui.center(image_location)
                pyautogui.moveTo(x, y)
                # time.sleep(0.1)
                pyautogui.leftClick(x, y)
                time.sleep(0.1)
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")

def costumer_click_image_2(costumer, image):
    try:
        costumer = f"{costumer}.png"
        costumer_location = pyautogui.locateOnScreen(costumer, confidence=0.95)
        if costumer_location:
            image = f"{image}.png"
            image_location = pyautogui.locateOnScreen(image, confidence=0.8)
            if image_location:
                x, y = pyautogui.center(image_location)
                pyautogui.moveTo(x, y)
                # time.sleep(0.1)
                pyautogui.leftClick(x, y)
                time.sleep(0.05)
                pyautogui.leftClick(x, y)
                time.sleep(0.1)
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")

def main():
    click_image(First_bun)

    click_image(Last_bun)

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
