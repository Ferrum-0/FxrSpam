import pyautogui as pg
import time as t

print(
f'''
###################################################################
#  ______  __   __  _____     _____   _____               __  __  #
# |  ____| \ \ / / |  __ \   / ____| |  __ \      /\     |  \/  | #
# | |__     \ V /  | |__) | | (___   | |__) |    /  \    | \  / | #
# |  __|     > <   |  _  /   \___ \  |  ___/    / /\ \   | |\/| | #
# | |       / . \  | | \ \   ____) | | |       / ____ \  | |  | | #
# |_|      /_/ \_\ |_|  \_\ |_____/  |_|      /_/    \_\ |_|  |_| #
###################################################################                                                                
                                                                
''')

pasteTime = int(input("How long do you want to spam for? (Seconds): "))
pastePhrase = input("Enter what you want to spam: ")

if pastePhrase:
    print(f"Phrase: {pastePhrase}")
    print(f"Time: {pasteTime}")
    t.sleep(1)
    print(3)
    t.sleep(1)
    print(2)
    t.sleep(1)
    print("Spamming Now.")
    t.sleep(1)
else: 
    print("Error.")

t_end = t.time() + 1 * pasteTime

def func():
    while t.time() < t_end:
        pg.typewrite(pastePhrase) 
        t.sleep(0.1)
        pg.hotkey("enter")
        func()

func()

print("Finished Spamming.")