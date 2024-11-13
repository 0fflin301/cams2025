from screeninfo import get_monitors


class Window:
    def __init__(self, mode=None, screen=None, windows=1, volume=100):
        self.mode = mode
        self.screen = screen
        self.options = [
            1,
            4,
            9,
            16,
            25,
            36,
            49,
            64,
            81,
            100,
            121,
            144,
            169,
            196,
            225,
            256,
            289,
            324,
            361,
            400,
            441,
            484,
            529,
            576,
            625,
            676,
            729,
            784,
            841,
            900,
            961,
            1024,
        ]
        if windows not in self.options:
            self.windows = 1
        else:
            self.windows = windows
        self.volume = volume
        self.screens = {
            "monitor": self.geometry(),
            "1080p": {
                # window: [volume, "widthxheight+x+y"]
                1: [80, "960x540+480+270"],
                2: [0, "480x270+0+0"],
                3: [0, "480x270+480+0"],
                4: [0, "480x270+960+0"],
                5: [0, "480x270+1440+0"],
                6: [0, "480x270+0+270"],
                7: [0, "480x270+1440+270"],
                8: [0, "480x270+0+540"],
                9: [0, "480x270+1440+540"],
                10: [0, "480x270+0+810"],
                11: [0, "480x270+480+810"],
                12: [0, "480x270+960+810"],
                13: [0, "480x270+1440+810"],
            },
            "1440p": {
                # window: [volume, "widthxheight+x+y"]
                1: [80, "1280x720+640+360"],
                2: [0, "640x360+0+0"],
                3: [0, "640x360+640+0"],
                4: [0, "640x360+1280+0"],
                5: [0, "640x360+1920+0"],
                6: [0, "640x360+0+360"],
                7: [0, "640x360+1920+360"],
                8: [0, "640x360+0+720"],
                9: [0, "640x360+1920+720"],
                10: [0, "640x360+0+1080"],
                11: [0, "640x360+640+1080"],
                12: [0, "640x360+1280+1080"],
                13: [0, "640x360+1920+1080"],
            },
        }

    def monitors(self):
        result = {}
        monitors = get_monitors()
        for n, m in enumerate(monitors):
            result[n] = [m.width, m.height]
        return result

    def setMonitor(self):
        monitors = self.monitors()
        if self.screen == "all":
            return [value for value in monitors.values()]
        else:
            return [monitors[int(self.screen)]]

    def geometry(self):
        result = {}
        resolutions = self.setMonitor()
        e = None
        for turn, resolution in enumerate(resolutions):
            X, Y = resolution
            for I in range(1, 49):
                key = I * I
                result.setdefault(key, {})
                x = 0
                y = 0
                if turn == 0:
                    e = 1
                if turn >= 1:
                    e = self.windows * turn + 1
                width = round(X / I)
                height = round(Y / I)
                # This "I" define columns
                for _ in range(I):
                    # And this "I" defines rows
                    for _ in range(I):
                        if e == 1:
                            v = self.volume
                        else:
                            v = self.volume
                        result[key].setdefault(e, [v, f"{width}x{height}+{x}+{y}"])
                        x += width
                        e += 1
                    x = 0
                    y += height
        return result[self.windows]

    def getValues(self):
        if self.mode == None:
            return self.screens["monitor"]
        else:
            return self.screens[self.mode]
