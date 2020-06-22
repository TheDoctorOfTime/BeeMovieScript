import pynput


from pynput.keyboard import Key, Controller
import time

import os

keyboard = Controller()

current = set()
myBool = False
clear = lambda: os.system('cls') #on Windows System

f=open("script/BeeMovieScript.txt", "r")
if f.mode == 'r':
    contents = f.read()

def execute():
    for char in contents:
        if char.isspace():
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.05)
        else:
            keyboard.press(char)
            keyboard.release(char)

    print("Done")

while myBool == False:
    clear()
    print("==============================================================================================")
    print("How to use:")
    print("1 - Load Messenger on your browser")
    print("2 - Select Your Desired Victim")
    print("3 - Make sure you can send messages by pressing the 'Enter' key")
    print("4 - Start the program and quickly click the textbox in you and your victims chat")
    print("")
    print("==============================================================================================")
    print("")
    answer = input("input 'start' to begin someones torture: ")

    if (answer == 'start'):
        myBool = True

print("Punishment Starting in 10s")

for i in range(10):
    time.sleep(1)
    print(i+1, "s")

execute()