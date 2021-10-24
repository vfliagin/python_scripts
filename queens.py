import numpy

class ChessBoard:

    def __init__(self):
        self.board = numpy.zeros((8,8))
        self.queens_count = 0
        self.found_solutions = 0
        

    def show_the_board(self):
        for x in range(8):
            for y in range(8):
                print(self.board[x][y], end = " ")
            print("\n")
        print("\n")


    def is_beyond_the_border(self, x, y):
        return (x < 0 or x > 7 or y < 0 or y > 7)
            
    
    def place_the_queen(self, x, y):
        """Размещает ферзя на доске. Клетка с ферзем обозначается 1 в матрице,
        к клетке, на которую ферзь может сходить, прибавляется 2""" 
        
        if(self.board[x][y] != 0):
            return False
        
        self.board[x][y] = 1
        
        for vector_x in {-1, 0, 1}:
            for vector_y in {-1, 0, 1}:
        
                if(vector_x == 0 and vector_y == 0):
                    continue
                
                tmp_x = x + vector_x
                tmp_y = y + vector_y
                
                while(not self.is_beyond_the_border(tmp_x, tmp_y)):
                    self.board[tmp_x][tmp_y] += 2
                    tmp_x += vector_x
                    tmp_y += vector_y
                    
        self.queens_count += 1
        
        return True
    
    def remove_the_queen(self, x, y):
        
        if(self.board[x][y] != 1):
            return False
        
        self.board[x][y] = 0
        
        for vector_x in {-1, 0, 1}:
            for vector_y in {-1, 0, 1}:
        
                if(vector_x == 0 and vector_y == 0):
                    continue
                
                tmp_x = x + vector_x
                tmp_y = y + vector_y
                
                while(not self.is_beyond_the_border(tmp_x, tmp_y)):
                    self.board[tmp_x][tmp_y] -= 2
                    tmp_x += vector_x
                    tmp_y += vector_y
        
        self.queens_count -= 1
        
        return True
                    

    def search_for_solution(self, x, y):
        
        """Функция находит ближайшее место для ферзя и вызыает себя для поиска 
        места для следующего ферзя. Возвращает False, если такого места нет или
        если выбран вариант поиска нового решения. В случае возврата False, 
        функция убирает ферзя и продолжает поиск. Возвращает True, если выбран
        вариант не искать следующее решение или если решений больше нет."""
        
        if(self.queens_count == 8):
            self.found_solutions += 1
            self.show_the_board()
            answer = input("next solution? y/n")
            if answer == "y":
                return False
            return True
        
        while(not self.is_beyond_the_border(x, y)):
            if(self.board[x][y] == 0):
                self.place_the_queen(x, y)
                    
                if(y == 7):
                    new_x = x + 1
                    new_y = 0
                else:
                    new_x = x
                    new_y = y + 1
                    
                if(not self.search_for_solution(new_x, new_y)):
                    self.remove_the_queen(x, y)
                
            if(y == 7):
                x += 1
                y = 0
            else:
                y += 1
                        
        if(self.queens_count == 0):
            print("That was the last one. Total solutions: ", self.found_solutions)
            return True
        
        return False
    
def main():
    board = ChessBoard()
    board.search_for_solution(0, 0)

if __name__ == "__main__":
    main()
                
            
            










