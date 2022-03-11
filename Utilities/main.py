from colorama import Fore
import requests, sys, time, os

class Colours:
    Green = Fore.GREEN
    Red = Fore.RED
    Reset = Fore.RESET

class Utilities:

    def __init__(self):
        self.ASCII_URL = "https://artii.herokuapp.com"

    def type(self, text):
        for char in text + "\n\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(1. / 7)

    def Logo(self):
        ascii = requests.get(self.ASCII_URL+"/make?text=Discord Editor")
        print(f"{Colours.Green}{ascii.text}{Colours.Reset}")

    def Clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')



