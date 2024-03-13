class Vehicle:
  def __init__(self, model, max_speed, mileage, color = "White"):
    self.model = model
    self.max_speed = max_speed
    self.mileage = mileage
    self.color = color

  def fare(self):
    return self. mileage * 100

  def __str__(self):
    return f"{self.color} {self.model} {self.max_speed} {self.mileage}"

class Bus(Vehicle):
  def __init__(self, model, max_speed, mileage):
    super().__init__(model, max_speed, mileage)
  
  def fare(self):
    return "%.1f" % (self.mileage * 100 * 1.1)

  def __str__(self):
    return f"Total Bus fare is: {self.fare()}"

class Car(Vehicle):
  def __init__(self, model, max_speed, mileage):
    super().__init__(model, max_speed, mileage)

  def __str__(self):
    return f"Total Car fare is: {self.fare()}"

arr = input().split()
if arr[3] == "(bus)":
  print(Bus(arr[0], int(arr[1]), int(arr[2])))
else:
  print(Car(arr[0], int(arr[1]), int(arr[2])))

arr = input().split()
if arr[3] == "(bus)":
  print(Bus(arr[0], int(arr[1]), int(arr[2])))
else:
  print(Car(arr[0], int(arr[1]), int(arr[2])))