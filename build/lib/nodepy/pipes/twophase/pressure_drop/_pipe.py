import math

class Pipe():
    """A class representing a cylindrical pipe, providing its geometric properties.
    
    Attributes:
        diam (float) : The outer diameter of the pipe.
        length (float) : The length of the pipe (default is 1.0).
        rough (float) : Absolute roughness of the pipe (m).
    
    Properties:
        radius (float): Returns the radius of the pipe.
        circumference (float): Returns the outer circumference of the pipe.
        surface_area (float): Returns the external surface area of the pipe.
        csa (float): Returns the cross-sectional area of the pipe.
        volume (float): Returns the internal volume of the pipe (assuming a solid cylinder).

    """

    def __init__(self,diam:float,length:float=1.,rough:float=None):
        """Initializes a Pipe object with diameter and length."""
        
        self.diam   = diam
        self.length = length
        self.rough  = rough

    @property
    def radius(self) -> float:
        """Returns the radius of the pipe."""
        return self.diam / 2

    @property
    def circumference(self) -> float:
        """Returns the outer circumference of the pipe."""
        return math.pi * self.diam

    @property
    def surface_area(self) -> float:
        """Returns the external surface area of the pipe (excluding ends)."""
        return self.circumference * self.length

    @property
    def csa(self) -> float:
       """Getter for the cross-sectional area of the pipe."""
       return math.pi*(self.diam**2)/4

    @property
    def volume(self) -> float:
        """Returns the volume of the pipe (assuming a solid cylinder)."""
        return self.csa * self.length

    @property
    def epd(self):
        """Returns relative roughness of the pipe."""
        return None if self.rough is None else self.rough/self.diam
    