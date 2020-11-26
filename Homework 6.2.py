class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_of_asphalt, thickness):
        return self._length * self._width * mass_of_asphalt * thickness / 1000

road = Road(20,5000)
print(f'Для покрытия дорожного полотна необходимо {road.mass(25, 5)} кг асфальта.')
