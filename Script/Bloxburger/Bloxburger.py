# Imported libraries
import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_controller = Controller()

# _______Storing the variables by image names_______
# Menu region:
Menu_region = "Menu_region.png"

# Menu images:
Last_bun = "Last_bun.png"
Onion = "Onion.png"
Cheese = "Cheese.png"
Vegan_beef = "Vegan_beef.png"
Normal_beef = "Normal_beef.png"
Tomato = "Tomato.png"
Lettuce = "Lettuce.png"
First_bun = "First_bun.png"

# Function for locating the center of the images
def locate_image(image, region=None):
    try:
        image_location = pyautogui.locateOnScreen(image, confidence=0.8, region=region)
        if image_location:
            image_center = pyautogui.center(image_location)
            return image_center
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")





# Define which keys the program is listening to
def on_press(key):
    try:
        if key.char == 'f': 
            # ______Setup for location of the burger menu______
            global Menu_region

            # Setting up the Menu_region
            Menu_region = pyautogui.locateOnScreen(Menu_region, confidence=0.8)
            if Menu_region:
                left, top, width, height = Menu_region
                Menu_region = (left, top, width, height)

            # Storing the center of the images
            global Last_bun, Onion, Cheese, Vegan_beef, Normal_beef, Tomato, Lettuce, First_bun

            Last_bun = locate_image(Last_bun, region=Menu_region)
            Onion = locate_image(Onion, region=Menu_region)
            Cheese = locate_image(Cheese, region=Menu_region)
            Vegan_beef = locate_image(Vegan_beef, region=Menu_region)
            Normal_beef = locate_image(Normal_beef, region=Menu_region)
            Tomato = locate_image(Tomato, region=Menu_region)
            Lettuce = locate_image(Lettuce, region=Menu_region)
            First_bun = locate_image(First_bun, region=Menu_region)

            # This setup is for the burger, and it works. Now make it automatically go to drinks and fries, and storing their locations
            # !!!First make the clicks work. Either with macro or find another solution. I'm out.



    except AttributeError:
        pass

# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("The script is ready to go.")

# Keep the script running
listener.join()

