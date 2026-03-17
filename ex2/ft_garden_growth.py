class Plant():
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
    def grow(self, days: int, daily_growth: int) -> None:
        initial_height = self.height
        self.age += days
        self.height += days * daily_growth
        self.get_info()
if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30), Plant("Tulipe", 12, 23), Plant("Sunflower", 7, 10)]
    print("=== Day 1 ===")
    for plant in plants:
        plant.get_info()
    print("=== Day 7 ===")
    for plant in plants:
        initial_height = plant.height
        plant.grow(6, 1)
    print(f"Growth this week +{plant.height - initial_height}cm")


