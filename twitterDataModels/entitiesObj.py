from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any
import datetime, json
from twitterDataModels import mediaObj as tmo

@dataclass
class Hashtags:
    text: str
    indices: list

@dataclass
class Unwound:
    url: str
    status: int
    title: str
    description: str

@dataclass
class UrlFomat:
    url: str
    expanded_url: str
    display_url: str
    unwound: Unwound
    indices: list

@dataclass
class UserMentions:
    screen_name: str
    name: str
    id: int
    id_str: str
    indices: list

@dataclass
class Entities():
    hashtags: list
    urls: List[UrlFomat]
    user_mentions: list
    symbols: list
    media: List[tmo.Media]
    
    def __post_init__(self):
        #Hashtags Section
        hashtaglist = list()
        for hashtag in self.hashtags:
            hashtagobj = Hashtags(hashtag['text'], hashtag['indices'])
            hashtaglist.append(hashtagobj)
        self.hashtags = hashtaglist
        
        #Urls Section
        urlformatlist = list()
        for url in self.urls:
            urlformat = UrlFomat(url['url'], url['expanded_url'], url['display_url'], url['unwound'], url['indices'])
            urlformatlist.append(urlformat)
        self.urls = urlformatlist
        
        #UrlsMentions
        if self.user_mentions is not None:
            usermentionslist = list()
            for um in self.user_mentions:
                usermention = UserMentions(um['screen_name'], um['name'], um['id'], um['id_str'], um['indices'])
                usermentionslist.append(usermention)
            self.user_mentions = usermentionslist
        else:
            self.user_mentions = None   
            
        #Media Object section
        if self.media is not None:
            medialist = list()
            for m in self.media:
    
                thumbImageSize = tmo.ImageSize(m['sizes']['thumb']['w'], 
                                            m['sizes']['thumb']['h'],
                                            m['sizes']['thumb']['resize']) 
                largeImageSize = tmo.ImageSize(m['sizes']['large']['w'], 
                                            m['sizes']['large']['h'], 
                                            m['sizes']['large']['resize'])
                smallImageSize = tmo.ImageSize(m['sizes']['small']['w'], 
                                            m['sizes']['small']['h'], 
                                            m['sizes']['small']['resize'])
                mediumImageSize = tmo.ImageSize(m['sizes']['medium']['w'], 
                                                m['sizes']['medium']['h'], 
                                                m['sizes']['medium']['resize'])
                    
                monetizable = tmo.Monetizable(m['additional_media_info']['monetizable']) 
                imagetypesize = tmo.ImageTypeSize(thumbImageSize, largeImageSize, smallImageSize, mediumImageSize)
            
                    
                media_entities = tmo.Media(m['id'], 
                                        m['id_str'], 
                                        m['indices'], 
                                        monetizable, 
                                        m['media_url'],
                                        m['media_url_https'], 
                                        m['url'], 
                                        m['display_url'], 
                                        m['expanded_url'],
                                        m['type'], 
                                        imagetypesize, 
                                        m['source_status_id'], 
                                        m['source_status_id_str'],
                                        m['source_user_id'], 
                                        m['source_user_id_str']
                                        )
                medialist.append(media_entities)
            self.media = medialist
        else:
            self.media = None
        
   
       
        
        



