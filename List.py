class Vehicle:
    def __init__(self, Name, Speed, Mileage):
        self.Name = Name
        self.Speed = Speed
        self.Mileage = Mileage

def display(car):
    print(f"{car.Name} has a speed of {car.Speed} Km/hr with mileage {car.Mileage}")

# Creating an instance of the Vehicle class
car = Vehicle(
    input("Enter the name of Vehicle: "),
    int(input("Enter the speed in Km/hr: ")),
    float(input("Enter the mileage: "))
)

# Calling the display function with the instance as an argument
display(car)
