class   Plant():

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        pass

class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def display_extra_info(self) -> None:
        if self.age >= 7:
            print(f"{self.name} is blooming beautifully!")
        if self.age < 7:
            print(f"The {self.name} is not ready to bloom yet!")
    def display_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} day(s), {self.color} color")

class Tree(Plant):

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display_extra_info(self) -> None:
       print(f"{self.name} provides {self.height / self.trunk_diameter:.0f} square meters of shade")

    def display_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} day(s), {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    
    def display_extra_info(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")
    
    def display_info(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} day(s), {self.harvest_season} harvest")
    
if __name__ == "__main__":
    plants = [
    Flower("Rose", 25, 30, "red"),
    Flower("Tulip", 15, 4, "blue"),
    Tree("Oak", 500, 1825, 50),
    Tree("Pine", 120, 982, 42),
    Vegetable("Tomato", 5, 2, "summer", "Vitamin C"),
    Vegetable("Carrot", 8, 1, "winter", "Vitamin E")
    ]
    for plant in plants:
        plant.display_info()
        plant.display_extra_info()
        print(" ")
