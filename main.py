import os
import sys
import traceback
from threading import Thread
from colorama import init
from fun.config import Config
from fun.models import Models
from fun.windows import Window
from fun.streams import Stream
from fun.tools import Tool

init(autoreset=True)
path = os.path.dirname(os.path.realpath(__file__))
config = Config(os.path.join(path, "config.json"))
config.load_config()
if len(sys.argv) >= 2:
    mode = sys.argv[1]
    screen = sys.argv[2]
    windows = int(sys.argv[3])
else:
    mode = config.get_value("video", "mode")
    screen = config.get_value("video", "screen")
    windows = config.get_value("video", "windows")
volume = config.get_value("video", "volume")
WINDOWS = Window(mode, screen, windows, volume).getValues()
MODELS = Models(
    Tool.path(
        config.get_value(
            "paths",
            "models",
        )
    ),
    config.get_value("config", "top"),
    config.get_value("config", "random"),
    Tool.path(config.get_value("paths", "backup")),
)
ONLINE = []
URL = {
    "Chaturbate": "https://chaturbate.com/__MODEL__/",
    "Stripchat": "https://stripchat.com/__MODEL__/",
}


def killer():
    while True:
        if ONLINE != []:
            for window, model, stream, values in ONLINE:
                try:
                    status = stream.poll()
                    if status != None:
                        stream.kill()
                        ONLINE.remove([window, model, stream, values])
                        print(f"{Tool.BLACK_BRIGHT} The stream with {model} is currently offline.")
                        Tool.log(f"The stream with {model} is currently offline.")
                        if values[0] != "":
                            nickname, window, volume, geometry, screen = range(5)
                            newStream = Stream(
                                model,
                                values[nickname],
                                "",
                                URL["Stripchat"],
                                values[window],
                                values[volume],
                                values[geometry],
                                values[screen],
                            ).run()
                            evaluate(newStream)
                except Exception as err:
                    print(err)
                    Tool.log(f"{window}:{model}:{status}:{err}")
                    pass
        Tool.sleep(0, 1)


def models():
    if ONLINE != []:
        return [model for window, model, stream, values in ONLINE]
    else:
        return []


def select():
    for key, value in WINDOWS.items():
        if ONLINE == []:
            window = key
            break
        elif ONLINE != [] and key not in [
            window for window, model, stream, values in ONLINE
        ]:
            window = key
            break
    return [window, value]


def evaluate(stream):
    if stream != None:
        ONLINE.append(stream)


def main():
    MODELS.backup()
    volume, geometry = range(2)
    window, value = range(2)
    kill = Thread(target=killer)
    kill.start()
    while True:
        try:
            for model in MODELS.getModels():
                if "/" in model:
                    chaturbate = model.split("/")[0]
                    stripchat = model.split("/")[1]
                    model = chaturbate
                else:
                    chaturbate = model
                    stripchat = ""
                if len(ONLINE) < len(WINDOWS) and model not in models():
                    windows = select()
                    stream = Stream(
                        model,
                        chaturbate,
                        stripchat,
                        URL["Chaturbate"],
                        windows[window],
                        windows[value][volume],
                        windows[value][geometry],
                        screen,
                    ).run()
                    evaluate(stream)
            Tool.sleep(33, 55)
        except TypeError as err:
            print(f"{Tool.RED_NORMAL}{Tool.now()} Models list empty!")
            Tool.sleep(33, 55)
            pass
        except ValueError as err:
            print(f"{Tool.RED_NORMAL}{Tool.now()} Not enough models on list!")
            Tool.sleep(33, 55)
            pass
        except Exception as err:
            Tool.log(f"{model}:{err}")
            raise traceback.print_exc()


if __name__ == "__main__":
    main()
