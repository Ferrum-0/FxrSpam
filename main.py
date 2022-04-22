from ipaddress import ip_address
import pyautogui as pg
import time as t
import socket as s
import wmi
import ctypes
import pyfiglet
import pyfiglet.fonts
import os
import json
from json import load
import requests
import pkg_resources

ctypes.windll.kernel32.SetConsoleTitleW("FxrSys - v2.5")


def main():
    print('''
    #########################################################
    #  ______  __   __  _____     _____  __     __   _____  #
    # |  ____| \ \ / / |  __ \   / ____| \ \   / /  / ____| #
    # | |__     \ V /  | |__) | | (___    \ \_/ /  | (___   #
    # |  __|     > <   |  _  /   \___ \    \   /    \___ \  #
    # | |       / . \  | | \ \   ____) |    | |     ____) | #
    # |_|      /_/ \_\ |_|  \_\ |_____/     |_|    |_____/  #
    #########################################################
    ''')

    print('''
    1) Spam
    2) Display Computer Info
    3) Ascii Art (Text)
    4) IP Tracker
    ''')

    option = int(input("Enter the what you want to do (Type the number): "))

    def pcInfo():
        c = wmi.WMI()
        my_system = c.Win32_ComputerSystem()[0]

        try:
            host_name = s.gethostname()
            host_ip = s.gethostbyname(host_name)
            print(f"Hostname :  {host_name}")
            print(f"IP : {host_ip}")
        except:
            print("Unable to get Hostname and IP")
        print(f"Manufacturer: {my_system.Manufacturer}")
        print(f"Model: {my_system. Model}")
        print(f"Name: {my_system.Name}")
        print(f"Number Of Processors: {my_system.NumberOfProcessors}")
        print(f"System Type: {my_system.SystemType}")
        print(f"System Family: {my_system.SystemFamily}")

    def Spammer():
        pasteTime = int(input("How long do you want to spam for? (Seconds): "))
        pastePhrase = input("Enter what you want to spam: ")

        if pastePhrase:
            print("Phrase: " + pastePhrase)
            print("Time: " + str(pasteTime))
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

        def spam():
            while t.time() < t_end:
                pg.typewrite(pastePhrase)
                t.sleep(0.1)
                pg.hotkey("enter")
                spam()

        spam()

        print("Finished Spamming.")

    def asciiArt():
        # asciiArtText = input("Enter what you want to become ascii art (TEXT ONLY): ")
        result = pyfiglet.figlet_format(
            input("Enter what you want to become ascii art (TEXT ONLY): "), "Big")
        print(result)

    def ipTracker():
        YOUR_GEOLOCATION_KEY = 'ec0cb00474be4d55a6bbf6a751609b40'
        ip_address = input('Enter the IP Address you want to track: ')
        response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address)
        result = json.dumps(json.loads(response.content), indent=1)
        print(result)
        

    if option == int(1):
        Spammer()
        t.sleep(3)
        main()
    if option == int(2):
        pcInfo()
        t.sleep(5)
        main()
    if option == int(3):
        asciiArt()
        t.sleep(5)
        main()
    if option == int(4):
        ipTracker()
        t.sleep(5)
        main()
    if option == int(5):
        print('Please provide a valid number.')
        t.sleep(2)
        main()


main()