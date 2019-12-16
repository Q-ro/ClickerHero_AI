'''
Author: Andres Mrad (Q-ro)
Date: Monday 16/December/2019 @ 00:03:05
Description: First attempt at having a game play itself using scripting and A.I.
'''
import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
speedUp_key = KeyCode(char='+')
speedDown_key = KeyCode(char='-')
exit_key = Key.esc
#  ==========================

pause = True
running = True


def on_press(key):
    global running, pause, delay

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == speedUp_key:
        delay = delay/2
        print("[Speed Up] :",delay)
    elif key == speedDown_key:
        delay = delay*2
        print("[Speed Down] :",delay)
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t + = Increase Speed")
    print("\t - = Decrease Speed")
    print("\t ESC = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()

    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay

    lis.stop()


if __name__ == "__main__":
    main()
