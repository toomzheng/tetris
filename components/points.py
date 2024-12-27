class Point:
    '''
    A class representing a point on the Tetris board

    Attributes:
        x (int/float): x coordinate of the point
        y (int/float): y coordinate of the point
    '''

    def __init__(self, x=0, y=0):
        
        '''
        Initializes a new instance of the Point class.
        
        Parameters
        ----------
        x : int/float, optional
            x coordinate of point. The default is 0.
        y : int/float, optional
            y coordinate of point. The default is 0.

        Returns
        -------
        None.
        '''
        
        self.x = x
        self.y = y
  
    def rotate(self, pivot = None):
        
        '''
        Method to rotate a point by 90 degrees clockwise with respect 
        to a given pivot point. If no given point, default is origin.
        
        Parameters
        ----------
        pivot : Point, optional
            pivot. The default is None.

        Returns
        -------
        Point
            New point after 90 degree rotation.
        '''
        
        # sets default pivot point to origin, (0,0)
        if pivot is None:
            pivot = Point(0,0)
            
        # formula for pivot point
        new_x = (self.y - pivot.y) + pivot.x
        new_y = -(self.x - pivot.x) + pivot.y
        
        return Point(new_x, new_y)
          
    def __add__(self, a):
        
        '''
        Defines operator for adding two points
        
        Parameters
        ----------
        a : Point
            new point to be added to the point within self.

        Returns
        -------
        Point
            sum of two points.
        '''
        
        new_x = self.x + a.x
        new_y = self.y + a.y
        return Point(new_x, new_y)
    
    def __sub__(self, a):
        
        '''
        Defines operator for subtracting two points
        
        Parameters
        ----------
        a : Point
            new point to be subtracted from the point within self.

        Returns
        -------
        Point
            result of subtracting the new point from the point within self.
        '''
        
        new_x = self.x - a.x
        new_y = self.y - a.y
        return Point(new_x, new_y)
    
    def __eq__(self, a):
        
        '''
        Defines operator for testing the equivalence of two points. True if
        equal, False if not equal.
        
        Parameters
        ----------
        a : Point
            point to be compared to the point within self

        Returns
        -------
        bool
            If the two points are equivalent or not.
        '''
        
        if self.x == a.x and self.y == a.y:
            return True
        return False
    
    def __ne__(self, a):
        
        '''
        Defines operator for testing the nonequivalence of two points. True if
        not equal, False if equal.
        
        Parameters
        ----------
        a : Point
            point to be compared to the point within self

        Returns
        -------
        bool
            If the two points are nonequivalent or not.
        '''
        
        if self.x != a.x or self.y != a.y:
            return True
        return False
    
    def __repr__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    def __str__(self):
        '''
        Returns user friendly string

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        return 'x: ' + str(round(self.x,4)) + ' y: ' + str(round(self.y,4))

    
 
 
