from pynput.mouse import Button, Controller
from time import sleep
from threading import Thread
import random


def move_click_left(mouse, x, y):
    mouse.position = (x, y)
    mouse.click(Button.left)


def prevent_lock(mouse, will_wait, move_delay=60.0):
    """Moves the mouse cursor randomly so the screen doesn't lock"""
    while will_wait():
        random_position = (random.randint(0, 800), random.randint(0, 800))
        print("Moving to:", random_position)

        mouse.position = random_position
        sleep(move_delay)


def main():
    mouse = Controller()
    delay_secs = 3 * 60 * 60  # Wait 3 hours
    sleeper = Thread(target=sleep, args=(delay_secs,), daemon=True)
    sleeper.start()

    prevent_lock(mouse, sleeper.is_alive)

    # Open the menu
    move_click_left(mouse, 76, 71)
    sleep(1)
    # Click resume download
    move_click_left(mouse, 81, 167)


if __name__ == "__main__":
    main()
