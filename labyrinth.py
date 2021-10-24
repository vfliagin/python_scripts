import numpy

"""Программа создает случайный лабиринт 8х8 и находит из него выход."""

class Block:
    def __init__(self, block_type):
        """Блок содержит информацию о том, за сколько шагов до него можно дойти, ссылку на блок, из которого до него
        можно дойти, код типа блока (-1 - стена, 0 - пустое пространство, 1 - старт, 2 - финиш)"""
        self.previous_block = None
        self.steps = None
        self.type = block_type


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
                print(self.labyrinth_plan[8 * x + y].type, end=" ")
            print("")

    def check_the_neighbours(self, i, to_check):
        """Функция проверяет соседние с i блоки. Если у блока нет предшественника, он добавляется в очередь, заполняются
        переменные previous_block и steps. Возвращается выход (если он найден) или None."""
        for x in [i + 1, i - 1, i + 8, i - 8]:
            if 0 <= x <= 63 and self.labyrinth_plan[x].type != -1:
                if self.labyrinth_plan[x].previous_block is None:
                    self.labyrinth_plan[x].previous_block = i
                    self.labyrinth_plan[x].steps = self.labyrinth_plan[i].steps + 1
                    to_check.append(x)
                if self.labyrinth_plan[x].type == 2:
                    return x
        return None

    def find_the_exit(self):
        """Функция ищет выход из лабиринта. Находится стартовый блок. Создается очередь блоков, которые нужно проверить.
         Изначально это старт, потом его соседи и т.д. Когда очередь становится пустой, либо находится старт, функция
         выписывает результат (путь от финиша к старту либо сообщение, что пути нет.)."""
        to_check = []
        escape = None

        for x in range(64):
            if self.labyrinth_plan[x].type == 1:
                to_check.append(x)
                self.labyrinth_plan[x].steps = 0
                self.labyrinth_plan[x].previous_block = x

        while to_check and escape is None:
            current_block = to_check.pop()
            escape = self.check_the_neighbours(current_block, to_check)

        if escape is None:
            print("No escape.")
            return

        tmp = escape
        while self.labyrinth_plan[tmp].steps != 0:
            print(tmp)
            tmp = self.labyrinth_plan[tmp].previous_block
        print(tmp)


def main():
    test = Labyrinth()
    test.show_labyrinth()
    test.find_the_exit()


if __name__ == "__main__":
    main()
