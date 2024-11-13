import os
import sys
import shutil
import urllib.request


class Setup:
    def __init__(self):
        self.here = os.path.abspath(os.path.dirname(__file__))
        self.urls = {
            "plugins": {
                "chaturbate": "https://raw.githubusercontent.com/community-plugins/streamlink-plugins/cloudscraper/plugins/chaturbate.py",
                "stripchat": "https://raw.githubusercontent.com/community-plugins/streamlink-plugins/cloudscraper/plugins/stripchat.py",
            },
            "mpv": "https://github.com/shinchiro/mpv-winbuild-cmake/releases/download/20241025/mpv-x86_64-20241025-git-5c59f8a.7z",
        }
        self.mpv = ".\\mvp.7z"
        self.requirements = "requirements.txt"
        if len(sys.argv) > 1:
            self.path = sys.argv[1]
            self.pip = sys.argv[1] + "\\python.exe -m pip"
        else:
            self.path = ".\\python3"
            self.pip = "pip"

    def installDependencies(self):
        try:
            os.system(f"{self.pip} install -r " + self.requirements)
            os.system(f"{self.pip} install --upgrade py7zr")
            print(f"{'='*35}\nDependencies successfully installed\n{'='*35}")
            return True
        except Exception as e:
            print("An error occurred:", e)
            return False

    def download(self, url, path, msg):
        try:
            response = urllib.request.urlopen(url)
            status = response.getcode()
            if status == 200:
                with open(path, "wb") as file:
                    file.write(response.read())
                print(msg)
                self.file = file
                return True
            else:
                print("Failed to download!")
                return False
        except Exception as e:
            print("An error occurred:", e)
            return False

    def uncompressMPV(self):
        try:
            import py7zr

            with py7zr.SevenZipFile(self.mpv, mode="r") as zip_ref:
                zip_ref.extractall("C:\\mpv")
            os.system('SET "PATH=C:\\mpv;%PATH%"')
            os.system('SET %PATH%')
            print(f"{'='*35}\nSuccessfully unzipped MPV\n{'='*35}")
        except py7zr.Bad7zFile:
            print("Error: The file is not a valid 7z archive.")
        except FileNotFoundError:
            print(f"Error: Not found: {zip_ref}")
        except PermissionError:
            print(f"Error: Not enough permissions: {self.mpv}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

    def deleteFiles(self):
        paths = [".\\mvp.7z"]
        for element in paths:
            if os.path.isdir(element):
                for root, dirs, files in os.walk(element):
                    for file in files:
                        os.chmod(os.path.join(root, file), 0o777)
                shutil.rmtree(element)
            else:
                os.remove(element)

    def run(self):
        self.installDependencies()
        for name, url in self.urls["plugins"].items():
            self.download(
                url,
                f"{self.path}\\Lib\\site-packages\\streamlink\\plugins\\{name}.py",
                f"{'='*35}\n{name.capitalize()} plugin downloaded successfully!\n{'='*35}",
            )
        self.download(self.urls["mpv"], self.mpv, f"{'='*35}\nMPV downloaded successfully!\n{'='*35}")
        if os.path.exists(self.mpv):
            self.uncompressMPV()
            self.deleteFiles()


def main():
    Setup().run()


if __name__ == "__main__":
    main()
