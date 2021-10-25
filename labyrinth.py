import numpy

"""Программа создает случайный лабиринт 8х8 и находит из него выход."""


class Block:
    def __init__(self, block_type):
        """Блок содержит информацию о том, за сколько шагов до него можно дойти, ссылку на блок,
        из которого до него можно дойти, код типа блока
        (-1 - стена, 0 - пустое пространство, 1 - старт, 2 - финиш, 3 - путь к выходу)"""
        self.previous_block = None
        self.steps = None
        self.type = block_type

    def print_self(self):
        """Функция выписывает в консоль тип блока с соответствующей подсветкой."""
        if self.type == 0:
            print("+" + str(self.type), end="")
        elif self.type > 0:
            print('\x1b[6;30;42m' + "+" + str(self.type) + '\x1b[0m', end="")
        else:
            print('\x1b[6;30;41m' + str(self.type) + '\x1b[0m', end="")


class Labyrinth:
    def __init__(self):
        """Функция случайно генерирует число стен, создает список из 64 блоков и создает их случайную пермутацию"""
        self.amount_of_wall_segments = numpy.random.randint(0, 30)
        self.labyrinth_plan = []

        for x in range(self.amount_of_wall_segments):
            self.labyrinth_plan.append(Block(-1))

        self.labyrinth_plan.append(Block(1))
        self.labyrinth_plan.append(Block(2))

        for x in range(64 - self.amount_of_wall_segments - 2):
            self.labyrinth_plan.append(Block(0))

        self.labyrinth_plan = numpy.random.permutation(self.labyrinth_plan)

    def show_labyrinth(self):
        for x in range(8):
            for y in range(8):
                self.labyrinth_plan[x * 8 + y].print_self()
                print("", sep="", end=" ")
            print("")

    @staticmethod
    def find_the_neighbours(i):
        res = []

        if i % 8 != 0:
            res.append(i - 1)
        if i % 8 != 7:
            res.append(i + 1)
        if i + 8 <= 63:
            res.append(i + 8)
        if i - 8 >= 0:
            res.append(i - 8)

        return res

    def check_the_neighbours(self, i, to_check):
        """Функция проверяет соседние с i блоки. Если у блока нет предшественника, он добавляется в очередь,
        заполняются переменные previous_block и steps. Возвращается выход (если он найден) или None."""

        neighbours = self.find_the_neighbours(i)

        for x in neighbours:
            if self.labyrinth_plan[x].type != -1:
                if self.labyrinth_plan[x].previous_block is None:
                    self.labyrinth_plan[x].previous_block = i
                    self.labyrinth_plan[x].steps = self.labyrinth_plan[i].steps + 1
                    to_check.append(x)
                if self.labyrinth_plan[x].type == 2:
                    return x
        return None

    def find_the_exit(self):
        """Функция ищет выход из лабиринта. Находится стартовый блок. Создается очередь блоков,
        которые нужно проверить. Изначально это старт, потом его соседи и т.д.
        Когда очередь становится пустой, либо находится старт,
        функция выписывает результат (путь от финиша к старту либо сообщение, что пути нет.)."""
        to_check = []
        escape = None

        for x in range(64):
            if self.labyrinth_plan[x].type == 1:
                to_check.append(x)
                self.labyrinth_plan[x].steps = 0
                self.labyrinth_plan[x].previous_block = x

        while to_check and escape is None:
            current_block = to_check.pop(0)
            escape = self.check_the_neighbours(current_block, to_check)

        if escape is None:
            self.show_labyrinth()
            print("No escape.")
            return

        tmp = self.labyrinth_plan[escape].previous_block
        while self.labyrinth_plan[tmp].steps != 0:
            self.labyrinth_plan[tmp].type = 3
            tmp = self.labyrinth_plan[tmp].previous_block
        self.show_labyrinth()


def main():
    test = Labyrinth()
    test.find_the_exit()


if __name__ == "__main__":
    main()
