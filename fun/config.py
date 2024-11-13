import json

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_config(self):
        try:
            with open(self.file_path, 'r', encoding="utf8") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding the file '{self.file_path}'.")

    def get_value(self, name, value):
        if self.data:
            paths = self.data.get(name, {})
            result = paths.get(value, {})
            return result
        else:
            print("The JSON file could not be loaded.")
    	