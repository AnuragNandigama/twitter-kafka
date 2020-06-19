from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any

@dataclass
class ImageSize:
    w: int
    h: int
    resize: str

@dataclass
class ImageTypeSize:
    thumb: ImageSize
    small: ImageSize
    medium: ImageSize
    large: ImageSize 

@dataclass
class Monetizable:
    monetizable: bool
    
@dataclass
class Media:
    id: int
    id_str: str
    indices: list
    additional_media_info: Monetizable
    media_url: str
    media_url_https: str
    url: str
    display_url: str
    expanded_url: str
    type: str
    sizes: ImageTypeSize
    source_status_id: int
    source_status_id_str: str
    source_user_id: int
    source_user_id_str: str
    
        