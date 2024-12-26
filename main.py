from ValueControl import ValueControl
from WinnersFinder import MadeAPoint

matriz = [["X", "O", "X"], ["O", "O","X"], ["X", "X", "O"]]

class Judge:
    def __init__(self):
        self.__board = None
        self.MadeAPoint = None
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board):
        ValueControl(board).check_board()
        self.__board = board
        self.MadeAPoint = MadeAPoint(board)
    def who_won(self, player):
        return self.MadeAPoint.check_winner(player)         
# Uso del código corregido
judge = Judge()
judge.board = matriz  # Esto debería funcionar si la matriz es válida.
if judge.who_won("X"):
    print("Las X ganan")
elif judge.who_won("O"):
    print("Las O ganan")
else:
    print("No hay ganador")
    
    
for i in matriz:
    print(i)