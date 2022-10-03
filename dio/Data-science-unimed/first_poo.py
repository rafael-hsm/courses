from time import sleep

class Bike:
    def __init__(self, color, brand, year, value) -> None:
        self.color = color
        self.brand = brand
        self.year = year
        self.value = value

    def honk(self):
        print("Plin plin...")

    def stop(self):
        print("Stopping the bike")
        sleep(1)
        print("Bicycle stopped!!!")

    def run(self):
        print("Vrummmmmmm")
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"

if __name__ == "__main__":
    by = Bike("Red", "Montra Trance", 200, 1_500)
    print(by)
    # print(dir(by))
    print(by.brand)
    by.honk()
    by.run()
    by.stop()
