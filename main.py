from ipaddress import ip_address
from itertools import count
import pyautogui as GUI
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

ctypes.windll.kernel32.SetConsoleTitleW("FxrSys - v2.6")


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
    5) Webhook Tool
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
                GUI.typewrite(pastePhrase)
                t.sleep(0.1)
                GUI.hotkey("enter")
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
        response = requests.get('https://iGUIeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address)
        result = json.dumps(json.loads(response.content), indent=1)
        print(result)

    # def counting():
    #     printWrite = input("Print or Write numbers? (P/W): ")
            
    #     def printNum():
    #         endNumber = int(input("Enter the number you want to count upto: "))
    #         for i in range(endNumber):
    #             print(i)


    #     def writeNum():
    #             endNumber = int(input("Enter the number you want to count upto: "))

    #             print(3)
    #             t.sleep(1)
    #             print(2)
    #             t.sleep(1)
    #             print(1)
    #             t.sleep(1)
    #             print("Counting Starting...")

    #             for num in range(1, endNumber + 1):
    #                 GUI.typewrite(num)

    #     if printWrite == 'p' or 'P':
    #         printNum()
    #     if printWrite == 'w' or 'W':
    #         writeNum()

    def webhookTool():
        print("Made by Pancakes#4891 and laika#9603")
        print("\nStay mad if you think stealing this code is wrong.")

        t.sleep(1)

        print('''
        ╦ ╦┌─┐┌┐ ┬ ┬┌─┐┌─┐┬┌─  ┌┬┐┌─┐┌─┐┬  ┌─┐
        ║║║├┤ ├┴┐├─┤│ ││ │├┴┐   │ │ ││ ││  └─┐
        ╚╩╝└─┘└─┘┴ ┴└─┘└─┘┴ ┴   ┴ └─┘└─┘┴─┘└─┘
        ''')

        def webhook():
            while True:
                option = input('''
                [1] webhook spammer
                [2] webhook deleter
                [3] dump webhook info
                [4] edit webhook
                [5] exit webhook tools
                ==> ''')
                hook = input("webhook: ")
                
                if option == "1":
                    message = input("message to spam: ")
                    amount = int(input("amount to spam: "))
                    wait = float(input("delay: "))

                    headers = {"content-type": "application/json"}
                    data = {"content": message}
                    t.sleep(wait)

                    for _ in range(amount):
                        r = requests.post(hook, json=data,headers=headers)
                        print(f"done sending {amount} messages")
                        
                        if r.status_code == 200:
                            print("sent message successfully")

                if option == "2":
                    requests.delete(hook)
                    print("webhook has been deleted!\n") 

                if option == "3":
                    r = requests.get(hook)
                    print(r.content)
                        
                if option == "4":
                    wbname = input("name: ")
                    requests.patch(hook, json={"name": wbname})
                    print("succsesfully changed webhook name to: ",wbname)

                if option == "5":
                    if "__main__" == __name__:
                        main()
        webhook()


    if option is None:
        print('Please provide a valid number.')
        t.sleep(2)
        if "__main__" == __name__:
            main()
    else: 
        if option == int(1):
            Spammer()
            t.sleep(3)
            if "__main__" == __name__:
                main()
        if option == int(2):
            pcInfo()
            t.sleep(5)
            if "__main__" == __name__:
                main()
        if option == int(3):
            asciiArt()
            t.sleep(5)
            if "__main__" == __name__:
                main()
        if option == int(4):
            ipTracker()
            t.sleep(5)
            if "__main__" == __name__:
                main()
        if option == int(5):
            webhookTool()
            t.sleep(2)
            if "__main__" == __name__:
                main()
        if option >= int(6):
            print('Please provide a valid number.')
            t.sleep(2)
            if "__main__" == __name__:
                main()


if "__main__" == __name__:
    main()