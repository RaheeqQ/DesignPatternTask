# global static instance 
# singlton design principle
import json


class Singleton:
    __shared_config = None

    @staticmethod
    def get_config():
        if Singleton.__shared_config is None:
            print("Loading config...")
            with open("config.json", "r") as f:
                Singleton.__shared_config = json.load(f)
        return Singleton.__shared_config