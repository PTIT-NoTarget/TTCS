class Vehicle:
  def __init__(self, model, max_speed, mileage):
    self.model = model
    self.max_speed = max_speed
    self.mileage = mileage

  def __str__(self):
    return f"{self.model} {self.max_speed} {self.mileage}"

class Bus(Vehicle):
  def __init__(self, model, max_speed, mileage, capacity = 50):
    super().__init__(model, max_speed, mileage)
    self.capacity = capacity

  def __str__(self):
    return f"The seating capacity of a {self.model} is {self.capacity} passengers"

arr = input().split()
print(Bus(arr[0], arr[1], arr[2]))