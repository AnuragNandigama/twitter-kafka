from dataclasses import dataclass, field
from utilities import deleteAttributes as da
from typing import List, Dict, Tuple, Any
import datetime
from twitterDataModels import tweetObj as tto
from twitterDataModels import userObj as tuo
from twitterDataModels import entitiesObj as teo
from twitterDataModels import extendedEntitiesObj as teeo
from twitterDataModels import quotedStatusObj as qso
from twitterDataModels import geoObj as geobj

@dataclass
class ExtendedTweet:
    full_text: str
    display_text_range: list
    entities: teo.Entities


#Skipping RetweetedStatus for a while
@dataclass
class QuotedStatus:
    created_at: str
    id: int
    id_str: str
    text: str
    source: str
    truncated: bool
    in_reply_to_status_id: int
    in_reply_to_status_id_str: str
    in_reply_to_user_id: int
    in_reply_to_user_id_str: str
    in_reply_to_screen_name: str
    user: tuo.User
    geo: geobj.Coordinates
    coordinates: geobj.Coordinates
    place: geobj.Place
    contributors: str
    is_quote_status: bool
    extended_tweet: ExtendedTweet
    quote_count: int
    reply_count: int
    retweet_count: int
    favorite_count: int
    entities: teo.Entities
    extended_entities: List[teeo.ExtendedEntities]
    favorited: bool
    retweeted: bool
    possibly_sensitive: bool
    filter_level: str
    lang: str    
    timestamp_ms: datetime
    
@dataclass
class QuotedStatusPermalink():
    url: str
    expanded: str
    display: str