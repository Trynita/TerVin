from dataclasses import dataclass
import pygame, pytmx, pyscroll

@dataclass
class Map:
    name: str
    walls: list([pygame.Rect])
    group: pyscroll.PyscrollGroup
    
    
class Map_manager:
    def __init__(self):
        self.maps = dict()
        self.current_map = "carte"
        
    