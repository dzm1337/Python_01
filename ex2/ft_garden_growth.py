class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, days: int, daily_growth: int) -> None:
        self.age += days
        self.height += days * daily_growth
        self.get_info()


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 12, 23),
        Plant("Sunflower", 7, 10),
    ]

    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()

    print("=== Day 7 ===")
    for plant in plants:
        initial_height = plant.height
        plant.grow(6, 1)
        growth = plant.height - initial_height
        print(f"Growth this week +{growth}cm")
