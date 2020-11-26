class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} car is going')

    def stop(self):
        print(f'{self.name} car is stopping')

    def turn(self, direction):
        print(f'{self.name} turning {direction}')
    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 60:
            print('Warning you speed more 60')
class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f'Speed: {self.speed}')
        if self.speed > 40:
            print('Warning you speed more 40')

class PoliceCar(Car):
    pass

town_car = TownCar(61, 'green', 'Nissan', False)
sport_car = SportCar(250, 'white', 'Porshe', False)
work_car = WorkCar(41, 'yellow', 'Ford', False)
police_car = PoliceCar(100, 'blue', 'Lada', True)

town_car.show_speed()
sport_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')