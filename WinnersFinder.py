class MadeAPoint:
    def __init__(self, board):
        self._board = board

    def check_winner(self, valor):
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                if self._board[row][col] == valor:
                    # Comprobando si el jugador tiene un punto
                    if self.check_line(row, col, valor):
                        return True
        return False

    def check_line(self, row, col, valor):
        result = False
        #Comprobando en vertical
        #* Como no se puede hacer una linea de tres en vertical desde abajo de la primera fila, no comprobaremos si hay una linea vertical por abajo de la primera fila
        if self.is_first_row(row):
            if self._board[row + 1][col] == valor and self._board[row + 2][col] == valor:
                result = True
                    
        #Comprobando en horizontal
        #* Dado a que el codigo verifica celda por celda no puede haber una linea horizontal en el medio de una linea o al final, ya que el programa ya habria encontrado coincidencias
        if self.is_first_col(col):
            if self._board[row][col + 1] == valor and self._board[row][col + 2] == valor:
                result = True
        
        #Comprobando en diagonal desde arriba izquierda hacia abajo derecha
        if self.is_first_row(row) and self.is_first_col(col):
            if self._board[row + 1][col + 1] == valor and self._board[row + 2][col + 2] == valor:
                result = True
        
        #Comprobando en diagonal desde arriba derecha hacia abajo izquierda
        if self.is_first_row(row) and self.is_last_col(col):
            if self._board[row + 1][col - 1] == valor and self._board[row + 2][col - 2] == valor:
                result = True
        return result
        
        

    def is_first_row(self, row):
        if not row > 0:
            return True
        else: return False
    def is_first_col(self, col):
        if not col > 0:
            return True
        else: return False
        
    def is_last_col(self, col):
        if not col < 2:
            return True
        else: return False
        