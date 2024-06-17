import pyautogui
from pynput import keyboard
from pynput.mouse import Controller

mouse_controller = Controller()

# Menu images - .png
burger_images = [
    "First_bun",
    "Lettuce",
    "Tomato",
    "Normal_beef",
    "Vegan_beef",
    "Cheese",
    "Onion",
    "Last_bun"
]

# Menu images - Centers
burger_centers = [None] * len(burger_images)

def locate_image(image):
    image_path = f"{image}.png"
    image_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if image_location:
        return pyautogui.center(image_location)
    return None

def cache_burgers():
    global burger_centers
    burger_centers = [locate_image(image) for image in burger_images]

def on_press(key):
    if hasattr(key, 'char') and key.char == 'k':
        print(cache_burgers())

# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Press 'k' to start the script.")

# Keep the script running
listener.join()
