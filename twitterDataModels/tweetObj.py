from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any
from twitterDataModels import userObj as tuo
from twitterDataModels import entitiesObj as teo
from twitterDataModels import extendedEntitiesObj as teeo
from twitterDataModels import quotedStatusObj as qso
from twitterDataModels import geoObj as geobj
import datetime

@dataclass
class ExtendedTweet:
    full_text: str
    display_text_range: list
    entities: teo.Entities

@dataclass
class ReTweet:
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
    quoted_status_id: int
    quoted_status_id_str: str
    quoted_status: qso.QuotedStatus
    quoted_status_permalink: qso.QuotedStatusPermalink
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
    
    
@dataclass
class Tweet(ReTweet):
    retweeted_status: ReTweet
    timestamp_ms: datetime
    