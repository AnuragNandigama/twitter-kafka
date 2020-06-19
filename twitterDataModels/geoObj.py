from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Any
import datetime, json

@dataclass
class Coordinates:
    coordinates: list
    type: str        
    
@dataclass
class BoundingBox:
    type: str
    coordinates: List[list]
    
@dataclass
class Place:
    id: str
    url: str
    place: str
    name: str
    full_name: str
    country_code: str
    country: str
    bounding_box: BoundingBox
    attributes: str
    
    
        
        