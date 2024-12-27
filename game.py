import pygame
import random

from points import Point as P
from pieces import Tetromino as T
from board import Board
import utils

class TetrisGame:
    '''
    A class to represent a Tetris game, which manages the game board, Tetromino pieces, and user interactions.

    Attributes:
        board (Board): The game board where Tetromino pieces are placed.
        names (list): A list of Tetromino piece names.
        verts (dict): A dictionary containing the vertices for different Tetromino pieces.
        colors (dict): A dictionary mapping Tetromino pieces to their respective colors.
        tetromino (Tetromino): The current active Tetromino piece.
        screen (pygame.Surface): The Pygame display window for the game.
        clock (pygame.time.Clock): A Pygame clock to control the game's frame rate.
    '''
    
    def __init__(self, size, aspect_ratio, block_size, verts, colors):
        '''
        Initializes a new instance of the TetrisGame class.

        Args:
            size (int): The width of the game board (in blocks).
            aspect_ratio (int): The aspect ratio (height-to-width ratio) of the game board.
            block_size (int): The size of each block (in pixels).
            verts (dict): A dictionary containing vertices for different Tetromino pieces.
            colors (dict): A dictionary mapping Tetromino names to their colors.
        '''
        
        # Initialize the game window
        pygame.init()
        
        self.board     = Board(size, aspect_ratio*size, block_size)
        self.names     = list(verts.keys())
        self.verts     = verts
        self.colors    = colors
        self.tetromino = self.generate_new_tetromino()
        self.screen    = pygame.display.set_mode((size*block_size, size*block_size*aspect_ratio))

        # Keep track of game time
        self.clock     = pygame.time.Clock()

                
    def generate_new_tetromino(self):
        '''
        Generates a new random Tetromino piece and places it in the starting position.

        Returns:
            Tetromino: A new randomly selected Tetromino object.
        '''
        
        # Pick a new piece to be sent into the game
        r_piece = random.choice(self.names) 
        return T(r_piece, self.verts[r_piece], self.colors[r_piece], dx = self.board.width//2)

    def step(self):
        '''
        Moves the active Tetromino piece down by one block and handles collisions. 
        If a collision occurs, places the Tetromino on the board and generates a new piece.

        Returns:
            bool: False if the game is over, True otherwise.
        '''
        
        # Push piece down
        self.tetromino.move(0, 1)

        if self.board.check_collision(self.tetromino):

            # If collision is detected reset piece position
            self.tetromino.move(0, -1)
            
            # Add piece to grid
            self.board.place_tetromino(self.tetromino)

            # Check if grid needs to be cleared
            self.board.clear_rows()

            # Create the next piece
            self.tetromino = self.generate_new_tetromino()

            # If this piece has a collision game is over
            if self.board.check_collision(self.tetromino):
               return False

        return True

    
    def rotate_tetromino(self):
        '''
        Rotates the active Tetromino piece. 
        If the rotation results in a collision, the rotation is undone.
        '''

        old_obj = self.tetromino.copy()
        self.tetromino.rotate()

        # If collision is detected reset tetromino
        if self.board.check_collision(self.tetromino):
            self.tetromino = old_obj

            
    def draw(self):
        '''
        Draws the current game state, including the board and the active Tetromino piece, to the screen.
        '''
        
        # Draw grid and tetromino
        self.screen.fill((225,225,225))
        self.board.draw(self.screen)
        self.tetromino.draw(self.screen)
        
        
    def move_tetromino(self, dx, dy):
        '''
        Moves the active Tetromino piece by the specified x and y distances.

        Args:
            dx (int): The distance to move in the x direction.
            dy (int): The distance to move in the y direction.
        '''
        
        self.tetromino.move(dx, dy)
        if self.board.check_collision(self.tetromino):
            self.tetromino.move(-dx, -dy)

    def run_game(self, gamespeed = 4):
        '''
        Runs the main game loop, handling user input, updating the game state, and drawing the game window.

        Args:
          gamespeed(int): Sets how fast the piece travels
        '''
        
        # Flag to check if game should continue
        running   = True
        
        while running:

            # Main event loop
            for event in pygame.event.get():

                # What if user presses quit window
                if event.type == pygame.QUIT:
                    running = False

                # What if user presses a key
                elif event.type == pygame.KEYDOWN:

                    match event.key:
                        # Left arrow is pressed
                        case pygame.K_LEFT:
                            self.move_tetromino(-1,0)
                        # Right arrow is pressed
                        case pygame.K_RIGHT:
                            self.move_tetromino(1,0)
                        # Up arrow is pressed
                        case pygame.K_UP:
                            self.rotate_tetromino()
                        # Down arrow is pressed
                        case pygame.K_DOWN:
                            self.move_tetromino(0,1)
                        # q key is pressed
                        case pygame.K_q:
                            running = False

            if running:
                # Update the game
                running = self.step()

            # Redraw windown
            self.draw()
            pygame.display.flip()

            # A brief pause to the game
            self.clock.tick(gamespeed)

    pygame.quit()
    
            
def main():

    '''
    The entry point of the game. Initializes and runs the TetrisGame.
    '''

    # Feel free to change these numbers and play the game    
    # Constants for the game
    SIZE          = 10   # 10 blocks in the x-direction
    BLOCK_SIZE    = 30   # block size in pixels
    ASPECT_RATIO  = 2    # 20 blocks in the y-direction

    # Create a game object
    game          = TetrisGame(SIZE, ASPECT_RATIO, BLOCK_SIZE, utils.VERTS, utils.COLORS)

    game.run_game()
    
if __name__ == "__main__":
    main()
