from random import randint, choice


class Lotto:

    def __init__(self):
        self.lines = 3
        self.columns = 9
        self.nums_card = 15
        self.max_num = 90
        self.nums_line = 5


class Card(Lotto):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.matrix = []
        range_num = list(range(1, self.max_num + 1))
        count = 0
        while count < self.lines:
            count += 1
            row = []
            while len(row) < self.nums_line:
                rand_num = choice(range_num)
                if rand_num not in row:
                    row.append(rand_num)
                    range_num.remove(rand_num)
            row.sort()
            for _ in range(len(row)):
                row.insert(randint(0, len(row)), ' ')
            self.matrix.append(row)

    def __str__(self):
        result = ''
        sep_head = round((self.columns ** 2 - len(self.name)) / 2)
        print('-' * sep_head + self.name + '-' * sep_head)
        for i in self.matrix:
            result += ('¦\t' + '\t¦\t'.join(map(str, i)) + '\t¦' + '\n' + '-' * (self.columns ** 2) + '\n')
        return result

    def __iter__(self):
        return iter(self.matrix)


class Game(Card):

    def __init__(self, human, computer):
        super().__init__(name=None)
        self.human = human
        self.computer = computer
        self.kegs_num = list(range(1, self.max_num + 1))

    def start(self):
        count = 1
        while count < self.max_num:
            keg_num = self.kegs_num.pop(randint(0, len(self.kegs_num) - 1))
            print(f'Новый бочонок: {keg_num} (Осталось {len(self.kegs_num)})')
            count += 1
            print(self.human)
            print(self.computer)
            user_answer = input('Зачеркнуть цифру? (y/n) --> ')
            if self.cross_out_num(self.human, keg_num):
                if user_answer != 'y':
                    print('Вы проиграли, номер есть в карточке')
                    break
            else:
                if user_answer != 'n':
                    print('Вы проиграли, такого номера нет в карточке')
                    break
            self.cross_out_num(self.computer, keg_num)

            if self.amount_num(self.human) == 0:
                print('☻☻☻ Победитель определен. Карточка победителя ☻☻☻\n', self.human)
                break
            elif self.amount_num(self.computer) == 0:
                print('☻☻☻ Победитель определен. Карточка победителя ☻☻☻\n', self.computer)
                break

    @staticmethod
    def cross_out_num(card, keg_num):
        result = False
        for row in card:
            for i in range(len(row)):
                if row[i] == keg_num:
                    row[i] = '☺'
                    result = True
        return result

    @staticmethod
    def amount_num(player):
        count = 0
        for row in player:
            for i in row:
                if str(i).isdigit():
                    count += 1
        return count


a = Card('Игрок')
b = Card('Компьютер')
game = Game(a, b)

game.start()