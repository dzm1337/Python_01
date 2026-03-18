class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        pass


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def display_extra_info(self) -> None:
        if self.age >= 7:
            print(f"{self.name} is blooming beautifully!\n")
        if self.age < 7:
            print(f"The {self.name} is not ready to bloom yet!\n")

    def display_info(self) -> None:
        height = self.height
        age = self.age
        name = self.name
        print(
            f"{name} (Flower): {height}cm, {age} day(s), "
            f"{self.color} color"
        )


class Tree(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int,
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def display_extra_info(self) -> None:
        size_shade = self.height / self.trunk_diameter
        name = self.name
        print(f"{name} provides {size_shade:.0f} square meters of shade\n")

    def display_info(self) -> None:
        h = self.height
        a = self.age
        n = self.name
        trunk_diameter = self.trunk_diameter
        print(
            f"{n} (Tree): {h}cm, {a} day(s), "
            f"{trunk_diameter}cm diameter"
        )


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_extra_info(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")

    def display_info(self) -> None:
        height = self.height
        age = self.age
        print(
            f"{self.name} (Vegetable): {height}cm, {age} days, "
            f"{self.harvest_season} harvest"
        )


if __name__ == "__main__":

    print("=== Garden Plant Types ===\n")

    plants: list[Plant] = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "Vitamin C"),
    ]

    for plant in plants:
        plant.display_info()
        plant.display_extra_info()
