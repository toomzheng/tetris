from points import Point as P

# Dictionaries that contain the different shapes for the tetris game
NAMES   = ['t','o','l','j','s','z','i']

VERTS = {'t':[P(0,0), P(0,1), P(1,1), P(1,2), P(2,2), P(2,1), P(3,1), P(3,0)], # T-shape
         'o':[P(0,0), P(0,2), P(2,2), P(2,0)], # O-shape
         'l':[P(0,0), P(0,3), P(2,3), P(2,2), P(1,2), P(1,0)], # L-shape
         'j':[P(0,2), P(0,3), P(2,3), P(2,0), P(1,0), P(1,2)], # J-shape
         's':[P(0,1), P(0,2), P(2,2), P(2,1), P(3,1), P(3,0), P(1,0), P(1,1)], # S-shape
         'z':[P(0,0), P(0,1), P(1,1), P(1,2), P(3,2), P(3,1), P(2,1), P(2,0)], # Z-shape
         'i':[P(0,0), P(0,1), P(4,1), P(4,0)] # I-shape
         }

# Add bounds to every object and then rotate

def h_to_rgb(hex_color):
    
    hex_color = hex_color.lstrip('#')  # Remove '#' if present
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

COLORS = {'t':h_to_rgb('#a6cee3'),'o':h_to_rgb('#1f78b4'),
          'l':h_to_rgb('#b2df8a'),'j':h_to_rgb('#33a02c'),
          's':h_to_rgb('#fb9a99'),'z':h_to_rgb('#e31a1c'),
          'i':h_to_rgb('#fdbf6f')}


def get_square_positions(name, verts, orientation):

    '''
    Returns the positions of the squares that make up a Tetris shape based on its name and orientation.
    
    Args:
        name (str): The name of the shape (e.g., 't', 'o', 'l', etc.).
        verts (list): A list of Point objects that represent the vertices of the shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
        
    Returns:
        list: A list of Point objects representing the positions of the 4 squares that form the shape.
    '''

    match name:
        case 't':
            return get_square_positions_t(verts, orientation)
        case 'o':
            return get_square_positions_o(verts, orientation)
        case 'l':
            return get_square_positions_l(verts, orientation)
        case 'j':
            return get_square_positions_j(verts, orientation)
        case 's':
            return get_square_positions_s(verts, orientation)
        case 'z':
            return get_square_positions_z(verts, orientation)
        case 'i':
            return get_square_positions_i(verts, orientation)

def get_minx_miny(verts):
    '''
    Returns the minimum x and y coordinates from a list of vertices.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the shape.
    
    Returns:
        tuple: A tuple containing the minimum x (mx) and minimum y (my) coordinates.
    '''

    mx = min([v.x for v in verts])
    my = min([v.y for v in verts])

    return mx, my
        
def get_square_positions_t(verts, orientation):
    '''
    Returns the positions of squares that form the T-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects that represent the vertices of the T-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the T-shape.
    '''
    
    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0:
            return [P(mx, my),P(mx+1, my), P(mx+2, my), P(mx+1, my+1)]
        case 1:
            return [P(mx, my),P(mx, my+1), P(mx, my+2), P(mx+1, my+1)]
        case 2:
            return [P(mx, my+1),P(mx+1, my+1), P(mx+2, my+1), P(mx+1, my)]
        case 3:
            return [P(mx+1, my),P(mx+1, my+1), P(mx+1, my+2), P(mx, my+1)]
            
def get_square_positions_o(verts, orientation):
    '''
    Returns the positions of squares that form the O-shaped Tetris piece (orientation is irrelevant for this shape).
    
    Args:
        verts (list): A list of Point objects representing the vertices of the O-shape.
        orientation (int): The orientation of the shape (ignored for O-shape).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the O-shape.
    '''

    mx, my = get_minx_miny(verts)

    return [P(mx, my),P(mx, my+1), P(mx+1, my), P(mx+1, my+1)]    
            
                        
def get_square_positions_l(verts, orientation):
    '''
    Returns the positions of squares that form the L-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the L-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the L-shape.
    '''
    
    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0:
            return [P(mx, my),P(mx, my+1), P(mx, my+2), P(mx+1, my+2)]
        case 1:
            return [P(mx, my+1),P(mx+1, my+1), P(mx+2, my+1), P(mx+2, my)]
        case 2:
            return [P(mx, my),P(mx+1, my), P(mx+1, my+1), P(mx+1, my+2)]
        case 3:
            return [P(mx, my),P(mx+1, my), P(mx+2, my), P(mx, my+1)]
            
                        
def get_square_positions_j(verts, orientation):
    '''
    Returns the positions of squares that form the J-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the J-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the J-shape.
    '''
    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0:
            return [P(mx, my+2),P(mx+1, my+2), P(mx+1, my+1), P(mx+1, my)]
        case 1:
            return [P(mx, my),P(mx+1, my), P(mx+2, my), P(mx+2, my+1)]
        case 2:
            return [P(mx, my),P(mx, my+1), P(mx, my+2), P(mx+1, my)]
        case 3:
            return [P(mx, my),P(mx, my+1), P(mx+1, my+1), P(mx+2, my+1)]
            
                        
def get_square_positions_s(verts, orientation):
    '''
    Returns the positions of squares that form the S-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the S-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the S-shape.
    '''
    
    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0 | 2:
            return [P(mx, my+1),P(mx+1, my+1), P(mx+1, my), P(mx+2, my)]
        case 1 | 3:
            return [P(mx, my),P(mx, my+1), P(mx+1, my+1), P(mx+1, my+2)]
        

def get_square_positions_z(verts, orientation):
    '''
    Returns the positions of squares that form the Z-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the Z-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the Z-shape.
    '''
    
    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0 | 2:
            return [P(mx, my),P(mx+1, my), P(mx+1, my+1), P(mx+2, my+1)]
        case 1 | 3:
            return [P(mx, my+1),P(mx, my+2), P(mx+1, my+1), P(mx+1, my)]

        
def get_square_positions_i(verts, orientation):
    '''
    Returns the positions of squares that form the I-shaped Tetris piece based on its orientation.
    
    Args:
        verts (list): A list of Point objects representing the vertices of the I-shape.
        orientation (int): The orientation of the shape (0, 1, 2, or 3).
    
    Returns:
        list: A list of Point objects representing the positions of the squares that form the I-shape.
    '''

    mx, my = get_minx_miny(verts)
    
    match orientation:
        
        case 0 | 2:
            return [P(mx, my),P(mx+1, my), P(mx+2, my), P(mx+3, my)]        
        case 1 | 3:
            return [P(mx, my),P(mx, my+1), P(mx, my+2), P(mx, my+3)]
        
        
        
