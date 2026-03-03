#prototype method 
from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class NPCPrototype(Prototype):
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
    def clone(self):
        return copy.deepcopy(self)
    def __str__(self):
        return f"NPC(name= {self.name}, weapon= {self.weapon})"
 

if __name__ == "__main__":
    basic_NPC_prototype = NPCPrototype("Goblin", {"type": "club", "damage": 10})
    print("Original enemy:", basic_NPC_prototype)

    prototype_clone = basic_NPC_prototype.clone()
    print("Cloned NPC:", prototype_clone)
    # Customizing the cloned NPC
    prototype_clone.name = "Goblin Clone"
    print("Customized cloned NPC:", prototype_clone)

