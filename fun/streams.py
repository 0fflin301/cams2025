import os
import sys
import shlex
import subprocess
import streamlink
from fun.config import Config
from fun.tools import Tool


class Stream:
    config = Config(sys.path[0] + "/config.json")
    config.load_config()

    def __init__(
        self, model, nickname, stripchat, url, window, volume, geometry, screen
    ):
        self.model = model
        self.window = window
        self.url = url.replace("__MODEL__", nickname)
        self.values = [stripchat, window, volume, geometry, screen]
        if sys.platform.startswith("win"):
            self.streamlink = "streamlink"
            self.mpv = Tool.path(self.config.get_value("paths", "mpv"))
        elif sys.platform.startswith("darwin"):
            self.mpv = Tool.path("mpv-osx")
            self.streamlink = "python3/bin/streamlink"
        elif sys.platform.startswith("linux"):
            self.streamlink = "python3/bin/streamlink"
            self.mpv = Tool.path("mpv")
        self.audio = self.config.get_value("video", "audio")
        self.options = self.config.get_value("video", "options")
        if self.config.get_value("stream", "streamlinkLog") == 0:
            self.log = " --loglevel info" f' --logfile "{self.logFile()}"'
        else:
            self.log = "--loglevel none"
        self.quality = self.config.get_value("stream", "quality")
        self.timeOut = self.config.get_value("stream", "timeOut")
        self.userAgent = self.config.get_value("headers", "User-Agent")
        self.accept = self.config.get_value("headers", "Accept")
        self.acceptLanguage = self.config.get_value("headers", "Accept-Language")
        self.encoding = self.config.get_value("headers", "Accept-Encoding")
        self.connection = self.config.get_value("headers", "Connection")
        self.upgrade = self.config.get_value("headers", "Upgrade-Insecure-Requests")
        self.command = (
            "streamlink"
            # LOG FILE
            f" {self.log}"
            # VIDEO PLAYER PATH
            f' --player "{self.mpv}"'
            # VIDEO PLAYER OPTIONS
            ' --player-args "'
            f" {self.options}"
            f" --audio-device={self.audio}"
            f" --volume={volume}"
            f" --screen={screen}"
            f" --geometry={geometry}"
            " --no-terminal --snap-window --no-border"
            " --no-window-dragging --no-osc"
            f" --osd-msg1='{self.model}' --script-opts=osd-msg1-duration=0 \""
            f' --title "{model} - {self.url}"'
            # URL
            " --url __URL__"
            # STREAM
            f' --default-stream "{self.quality}"'
            f" --stream-timeout {self.timeOut}"
            # BROWSER HEADERS
            f' --http-header User-Agent="{self.userAgent}"'
            f' --http-header Accept="{self.accept}"'
            f' --http-header Accept-Language="{self.acceptLanguage}"'
            f' --http-header Accept-Encoding="{self.encoding}"'
            f' --http-header Connection="{self.connection}"'
            f' --http-header Upgrade-Insecure-Requests="{self.upgrade}"'
        )

    def logFile(self):
        if sys.platform.startswith("win"):
            path = f"{Tool.LOG}/{Tool.now('%Y/%m')}"
        else:
            path = f"logs/{Tool.now('%Y/%m')}"
        if not os.path.exists(path):
            Tool.createPath(path)
        return f"{path}/StreamlinkCli-{Tool.now('%Y-%m-%d')}.txt"

    def conect(self, url):
        try:
            print(f"{Tool.now()} Attempting to connect with {self.model} on {url}")
            Tool.log(f"Attempting to connect with {self.model} on {url}")
            args = shlex.split(self.command.replace("__URL__", url))
            Tool.log(args)
            play = subprocess.Popen(args)
            Tool.sleep(7, 9)
            status = play.poll()
            if status == None:
                print(f"{Tool.GREEN_BRIGHT}{Tool.now()} Connection with {self.model} successful.")
                Tool.log(f"Connection with {self.model} successful.")
                return play
            elif status == 1:
                print(f"{Tool.RED_NORMAL}{Tool.now()} Connection with {self.model} failed.")
                Tool.log(f"Connection with {self.model} failed.")
                play.kill()
                return None
        except streamlink.exceptions.StreamError as err:
            print(
                f"{Tool.BLACK_BRIGHT}{Tool.now()} {self.model} 404 Not found for url: {url}"
            )
            Tool.log(f"{self.model}:{url}:STREAMLINK->{err}")
            Tool.log(self.command.replace("__URL__", url))
            return None
        except subprocess.CalledProcessError as err:
            print(
                f"{Tool.RED_NORMAL}{Tool.now()} ERROR: Attempting to connect with {self.model} on {url}"
            )
            Tool.log(f"{self.model}:{url}:SUBPROCESS->{err}")
            Tool.log(self.command.replace("__URL__", url))
            return None
        except Exception as err:
            print(f"UNEXPECTED ERROR: {err}")
            Tool.log(f"{self.model}:{url}:{err}")
            Tool.log(self.command.replace("__URL__", url))
            raise err 
            return None

    def run(self):
        stream = self.conect(self.url)
        if stream != None:
            return [self.window, self.model, stream, self.values]
        else:
            return None
