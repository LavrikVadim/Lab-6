class Car:
    className = 'Car'
    objectsCount = 0

    def __init__(self, capacity, consumption, avr_speed):
        self.capacity = capacity
        self.consumption = consumption
        self.avr_speed = avr_speed
        Car.objectsCount = Car.objectsCount + 1


    def distance_fulltank(self):
        return (self.capacity / self.consumption) * 100
        
    def __add__(self, other):
        return Car(self.average_speed + other.average_speed)
    
    def info(self):
        print(f'Тип: {Car.className}')
        print(f"Емкость бака: {self.capacity} л")
        print(f"Расход топлива: {self.consumption} л/100 км")
        print(f"Средняя скорость: {self.avr_speed} км/ч")


class Truck(Car):
    className = 'Truck'

    def __init__(self, capacity, consumption, avr_speed, weight):
        super().__init__(capacity, consumption, avr_speed)
        self.weight = weight

    def ratio(self):
        return self.weight / (self.consumption * 250)
    
    def info(self):
        super().info()
        print(f'Тип: {Truck.className}')
        print(f"Емкость бака: {self.capacity} л")
        print(f"Расход топлива: {self.consumption} л/100 км")
        print(f"Средняя скорость: {self.avr_speed} км/ч")
        print(f"Вес грузовика: {self.weight} кг")
    
    
class Bus(Car):
    className = 'Bus'
    
    def __init__(self, capacity, consumption, avr_speed, passengers):
        super().__init__(capacity, consumption, avr_speed)
        self.passengers = passengers

    def ratio(self):
        return self.passengers / (self.consumption * 250)
    
    def info(self):
        super().info()
        print(f'Тип: {Bus.className}')
        print(f"Емкость бака: {self.capacity} л")
        print(f"Расход топлива: {self.consumption} л/100 км")
        print(f"Средняя скорость: {self.avr_speed} км/ч")
        print(f"Количество пассажиров: {self.passengers} человек")


car1 = Car(50, 8, 25)
car1.info()

truck = Truck(120, 10, 80, 3250)

print(f"Расстояние до полного опустошения бака(грузовик): {truck.distance_fulltank():.2f} км")
print(f"Вес груза / количество топлива на 250 км: {truck.ratio():.2f}")

bus = Bus(248, 25, 20, 50)

print(f"Расстояние до полного опустошения бака(автобус): {bus.distance_fulltank():.2f} км")
print(f"Количество пассажиров / количество топлива на 250 км: {bus.ratio():.2f}")

print(f'Objects count: {Car.objectsCount}')