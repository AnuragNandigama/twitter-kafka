from twitterDataModels import tweetObj as tto
from twitterDataModels import extendedEntitiesObj as teeo
from twitterDataModels import entitiesObj as teo
from twitterDataModels import userObj as tuo
from twitterDataModels import quotedStatusObj as qso
from twitterDataModels import geoObj as geobj
from utilities import deleteAttributes as da
from typing import List, Dict, Tuple, Any

# User Obj creation function
def create_user_obj(id=None,
                    id_str=None,
                    name=None,
                    screen_name=None,
                    location=None,
                    url=None,
                    description=None,
                    translator_type=None,
                    protected=None,
                    verified=None,
                    followers_count=None,
                    friends_count=None,
                    listed_count=None,
                    favourites_count=None,
                    statuses_count=None,
                    created_at=None,
                    utc_offset=None,
                    time_zone=None,
                    geo_enabled=None,
                    lang=None,
                    contributors_enabled=None,
                    is_translator=None,
                    profile_background_color=None,
                    profile_background_image_url=None,
                    profile_background_image_url_https=None,
                    profile_background_tile=None,
                    profile_link_color=None,
                    profile_sidebar_border_color=None,
                    profile_sidebar_fill_color=None,
                    profile_text_color=None,
                    profile_use_background_image=None,
                    profile_image_url=None,
                    profile_image_url_https=None,
                    profile_banner_url=None,
                    default_profile=None,
                    default_profile_image=None,
                    following=None,
                    follow_request_sent=None,
                    notifications=None):

    user = tuo.User(id,
                    id_str,
                    name,
                    screen_name,
                    location,
                    url,
                    description,
                    translator_type,
                    protected,
                    verified,
                    followers_count,
                    friends_count,
                    listed_count,
                    favourites_count,
                    statuses_count,
                    created_at,
                    utc_offset,
                    time_zone,
                    geo_enabled,
                    lang,
                    contributors_enabled,
                    is_translator,
                    profile_background_color,
                    profile_background_image_url,
                    profile_background_image_url_https,
                    profile_background_tile,
                    profile_link_color,
                    profile_sidebar_border_color,
                    profile_sidebar_fill_color,
                    profile_text_color,
                    profile_use_background_image,
                    profile_image_url,
                    profile_image_url_https,
                    profile_banner_url,
                    default_profile,
                    default_profile_image,
                    following,
                    follow_request_sent,
                    notifications)

    #user = da.delete_attribute(user)
    return user

#Geo Obj creation function
def create_geo_obj(type=None, coordinates=None):
    geo = geobj.Coordinates(type, coordinates)
    return geo

#Coordinates Obj creation function
def create_coordinates_obj(type=None, coordinates=None):
    coordinates = geobj.Coordinates(type, coordinates)
    return coordinates

#Place Obj creation function
def create_place_obj(id=None,url=None,place=None,name=None,full_name=None,country_code=None,country=None,bounding_box=None,attributes=None):
    place = geobj.Place(id, url, place, name, full_name, country_code, country, bounding_box, attributes)
    return place

# Entities Object creation function
def create_entities_obj(hashtags=None, urls=None, user_mentions=None, symbols=None, media=None):
    entity = teo.Entities(hashtags, urls, user_mentions, symbols, media)
    #entity = da.delete_attribute(entity)
    return entity

# Extended Entities Object creation function
def create_extended_entities_obj(media=None):
    extended_entity = teeo.ExtendedEntities(media)
    #extended_entity = da.delete_attribute(extended_entity)
    return extended_entity
  
#Check User and Create Object Function
def check_user_create_obj(user):
    tweet_user = Any
    if user is not None:
        ukwargs = {k:v for k, v in user.items()}
        tweet_user = create_user_obj(**ukwargs)
    else:
        tweet_user = None
    return tweet_user

#Check Geo and Create Object Function
def check_geo_create_obj(geo):
    tweet_geo = Any
    if geo is not None:
        gkwargs = {k:v for k,v in geo.items()}
        tweet_geo = create_geo_obj(**gkwargs)
    else:
        tweet_geo = None
    return tweet_geo

#Check Coordinates and create obj
def check_coordinates_obj(coordinates):
    tweet_coordinates = Any
    if coordinates is not None:
        ckwargs = {k:v for k,v in coordinates.items()}
        tweet_coordinates = create_coordinates_obj(ckwargs)
    else:
        tweet_coordinates = None
    return tweet_coordinates

