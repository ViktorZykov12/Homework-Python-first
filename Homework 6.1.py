import time

class TrafficLight:
    def __init__(self):
        self.color = ('Красный', 'Желтый', 'Зеленый')
    def running(self, time_green):
        while True:
            print(self.color[0])
            time.sleep(7)
            print(self.color[1])
            time.sleep(2)
            print(self.color[2])
            time.sleep(time_green)
time_green = int(input('Введите время работы зеленого сфетофора: '))
traffic_light = TrafficLight()
traffic_light.running(time_green)
