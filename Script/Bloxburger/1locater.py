import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_controller = Controller()

# Menu images - .png
# Burgers
Last_bun = "Last_bun.png"
Onion = "Onion.png"
Cheese = "Cheese.png"
Vegan_beef = "Vegan_beef.png"
Normal_beef = "Normal_beef.png"
Tomato = "Tomato.png"
Lettuce = "Lettuce.png"
First_bun = "First_bun.png"

# Fries
Fry_menu = "Fry_menu.png"
Normal_fry = "Normal_fry.png"
Round_fry = "Round_fry.png"
Ring_fry = "Ring_fry.png"

# Menu images - Centers
Burger_centers = [None] * 8

Fry_centers = [None] * 4

Drink_centers = [None] * 4

def locate_image(image):
    try:
        image_location = pyautogui.locateOnScreen(image, confidence=0.8)
        if image_location:
            image_center = pyautogui.center(image_location)
            return image_center
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")

def cache_burgers():
    global Burger_centers
    Burger_centers[0] = locate_image(First_bun)
    Burger_centers[1] = locate_image(Lettuce)
    Burger_centers[2] = locate_image(Tomato)
    Burger_centers[3] = locate_image(Normal_beef)
    Burger_centers[4] = locate_image(Vegan_beef)
    Burger_centers[5] = locate_image(Cheese)
    Burger_centers[6] = locate_image(Onion)
    Burger_centers[7] = locate_image(Last_bun)

def cache_fries():
    global Fry_centers
    Fry_centers[0] = locate_image(Fry_menu)
    Fry_centers[1] = locate_image(Normal_fry)
    Fry_centers[3] = locate_image(Round_fry)
    Fry_centers[2] = locate_image(Ring_fry)

def cache_drinks():
    global Drink_centers

def on_press(key):
    try:
        if key.char == 'k':
            cache_burgers()
        elif key.char == 'j':
            cache_fries()
        elif key.char == 'h':
            cache_drinks()
    except AttributeError:
        pass

# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Press 'k' to start the script.")

# Keep the script running
listener.join()
