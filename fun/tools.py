import datetime
import os
import sys
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

this = os.path.dirname(os.path.realpath(__file__))

class Tool:

    MAGENTA_BRIGHT = Fore.MAGENTA + Style.BRIGHT
    GREEN_BRIGHT = Fore.GREEN + Style.BRIGHT
    RED_NORMAL = Fore.RED + Style.NORMAL
    BLUE_NORMAL = Fore.BLUE + Style.NORMAL
    YELLOW_BRIGHT = Fore.YELLOW + Style.BRIGHT
    YELLOW_NORMAL = Fore.YELLOW + Style.NORMAL
    BLACK_BRIGHT = Fore.BLACK + Style.BRIGHT
    WHITE_BRIGHT = Fore.WHITE + Style.BRIGHT
    WHITE_NORMAL = Fore.WHITE + Style.NORMAL
    WHITE_DIM = Fore.WHITE + Style.DIM
    CYAN_NORMAL = Fore.CYAN + Style.NORMAL

    LOG = f"{this}/logs"

    def path(value):
        if "~/" == value[0:2]:
            return os.path.expanduser(value)
        else:
            return value
    
    def now(value="%Y/%m/%d %H:%M:%S"):
        return datetime.datetime.now().strftime(value)

    def sleep(a, b, mute=True):
        for i in range(random.randint(a, b), 0, -1):
            if mute is False:
                print(f"wait {i}s", end="\r")
            time.sleep(1)
        time.sleep(float(f"0.{random.randint(0,1000000)}"))

    def log(value, out=False):
        date = str(Tool.now('%Y-%m-%d'))
        year = date[0:4]
        mount = date[5:7]
        path = f"{Tool.LOG}/{year}/{mount}/"
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"{path}log_{date}.txt", "a", encoding="utf-8"
                  ) as file:
            file.write(f"{Tool.now()} {value}\n")
        if out is True:
            print(f"{Tool.now()} {value}")

    def createPath(path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path
