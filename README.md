## About ##

This is a Chaturbate and Stripchat bot. It reproduces multiple streams in different windows on one or all your monitors. This bot does not record; it only plays. Have fun!

## Requeriments ##

- [Python](https://www.python.org/)
- [streamlink](https://github.com/streamlink/streamlink)
- [screeninfo](https://github.com/rr-wfm/screeninfo)
- [colorama](https://github.com/tartley/colorama)
- [cloudscraper](https://github.com/codelucas/cloudscraper)
- [mpv](https://github.com/mpv-player/mpv)

## Starting ##

Important: You need to have Python 3.8+ installed, all dependencies, MPV, and the corresponding plugins for streamlink.

There is a file called "install.bat"  with all the requirements. For Windows, you can install all the dependencies with the following command:

```bash
install.bat
```
Check the config.json file to see the default values.

Copy and paste the nicknames of the models to watch in the models.txt file, one per line. Some Chaturbate models have and Stripchat account; if you follow the next syntax: ChaturbateNickname/StripchatNickname, the bot will try to connect to Stripchat after the Chaturbate connection fails.

The numeric value of "Top" in config.json indicates the order to connect. The first "Top:value" models in the list models.txt, search in reading order, after that makes a random selection of numeric "random:value" models that are not in the Top. This is useful if you have a list with a lot of lines.
Configuration File

### Configuration File

Use config.json to establish your default configurations:
```json
{
	"config": {
		"top": 10,
		"random": 20
	},
	"video":{
		"mode": "monitor",
		"screen": 0,
		"windows": 16,
		"volume": 50,
		"audio": "default",
		"options": "--vo=gpu --gpu-api=d3d11 --gpu-context=d3d11 --hwdec=d3d11va"
	},
	"stream":{
		"streamlinkLog": 0,
		"quality": "1080p,720p,540p,480p,360p,worst",
		"timeOut": 10
	},
	"headers": {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",	
		"Accept-Language": "en-US;q=0.5,en;q=0.3",
		"Accept": "*/*",
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Connection": "keep-alive",
		"Upgrade-Insecure-Requests": "1"
		},
	"paths": {
		"mpv": "C:/mpv/mpv.exe",
		"models": "~/Cams2025/models.txt",
		"backup": "~/Cams2025/backup/models.txt"
	}
}
```
* top: First models in list, search in order
* random: After search the top, makes a random selection of the value
* mode: Mode of the grid in screen, monitor is the default value, check 1080p and 1440p example modes. If you want to do your personalized grid, check fun/windows.py.
* screen: Number of monitor, if you have 3 monitors, the values are 0, 1, 2
* windows: Number of windows to connect for a screen
* volume: Volume level for all the windows
* audio: If you have more than one audio output, you can configure the output; use this command: mpv --audio-device=help
* options: Extra options for mpv reproduction; check the mpv.io documentation
* streamLinkLog: 0 creates a Streamlink log; any other value is False
* quality: Order of the preference quality on streams
* timeOut: Time to wait for a stream to reconnect, in case of an offline stream
* headers: Web browser headers for HTTP
* mpv: MPV default path
* models: Models list default path
* backup: Automatically, the program makes a backup if models in the list (~/ = your default user directory)

For Windows, there is a batch file called cams.bat that you can run to start the bot. Then, you can run the bot with the following command on the terminal:

1. cams
2. Name of the windows grid, default value is "monitor"; you can specify a personal grid in fun/windows.py, probe "1080p"  and "1440p" modes.
3. Number of the monitor (0, 1, 2), or "all" for all monitors
4. Number of windows per monitor, default value is 16. This is the list of available values for the number of windows per monitor, but all depend on your hardware, internet connection, and monitors' resolution.
* Values for windows: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 
	324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024]
5 Volume level, if you want to use a different volume level than the default value in config.json

### Examples:

```bash\
cams # Just reproduce the default values.

cams monitor all 100 # Reproduce 100 windows in all monitors.

cams 1080p 0 # This reproduces the 1080p example grid in the `fun/windows.py` file on monitor 0.

cams monitor 25 0 0 # Reproduce 25 windows in the default grid on monitor 0 with volume level at 0
```
## Linux

For Linux, I assume you know what to do!
