class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Должность: {self.position} {self.surname} {self.name}'
    def get_total_income(self):
        return sum(self._income.values())

worker1 = Position('Светлана', 'Арефьева', 'Руководитель маркетингового отдела', 150000, 100000)
worker2 = Position('Виктор', 'Зыков', 'Сеньер', 350000, 150000)

print(f'{worker1.get_full_name()} зарабатывает {worker1.get_total_income()} рублей в месяц.')
print(f'{worker2.get_full_name()} зарабатывает {worker2.get_total_income()} рублей в месяц.')