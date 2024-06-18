from pynput import keyboard, mouse
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

# Initialize controllers
mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Mouse position for chopping
MOUSE_POSITION = (770, 780)

def chopping():
    for _ in range(10):
        mouse_controller.press(Button.left)
        mouse_controller.release(Button.left)
        time.sleep(2)

def moving(a):
    keyboard_controller.press(a)
    time.sleep(1.14)
    keyboard_controller.release(a)

def initial_key_actions():
    keyboard_controller.press('w')
    time.sleep(0.5)
    keyboard_controller.release('w')

    keyboard_controller.press('d')
    time.sleep(1.3)
    keyboard_controller.release('d')
    keyboard_controller.press('w')
    time.sleep(3.25)
    keyboard_controller.release('w')
    keyboard_controller.press(Key.left)
    time.sleep(0.75)
    keyboard_controller.release(Key.left)
    time.sleep(0.1)
    keyboard_controller.press('w')
    time.sleep(3)
    keyboard_controller.release('w')
    time.sleep(0.1)
    keyboard_controller.press(Key.right)
    time.sleep(2.25)
    keyboard_controller.release(Key.right)
    time.sleep(0.1)
    keyboard_controller.press('s')
    time.sleep(0.30)
    keyboard_controller.release('s')
    time.sleep(0.1)
    keyboard_controller.press(Key.right)
    time.sleep(0.075)
    keyboard_controller.release(Key.right)
    keyboard_controller.press('s')
    time.sleep(0.245)
    keyboard_controller.release('s')

    keyboard_controller.press(Key.shift)
    keyboard_controller.release(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press(Key.left)
    time.sleep(0.75)
    keyboard_controller.release(Key.left)
    time.sleep(0.1)
    keyboard_controller.press('w')
    time.sleep(0.085)
    keyboard_controller.release('w')
    time.sleep(0.1)
    keyboard_controller.press(Key.shift)
    keyboard_controller.release(Key.shift)
    time.sleep(0.1)
    keyboard_controller.press(Key.right)
    time.sleep(0.7205)
    keyboard_controller.release(Key.right)

def on_press(key):
    try:
        if key.char == 'k':
            # Initial moves
            mouse_controller.position = MOUSE_POSITION
            initial_key_actions()
            mouse_controller.position = MOUSE_POSITION
            # Main loop for chopping and moving
        elif key.char == 'u':  # New action for 'h' key
                while True:
                    chopping()  # Call the chopping function
                    moving('d')
                    chopping()  # Call the chopping function again
                    moving('a')
        elif key.char == 'j':  # New action for 'h' key
                keyboard_controller.press(Key.right)
                time.sleep(0.03525)
                keyboard_controller.release(Key.right)
        elif key.char == 'h':  # New action for 'h' key
                keyboard_controller.press(Key.left)
                time.sleep(0.03525)
                keyboard_controller.release(Key.left)
        elif key.char == 'g':  # New action for 'h' key
                keyboard_controller.press('d')
                time.sleep(0.05)
                keyboard_controller.release('d')
        elif key.char == 'l':  # New action for 'h' key
                keyboard_controller.press(Key.right)
                time.sleep(1.5)
                keyboard_controller.release(Key.right)
    except AttributeError:
        pass

# Setup keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
