# module_b.py
from config import Singleton


def run_b():
    config = Singleton.get_config()
    print("Module B running with:", config["mode"])
    print(id(config))