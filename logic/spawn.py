import random
from abc import ABC, abstractmethod
from logic.cell import Cell, Level, FireCell, IceCell

class Spawn:
    
    def __init__(self, life=300, positions=None, board=None):
        self.life = life
        self.positions = positions
        self.board = board
        self.type = self.get_type()
        
    def set_life(self, life):
        self.life = life
        
    def set_board(self, board):
        self.board = board
        
    def get_positions(self):
        return self.positions

    def get_life(self):
        return self.life
        
    def decrease_life(self, damage):
        life -= damage
    
    def __str__(self):
        return 'SP' 
    
    def get_adjacents(self, posXY):
        row, col = posXY
        length = len(self.board)
        adjacentList = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < length and 0 <= new_col < length:
                cell = self.board.get_cells(new_row, new_col)
                if (str(cell) == ' '):
                    adjacentList.append(cell)
        return adjacentList
    
    def get_type(self):
        return 'Spawn'

    def generate_cells(self):
        if self.position is not None:
            tuplePos = self.position
            positionsList = self.get_adjacents_for_move(tuplePos)
            cantCells = random.randint(0,4)
            for i in range(cantCells):
                position = random.choice(positionsList)
                positionsList.remove(position)
                cellN = Cell.__init__(1, 20, position, self.board)

    def fight(self, cell):
        if cell.get_position() in self.get_positions():
            new_life = self.get_life() - cell.get_life()
            if new_life > 0:
                self.set_life(new_life)
                self.board.remove_cell(*cell.get_position(), cell)
            else:
                self.set_life(0)
    
    @staticmethod
    def from_string(spawn_str):
        if spawn_str == IceSpawn().__str__():
            return IceSpawn()
        elif spawn_str == FireSpawn().__str__():
            return FireSpawn()
        else:
            raise ValueError(f'Invalid spawn string: {spawn_str}')

class FireSpawn(Spawn):
        
    def set_life(self, life):
        self.life = life
        
    def set_board(self, board):
        self.board = board
        
    def decrease_life(self, damage):
        life -= damage
    
    def __str__(self):
        return 'FS'
    
    def get_type(self):
        return 'FireSpawn'
    
    def __eq__(self, other):
        return isinstance(other, FireSpawn)    
    
    def generate_cells(self):
        if self.position is not None:
            tuplePos = self.position
            positionsList = self.get_adjacents_for_move(tuplePos)
            cantCells = random.randint(0,4)
            for i in range(cantCells):
                position = random.choice(positionsList)
                positionsList.remove(position)
                cellN = FireCell.__init__(1, 20, position, self.board)

class IceSpawn(Spawn):
    def __str__(self):
        return 'IS'
    
    def __eq__(self, other):
        return isinstance(other, IceSpawn)
        
    def set_life(self, life):
        self.life = life
        
    def set_board(self, board):
        self.board = board
        
    def decrease_life(self, damage):
        life -= damage
        
    def generate_cells(self):
        if self.position is not None:
            tuplePos = self.position
            positionsList = self.get_adjacents_for_move(tuplePos)
            cantCells = random.randint(0,4)
            for i in range(cantCells):
                position = random.choice(positionsList)
                positionsList.remove(position)
                cellN = IceCell.__init__(1, 20, position, self.board)

    def get_type(self):
        return 'IceSpawn'