import pyautogui as pg
import time as t

class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED

pasteTime = int(input("How long do you want to spam for? (SECONDS): "))
if pasteTime:
    print(f"pasteTime: {pasteTime}")
else:
    print("Error. Restart Code.")

pastePhrase = input("Enter what you want to spam: ")
if pastePhrase:
    print(f"pastePhrase: {pastePhrase}")
    t.sleep(1)
    print(3)
    t.sleep(1)
    print(2)
    t.sleep(1)
    print("Spamming Now.")
    t.sleep(1)
else: 
    print("Error. Restart Code.")

t_end = t.time() + 1 * pasteTime

def func():
    while t.time() < t_end:
        pg.typewrite(pastePhrase) 
        t.sleep(0.1)
        pg.hotkey("enter")
        func()

func()

print("Finished Spamming.")