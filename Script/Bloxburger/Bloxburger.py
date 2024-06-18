# Imported libraries
import pyautogui
import time
from pynput import keyboard
from pynput.mouse import Button, Controller

mouse_controller = Controller()

# ___________________Storing the variables by image names___________________
# ______Declaring the variables of the menu______
# Menu region:
Menu_region = "Menu_region.png"

# Menu images - Burger menu:
Last_bun = "Last_bun.png"
Onion = "Onion.png"
Cheese = "Cheese.png"
Vegan_beef = "Vegan_beef.png"
Normal_beef = "Normal_beef.png"
Tomato = "Tomato.png"
Lettuce = "Lettuce.png"
First_bun = "First_bun.png"

# Menu images - Fry menu:
Fry_menu = "Fry_menu.png"
Normal_fry = "Normal_fry.png"
Round_fry = "Round_fry.png"
Ring_fry = "Ring_fry.png"

# Menu images - Drink menu:
Drink_menu = "Drink_menu.png"
Cola = "Cola.png"
Juice = "Juice.png"
Milkshake = "Milkshake.png"

# Menu images - Size & confirmation:
Small = "Small.png"
Medium = "Medium.png"
Large = "Large.png"
Confirm_button = "Confirm.png"

# ______Declaring the variables of the customers' orders______
# Customers' orders region:
Customer_region = "Customer_region.png"

# Orders - Burger
Cheese_1 = "Cheese_1.png"
Cheese_2 = "Cheese_2.png"
Lettuce_1 = "Lettuce_1.png"
Lettuce_2 = "Lettuce_2.png"
Normal_beef_1 = "Normal_beef_1.png"
Normal_beef_2 = "Normal_beef_2.png"
Onion_1 = "Onion_1.png"
Onion_2 = "Onion_2.png"
Tomato_1 = "Tomato_1.png"
Tomato_2 = "Tomato_2.png"
Vegan_beef_1 = "Vegan_beef_1.png"
Vegan_beef_2 = "Vegan_beef_2.png"

# Orders - Fries


# Orders - Drinks



# ___________________Functions used in the following program___________________
# Function for locating the center of the images. Searches in a given region.
def locate_image(image, region=None):
    try:
        image_location = pyautogui.locateOnScreen(image, confidence=0.8, region=region)
        if image_location:
            image_center = pyautogui.center(image_location)
            print(f"{image} is located at: {image_location}")
            return image_center
        else:
            None# print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        None# print(f"Image {image} not found (exception caught).")

# Function for locating and clicking the center of a given image. Searches in a given region.
def locate_and_click(image, region=None):
    try:
        image_location = pyautogui.locateOnScreen(image, confidence=0.8, region=region)
        if image_location:
            x, y = pyautogui.center(image_location)
            pyautogui.moveTo(x, y)
            pyautogui.press('8')
            time.sleep(0.2)
            print(f"{image} is located at: {image_location}")
            return image_location
        else:
            print(f"Image {image} not found on screen.")
    except pyautogui.ImageNotFoundException:
        print(f"Image {image} not found (exception caught).")

def order_click_1(order, menu):
    try:
        order_location = pyautogui.locateOnScreen(order, confidence=0.95, region=Customer_region)
        if order_location:
            pyautogui.moveTo(menu)
            pyautogui.press('8')
            time.sleep(0.2)
        else:
            None
    except pyautogui.ImageNotFoundException:
        print(f"Image {menu} not found (exception caught).")

def order_click_2(order, menu):
    try:
        order_location = pyautogui.locateOnScreen(order, confidence=0.95, region=Customer_region)
        if order_location:
            pyautogui.moveTo(menu)
            pyautogui.press('8')
            time.sleep(0.2)
            pyautogui.leftClick()
            time.sleep(1.0)
        else:
            print(f"Image {menu} not found on screen.")
    except pyautogui.ImageNotFoundException:
        print(f"Image {menu} not found (exception caught).")


