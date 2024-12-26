class ValueControl:
    def __init__(self, board):
        self._board = board
    def check_board(self):
        if self.is_valid_size_board():
            return True
    def is_valid_size_board(self):
        # Verificar que el tablero sea una lista
        if not isinstance(self._board, list):
            raise ValueError("The board must be a list of lists (A matrix)")  # Si no es una lista.
        # Verificar que el tablero tenga exactamente 3 filas
        if len(self._board) != 3:
            raise ValueError("The board must have three rows")  # Si no hay exactamente 3 filas.
        for row in self._board:
            # Verificar que cada fila tenga exactamente 3 columnas
            if len(row) != 3:
                raise ValueError("The board must have three columns")  # Si alguna fila no tiene 3 columnas.
        return True  # Si todas las comprobaciones son correctas.