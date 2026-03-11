# flyweight method 
class CharacterFlyweight:
    def __init__(self, char, font, size):
        self.char = char
        self.font = font 
        self.size = size
    def draw(self, pos):
        return "ComplexPattern[% s]" % (pos)


class FlyweightFactory:
    flyweights = {}

    @classmethod
    def get_flyweight(cls, char, font, size):
        if (char, font, size) not in cls.flyweights:
            cls.flyweights[char, font, size] = CharacterFlyweight(char, font, size)
        return cls.flyweights[char, font, size]


if __name__ == "__main__":
    flyweights = []
    for i, c in enumerate("hello world"):
        chars = FlyweightFactory.get_flyweight(c, "Arial", 12)
        flyweights.append(chars)
    
    for i, chars in enumerate(flyweights):
        print(f"char {i} id = {id(chars)}")
    
    print(flyweights[2] is flyweights[3])