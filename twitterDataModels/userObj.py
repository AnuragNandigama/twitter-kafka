from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any

@dataclass
class User:
    id: int
    id_str: str
    name: str
    screen_name: str 
    location: str
    url: str
    description: str
    translator_type: str
    protected: bool
    verified: bool
    followers_count: int
    friends_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: str
    utc_offset: str
    time_zone: str
    geo_enabled: bool
    lang: str
    contributors_enabled: bool
    is_translator: bool
    profile_background_color: str
    profile_background_image_url: str
    profile_background_image_url_https: str
    profile_background_tile: bool
    profile_link_color: str
    profile_sidebar_border_color: str
    profile_sidebar_fill_color: str
    profile_text_color: str
    profile_use_background_image: bool
    profile_image_url: str
    profile_image_url_https: str
    profile_banner_url: str
    default_profile: bool
    default_profile_image: bool
    following: int
    follow_request_sent: int
    notifications: int
                