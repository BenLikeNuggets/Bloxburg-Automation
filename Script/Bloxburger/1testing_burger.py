import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Controller

mouse_controller = Controller()

# Burger customer and menu items
items = {
    "Vegan_beef_1": "Vegan_beef_1.png",
    "Vegan_beef_2": "Vegan_beef_2.png",
    "Cheese_1": "Cheese_1.png",
    "Cheese_2": "Cheese_2.png",
    "Lettuce_1": "Lettuce_1.png",
    "Lettuce_2": "Lettuce_2.png",
    "Normal_beef_1": "Normal_beef_1.png",
    "Normal_beef_2": "Normal_beef_2.png",
    "Onion_1": "Onion_1.png",
    "Onion_2": "Onion_2.png",
    "Tomato_1": "Tomato_1.png",
    "Tomato_2": "Tomato_2.png",
    "Last_bun": "Last_bun.png",
    "Onion": "Onion.png",
    "Cheese": "Cheese.png",
    "Vegan_beef": "Vegan_beef.png",
    "Normal_beef": "Normal_beef.png",
    "Tomato": "Tomato.png",
    "Lettuce": "Lettuce.png",
    "First_bun": "First_bun.png"
}

def click_image(image, double_click=False):
    try:
        image_location = pyautogui.locateCenterOnScreen(image, confidence=0.85)
        if image_location:
            pyautogui.moveTo(image_location)
            pyautogui.leftClick()
            if double_click:
                time.sleep(0.05)
                pyautogui.leftClick()
            time.sleep(0.05)
    except pyautogui.ImageNotFoundException:
        pass

def costumer_click_image(costumer, image, double_click=False):
    try:
        costumer_location = pyautogui.locateCenterOnScreen(costumer, confidence=0.9)
        if costumer_location:
            click_image(image, double_click)
    except pyautogui.ImageNotFoundException:
        pass

def main():
    click_image(items["First_bun"])
    for item1, item2 in [("Lettuce_1", "Lettuce"), ("Lettuce_2", "Lettuce"),
                         ("Tomato_1", "Tomato"), ("Tomato_2", "Tomato"),
                         ("Normal_beef_1", "Normal_beef"), ("Normal_beef_2", "Normal_beef"),
                         ("Vegan_beef_1", "Vegan_beef"), ("Vegan_beef_2", "Vegan_beef"),
                         ("Cheese_1", "Cheese"), ("Cheese_2", "Cheese"),
                         ("Onion_1", "Onion"), ("Onion_2", "Onion")]:
        costumer_click_image(items[item1], items[item2], double_click=item1.endswith('2'))
    click_image(items["Last_bun"])

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
