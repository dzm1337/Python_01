class Plant:
    type_name = "regular"

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount=1) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def display_info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class Flowering_Plant(Plant):
    type_name = "flowering"

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return "blooming" if self.age >= 7 else "not blooming"

    def display_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers ({self.bloom()})"
        )


class Prize_Flower(Flowering_Plant):
    type_name = "prize_flowers"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
        prize_points: int,
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def display_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, {self.color} flowers "
            f"({self.bloom()}), Prize points: {self.prize_points}"
        )


class Garden_Manager:
    gardens = []

    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plants(self, plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def grow_plants(self) -> None:
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def show_report(self) -> None:
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display_info()

        counts = {"regular": 0, "flowering": 0, "prize_flowers": 0}
        for plant in self.plants:
            if getattr(plant, "type_name", None):
                plant_type = plant.type_name
                if plant_type in counts:
                    counts[plant_type] += 1

        total_growth = len(self.plants)
        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {total_growth}cm"
        )
        print(
            f"Plant types: {counts['regular']} regular, "
            f"{counts['flowering']} flowering, "
            f"{counts['prize_flowers']} prize flowers"
        )

        valid = all(plant.height >= 0 for plant in self.plants)
        print(f"\nHeight validation test: {valid}")

    @classmethod
    def create_garden_network(cls, names):
        network = []
        for n in names:
            garden = cls(n)
            cls.gardens.append(garden)
            network.append(garden)
        return network

    class GardenStats:
        @staticmethod
        def garden_score(garden):
            score = 0
            for p in garden.plants:
                score += getattr(p, "height", 0)
                score += getattr(p, "prize_points", 0)
            return score

        @staticmethod
        def total_gardens():
            return len(Garden_Manager.gardens)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    gardens = Garden_Manager.create_garden_network(["Alice", "Bob"])

    gardens[0].add_plants(Plant("Oak Tree", 100, 1825))
    gardens[0].add_plants(Flowering_Plant("Rose", 25, 30, "red"))
    gardens[0].add_plants(Prize_Flower("Sunflower", 83, 30, "yellow", 10))
    gardens[1].plants = [
        Plant("Pine", 40, 982),
        Flowering_Plant("Tulip", 25, 30, "pink"),
        Prize_Flower("Daisy", 20, 10, "white", 7),
    ]
    scores = {g.name: Garden_Manager.GardenStats.garden_score(g)
              for g in gardens}

    print(" ")
    gardens[0].grow_plants()
    print(" ")
    gardens[0].show_report()

    score_str = ", ".join(
        f"{name}: {score}" for name, score in scores.items()
    )
    print(f"Garden scores - {score_str}")
    gardens_managed = Garden_Manager.GardenStats.total_gardens()
    print(f"Total gardens managed: {gardens_managed}")