#Check Place and create obj
def check_place_obj(place):
    tweet_place = Any
    if place is not None:
        pkwargs = {k:v for k,v in place.items()}
        tweet_place = create_place_obj(pkwargs)
    else:
        tweet_place = None
    return tweet_place

# Extended Tweet Object creation function
def create_extended_tweet_obj(full_text=None, display_text_range=None, entities=None):
    extended_tweet_entity = Any
    if entities is not None:
        etekwargs = {k:v for k, v in entities.items()}
        extended_tweet_entity = create_entities_obj(**etekwargs)
    else:
        extended_tweet_entity = None
    extended_tweet = tto.ExtendedTweet(full_text, display_text_range, extended_tweet_entity)
    #extended_tweet = da.delete_attribute(extended_tweet)
    return extended_tweet

#Check Extended Tweet and create Object function
def check_extended_tweet_create_obj(extended_tweet):
    tweet_extended_tweet = Any
    if extended_tweet is not None:
        etkwargs = {k:v for k, v in extended_tweet.items()}
        tweet_extended_tweet = create_extended_tweet_obj(**etkwargs)
    else:
        tweet_extended_tweet = None
    return tweet_extended_tweet

#Check Entities and create obj
def check_entities_create_obj(entities):
    tweet_entities = Any
    if entities is not None:
        ekwargs = {k:v for k, v in entities.items()}
        tweet_entities = create_entities_obj(**ekwargs)
    else:
        tweet_entities = None
    return tweet_entities

#Check Extended Entities and create obj
def check_extended_entities_create_obj(extended_entities):
    tweet_extended_entities = Any
    if extended_entities is not None:
        eekwargs = {k:v for k,v in extended_entities.items()}
        tweet_extended_entities = create_extended_entities_obj(**eekwargs)
    else:
        tweet_extended_entities = None
    return tweet_extended_entities

# Retweet Obj Creation function
def create_retweet_obj(created_at=None,
                       id=None,
                       id_str=None,
                       text=None,
                       source=None,
                       truncated=None,
                       in_reply_to_status_id=None,
                       in_reply_to_status_id_str=None,
                       in_reply_to_user_id=None,
                       in_reply_to_user_id_str=None,
                       in_reply_to_screen_name=None,
                       user=None,
                       geo=None,
                       coordinates=None,
                       place=None,
                       contributors=None,
                       quoted_status_id=None,
                       quoted_status_id_str=None,
                       quoted_status=None,
                       quoted_status_permalink=None,
                       is_quote_status=None,
                       extended_tweet=None,
                       quote_count=None,
                       reply_count=None,
                       retweet_count=None,
                       favorite_count=None,
                       entities=None,
                       extended_entities=None,
                       favorited=None,
                       retweeted=None,
                       possibly_sensitive=None,
                       filter_level=None,
                       lang=None
                       ):

    retweet = tto.ReTweet(created_at,
                          id,
                          id_str,
                          text,
                          source,
                          truncated,
                          in_reply_to_status_id,
                          in_reply_to_status_id_str,
                          in_reply_to_user_id,
                          in_reply_to_user_id_str,
                          in_reply_to_screen_name,                          
                          check_user_create_obj(user),
                          geo,
                          coordinates,
                          place,
                          contributors,
                          is_quote_status,
                          check_extended_tweet_create_obj(extended_tweet),
                          quote_count,
                          reply_count,
                          retweet_count,
                          favorite_count,
                          check_entities_create_obj(entities),
                          check_extended_entities_create_obj(extended_entities),
                          favorited,
                          retweeted,
                          possibly_sensitive,
                          filter_level,
                          lang)

    #retweet = da.delete_attribute(retweet)
    return retweet

#Check Retweeted Status and create obj
def check_retweeted_status_create_obj(retweeted_status):
    tweet_retweeted_stauts = Any
    if retweeted_status is not None:
        rskwargs = {k:v for k, v in retweeted_status.items()}
        tweet_retweeted_stauts = create_retweet_obj(**rskwargs)
    else:
        tweet_retweeted_stauts = None
    return tweet_retweeted_stauts

