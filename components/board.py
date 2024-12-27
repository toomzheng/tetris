import pygame

class Block:
    
    '''
        A class to represent an individual block in the Tetris game grid.

        Attributes:
            x (int): The x-coordinate of the block.
            y (int): The y-coordinate of the block.
            color (tuple): The RGB color of the block.
    '''
        
    def __init__(self, p, color):
        '''
        Initializes a new block.

        Args:
            p (Point): A Point object representing the block's position.
            color (tuple): The RGB color of the block.
        '''
        
        self.x     = p.x
        self.y     = p.y
        self.color = color

    def draw(self, screen, p_size):
        '''
        Draws the block on the game screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the block will be drawn.
            p_size (int): The size of the block in pixels.
        '''
        
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x * p_size, self.y * p_size, p_size, p_size))



class Board:
    '''
    A class to represent the Tetris game board.
    
    Attributes:
        width (int): The width of the game board (in blocks).
        height (int): The height of the game board (in blocks).
        pix_size (int): The pixel size of each block. (Used for visualization purposes)
        grid (list): A 2D list representing the grid of blocks (None for empty cells, Block for filled).
    '''

    def __init__(self, w, h, pixel_size = 30):
        '''
        Initializes the Tetris game board.

        Args:
            w (int): The width of the board in number of blocks.
            h (int): The height of the board in number of blocks.
            pixel_size (int, optional): The size of each block in pixels. Default is 30.
        '''

        self.width    = w
        self.height   = h
        self.pix_size = pixel_size
        self.grid     = [[None for _ in range(self.width)] for _ in range(self.height)]

        
    def check_collision(self, tet):
        '''
        Checks if the active Tetromino has collided with the edges of the board or other placed blocks.

        Args:
            tet (Tetromino): The Tetromino object currently falling.
        
        Returns:
            bool: True if there is a collision, False otherwise.
        '''
        
        # check for collision with walls on either side or bottom
        for v in tet.verts:
            if v.x > self.width or v.x < 0 or v.y > self.height:
                return True
            
        # check for collision with other squares
        # if any Tetromino square in self.grid is already occupied, collision is True
        for square in tet.squares:
            if square.y >= 0 and self.grid[square.y][square.x] is not None:
                return True
        
        return False
            
    
    def place_tetromino(self, tet):
        '''
        Places a Tetromino on the game board by adding its blocks to the grid.

        Args:
            tetromino (Tetromino): The Tetromino object to be placed on the board.
        '''

        for s in tet.squares:
            self.grid[s.y][s.x] = Block(s, tet.color)
                                
            
    def clear_rows(self):
        '''
        Clears any rows that are completely filled with blocks and shifts blocks above down by one row.
        '''
                
        """
        pseudocode for clear_rows
        1) first check if any are full
        2) if a row is full, remove the row
        3) shift everything down by 1 from 0 to that row
        4) insert None afterwards at index 0
        """
        
        for row_index, row in enumerate(self.grid):
            
            # check if any rows are full by first assuming all rows are full
            row_full = True
            for cell in row:
                # if there is a cell with None, row is not full
                if cell is None:
                    row_full = False
            
            # if there's a full row, use the index of the full row to remove it
            if row_full == True:
                del self.grid[row_index]

                # shifts all remaining squares down by one square in the grid
                for i in range(row_index):
                    for square in self.grid[i]:
                        if square is not None:
                            square.y += 1
                
                # add empty row at the start of list self.grid
                self.grid.insert(0, [None] * self.width)
                
        
    def draw(self, screen):
        '''
        Draws the game board and all placed blocks on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface where the game board will be drawn.
        '''

        for row in self.grid:
            for block in row:
                if block:
                    block.draw(screen, self.pix_size)
        

if __name__ == "__main__":
    pass
