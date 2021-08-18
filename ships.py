class Ships:
    def __init__(self, name, space_size):
        self.name = name
        self.space_size = space_size


class Destroyer(Ships):
    def __init__(self):
        super().__init__("Destroyer", 2)

class Submarine(Ships):
    def __init__(self):
        super().__init__("Submarine", 3)

class Battleship(Ships):
    def __init__(self):
        super().__init__("Battleship", 4)

class Aircraft_Carrier(Ships):
    def __init__(self):
        super().__init__("AirCraft Carrier", 5)