class Plant():
    type_name = "regular"

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
    def grow(self, amount=1):
        self.height = self.height + amount
        print(f"{self.name} grew {amount}cm")
    def display_info(self):
        print(f"- {self.name}: {self.height}")

class   Flowering_Plant(Plant):
    type_name = "flowering"

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
    def bloom(self) -> str:
        if self.age >= 7:
            return "blooming"
        return "not blooming"
    def display_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom()})")

class   Prize_Flower(Flowering_Plant):
    type_name = "prize_flowers"

    def __init__(self, name: str, height: int, age: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    def display_info(self) -> None:
        print(f"- {self.name}: {self.height}cm, {self.color} flowers ({self.bloom()}), Prize points: {self.prize_points}")

class   Garden_Manager():
    
    gardens = []

    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plants(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")
    def grow_plants(self):
        print(" ")
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
    def show_report(self):
        print(" ")
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.display_info()
        counts = {"regular": 0, "flowering": 0, "prize_flowers": 0}
        for plant in self.plants:
            if getattr(plant, "type_name", None):
                type = plant.type_name
            if type in counts:
                counts[type] += 1
        total_growth = len(self.plants)
        print(" ")
        print(f"Plants added: {len(self.plants)}, Total_growth = {total_growth}cm")
        print(f"Plant types: {counts['regular']} regular, {counts['flowering']} flowering, {counts['prize_flowers']} prize flowers")
        valid = True
        for plant in self.plants:
            if (plant.height < 0):
                valid = False
        print(" ")
        print(f"Height validation test: {valid}")
    @classmethod
    def create_garden_network(cls, names):
        network = []
        for n in names:
            garden = cls(n)
            cls.gardens.append(garden)
            network.append(garden)
        return network   
    @staticmethod
    def cm_to_meters(cm: int):
        return cm / 100
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
    print(" ")
    print("=== Garden Management System Demo ===")
    gardens = Garden_Manager.create_garden_network(["Alice", "Bob"])
    gardens[0].add_plants(Plant("Oak Tree", 100, 1825))
    gardens[0].add_plants(Flowering_Plant("Rose", 25, 30, "red"))
    gardens[0].add_plants(Prize_Flower("Sunflower", 50, 30, "yellow", 10))
    gardens[1].add_plants(Plant("Pine", 90, 982))
    for garden in gardens:
        if garden.name == "Alice":
            garden.grow_plants()
            garden.show_report()
            break
    scores = {}
    for garden in gardens:
        if garden.name == "Alice":
            scores[garden.name] = Garden_Manager.GardenStats.garden_score(garden)
    print()
    for name, score in scores.items():
        print(f"Garden score - {name}: {score}")
        total = Garden_Manager.GardenStats.total_gardens()
    print(f"Total gardens managed: {total}")
    print(" ")