# Quoted Status object creation function
def create_quoted_status_obj(created_at=None,
                       id=None,
                       id_str=None,
                       text=None,
                       source=None,
                       truncated=None,
                       in_reply_to_status_id=None,
                       in_reply_to_status_id_str=None,
                       in_reply_to_user_id=None,
                       in_reply_to_user_id_str=None,
                       in_reply_to_screen_name=None,
                       user=None,
                       geo=None,
                       coordinates=None,
                       place=None,
                       contributors=None,
                       quoted_status_id=None,
                       quoted_status_id_str=None,
                       quoted_status=None,
                       quoted_status_permalink=None,
                       is_quote_status=None,
                       extended_tweet=None,
                       quote_count=None,
                       reply_count=None,
                       retweet_count=None,
                       favorite_count=None,
                       entities=None,
                       extended_entities=None,
                       favorited=None,
                       retweeted=None,
                       possibly_sensitive=None,
                       filter_level=None,
                       lang=None,
                       timestamp_ms=None):
    
    quoted_status = qso.QuotedStatus(
                          created_at,
                          id,
                          id_str,
                          text,
                          source,
                          truncated,
                          in_reply_to_status_id,
                          in_reply_to_status_id_str,
                          in_reply_to_user_id,
                          in_reply_to_user_id_str,
                          in_reply_to_screen_name,                          
                          check_user_create_obj(user),
                          geo,
                          coordinates,
                          place,
                          contributors,                          
                          is_quote_status,
                          check_extended_tweet_create_obj(extended_tweet),
                          quote_count,
                          reply_count,
                          retweet_count,
                          favorite_count,
                          check_entities_create_obj(entities),
                          check_extended_entities_create_obj(extended_entities),
                          favorited,
                          retweeted,
                          possibly_sensitive,
                          filter_level,
                          lang,
                          timestamp_ms
                        )
    
    return quoted_status

#Quoted Status Obj Creation Function        
def check_quoted_status_obj(quoted_status):
    tweet_quoted_status = Any
    if quoted_status is not None:
        qskwargs = {k:v for k, v in quoted_status.items()}
        tweet_quoted_status = create_quoted_status_obj(**qskwargs)
    else:
        tweet_quoted_status = None
    return tweet_quoted_status

# Quoted Status Permalink Obj Creation Function
def create_quoted_status_permalink_obj(url=None, expanded=None, display=None):
    quoted_status_permalink = qso.QuotedStatusPermalink(url, expanded, display)
    return quoted_status_permalink

#Quoted Status Obj Creation Function        
def check_quoted_status_permalink_obj(quoted_status_permalink):
    tweet_quoted_status_permalink = Any
    if quoted_status_permalink is not None:
        qspkwargs = {k:v for k, v in quoted_status_permalink.items()}
        tweet_quoted_status_permalink = create_quoted_status_permalink_obj(**qspkwargs)
    else:
        tweet_quoted_status_permalink = None
    return tweet_quoted_status_permalink
    
# Tweet Object Creation function
def create_tweet_obj(created_at=None,
                     id=None,
                     id_str=None,
                     text=None,
                     source=None,
                     truncated=None,
                     in_reply_to_status_id=None,
                     in_reply_to_status_id_str=None,
                     in_reply_to_user_id=None,
                     in_reply_to_user_id_str=None,
                     in_reply_to_screen_name=None,
                     user=None,
                     geo=None,
                     coordinates=None,
                     place=None,
                     contributors=None,
                     retweeted_status=None,
                     quoted_status_id = None,
                     quoted_status_id_str = None,
                     quoted_status = None,
                     quoted_status_permalink = None,
                     is_quote_status=None,
                     extended_tweet=None,
                     quote_count=None,
                     reply_count=None,
                     retweet_count=None,
                     favorite_count=None,
                     entities=None,
                     extended_entities=None,
                     favorited=None,
                     retweeted=None,
                     possibly_sensitive=None,
                     filter_level=None,
                     lang=None,
                     timestamp_ms=None):    
    
    tweet = tto.Tweet(created_at,
                     id,
                     id_str,
                     text,
                     source,
                     truncated,
                     in_reply_to_status_id,
                     in_reply_to_status_id_str,
                     in_reply_to_user_id,
                     in_reply_to_user_id_str,
                     in_reply_to_screen_name,
                     check_user_create_obj(user),
                     check_geo_create_obj(geo),
                     check_coordinates_obj(coordinates),
                     check_place_obj(place),
                     contributors,
                     quoted_status_id,
                     quoted_status_id_str,
                     check_quoted_status_obj(quoted_status),
                     check_quoted_status_permalink_obj(quoted_status_permalink),
                     is_quote_status,  
                     check_extended_tweet_create_obj(extended_tweet),                   
                     quote_count,
                     reply_count,
                     retweet_count,
                     favorite_count,
                     check_entities_create_obj(entities),
                     check_extended_entities_create_obj(extended_entities),
                     favorited,
                     retweeted,
                     possibly_sensitive,
                     filter_level,
                     lang,
                     check_retweeted_status_create_obj(retweeted_status),                     
                     timestamp_ms)
    return tweet
