# module_a.py
from config import Singleton


def run_a():
    config = Singleton.get_config()
    print("Module A running with:", config["mode"])
    print(id(config))