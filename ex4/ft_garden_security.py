class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"Invalid operation attempted: days {age} [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days [OK]")
    def set_height(self, height: int) -> None:
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def get_age(self) -> int:
        return self.__age
    def get_height(self) -> int:
        return self.__height
    
if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 0, 0)
    print(f"Plant created: {plant1.name}")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-5)
    print("\n")
    print(f"Current plant: {plant1.name} ({plant1.get_height()}cm, {plant1.get_age()})")




