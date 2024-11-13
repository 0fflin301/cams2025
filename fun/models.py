import os
import sys
import random
from fun.tools import Tool


class Models:
    def __init__(self, path, top, models, backup):
        self.file = path
        self.top = top
        self.models = models
        self.backupFile = backup

    def readList(self, file):
        with open(self.file, "r", encoding="utf8") as file:
            result = file.read().split("\n")
        return result

    def saveList(self, file, data):
        try:
            with open(file, "w", encoding="utf-8") as file:
                file.write("\n".join(data))
        except:
            pass

    def backup(self):
        models = Models.readList(self, self.file)
        newList = []
        for model in models:
            if model != "" and model not in newList:
                newList.append(model)
        Models.saveList(self, self.backupFile, newList)
        Models.saveList(self, self.file, newList)
        return newList

    def getModels(self):
        print(f"{Tool.YELLOW_BRIGHT}{Tool.now()} Reading models list.")
        result = Models.readList(self, self.file)
        if result != [""]:
            result[self.top :] = random.sample(
                result[self.top :], len(result) - self.top
            )
            result = [linea for linea in result if linea and result.count(linea) == 1]
            new_result = result[: self.top] + result[self.top :]
            return new_result[: self.models + self.top]
        else:
            return result