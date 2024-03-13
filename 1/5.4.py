class Vehicle:
  def __init__(self, model, max_speed, mileage, color = "White"):
    self.model = model
    self.max_speed = max_speed
    self.mileage = mileage
    self.color = color

  def __str__(self):
    return f"{self.color} {self.model} {self.max_speed} {self.mileage}"

arr = input().split()
print(Vehicle(arr[0], arr[1], arr[2]))
arr = input().split()
print(Vehicle(arr[0], arr[1], arr[2]))