# The script will act differently depending on which key you press.
def on_press(key):
    try:
        if key.char == 'g': 
            # ______Setup for location of the customer region______
            # Reference the global variables from the start:
            global Customer_region

            # Locating the image 'Customer_region' on screen. 
            Customer_region = pyautogui.locateOnScreen(Customer_region, confidence=0.8)
            if Customer_region:
                left, top, width, height = Customer_region
                # Assigning the location to the variable: 'Customer_region'
                Customer_region = (left, top, width, height)
                print(f"Copy & paste this to the next section:\n{Customer_region}")
            else:
                print(f"The region wasn't found")

        if key.char == 'f': 
            # ______Setup for location of the menu region______
            # Reference the global variables from the start:
            global Menu_region

            # Locating the image 'Menu_region' on screen. 
            Menu_region = pyautogui.locateOnScreen(Menu_region, confidence=0.8)
            if Menu_region:
                left, top, width, height = Menu_region
                # Assigning the location to the variable: 'Menu_region'
                Menu_region = (left, top, width, height)
                print(f"Location of the menu_region is: {Menu_region}")
            else:
                print(f"The region wasn't found")

            # ______Setup for location of the burger menu______
            # Reference the global variables from the start:
            global Last_bun, Onion, Cheese, Vegan_beef, Normal_beef, Tomato, Lettuce, First_bun

            Last_bun = locate_image(Last_bun, region=Menu_region)
            Onion = locate_image(Onion, region=Menu_region)
            Cheese = locate_image(Cheese, region=Menu_region)
            Vegan_beef = locate_image(Vegan_beef, region=Menu_region)
            Normal_beef = locate_image(Normal_beef, region=Menu_region)
            Tomato = locate_image(Tomato, region=Menu_region)
            Lettuce = locate_image(Lettuce, region=Menu_region)
            First_bun = locate_image(First_bun, region=Menu_region)

            time.sleep(1)

            # ______Setup for location of the fry menu______
            # Reference the global variables from the start:
            global Fry_menu, Normal_fry, Round_fry, Ring_fry

            locate_and_click(Fry_menu, region=Menu_region)

            time.sleep(2)

            Normal_fry = locate_image(Normal_fry, region=Menu_region)
            Round_fry = locate_image(Round_fry, region=Menu_region)
            Ring_fry = locate_image(Ring_fry, region=Menu_region)

            # ______Setup for location of the drink menu______
            global Drink_menu, Cola, Juice, Milkshake

            locate_and_click(Drink_menu, region=Menu_region)

            time.sleep(2)

            Cola = locate_image(Cola, region=Menu_region)
            Juice = locate_image(Juice, region=Menu_region)
            Milkshake = locate_image(Milkshake, region=Menu_region)

            # ______Setup for location of the sizes & confirmation button______
            # Reference the global variables from the start:
            global Small, Medium, Large, Confirm_button

            time.sleep(2)

            Small = locate_image(Small, region=Menu_region)
            Medium = locate_image(Medium, region=Menu_region)
            Large = locate_image(Large, region=Menu_region)

            time.sleep(2)

            locate_and_click(Confirm_button, region=Menu_region)

            time.sleep(2.75)

            # ______Assigned customer region for this section of the script______
            Customer_region = (670, 369, 603, 97)

            # ______Clicking customers burger orders______
            order_click_1(Cheese_1, Cheese)
            order_click_2(Cheese_2, Cheese)
            order_click_1(Lettuce_1, Lettuce)
            order_click_1(Lettuce_2, Lettuce)
            order_click_1(Normal_beef_1, Normal_beef)
            order_click_2(Normal_beef_2, Normal_beef)
            order_click_1(Onion_1, Onion)
            order_click_2(Onion_2, Onion)
            order_click_1(Tomato_1, Tomato)
            order_click_2(Tomato_2, Tomato)
            order_click_1(Vegan_beef_1, Vegan_beef)
            order_click_2(Vegan_beef_2, Vegan_beef)


            # ______Clicking customers fry orders______


            # ______Clicking customers drink orders______


            # ______Clicking confirmation button______

        if key.char == 'h':
            f=1



    except AttributeError:
        pass

# Start listening for the 'k' key
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("The script is ready to go.")

# Keep the script running
listener.join()

