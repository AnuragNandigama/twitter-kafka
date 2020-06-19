from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any
from twitterDataModels import mediaObj as tmo

@dataclass
class Variants:
    bitrate: float
    content_type: str = field(default = None)
    url: str = field(default = None)

@dataclass
class VideoInfo:
    aspect_ratio: list 
    duration_millis: int
    variants: List[Variants]
    
@dataclass
class ExtendedEntitiesMedia(tmo.Media): 
    video_info: VideoInfo
    
@dataclass
class ExtendedEntities:
    media: List[ExtendedEntitiesMedia]
    
    def create_extended_entity(self, extended_entities_media):
        #Extended Entities section
        extendedmedialist = list()
        
        for ex_media in extended_entities_media:
            #Variants section
            variantlist = list()
            variants_media = ex_media['video_info']['variants']
            for variant in variants_media:
                if 'bitrate' in variant:
                    variant = Variants(variant['bitrate'], variant['content_type'], variant['url'])
                else:
                    variant = Variants(content_type=variant['content_type'], url=variant['url'])
                variantlist.append(variant)
            
            videoinfo = VideoInfo(ex_media['video_info']['aspect_ratio'], ex_media['video_info']['duration_millis'], variantlist)
            
            thumbImageSize = tmo.ImageSize(ex_media['sizes']['thumb']['w'], 
                                           ex_media['sizes']['thumb']['h'], 
                                           ex_media['sizes']['thumb']['resize']) 
            largeImageSize = tmo.ImageSize(ex_media['sizes']['large']['w'], 
                                           ex_media['sizes']['large']['h'], 
                                           ex_media['sizes']['large']['resize'])
            smallImageSize = tmo.ImageSize(ex_media['sizes']['small']['w'], 
                                           ex_media['sizes']['small']['h'], 
                                           ex_media['sizes']['small']['resize'])
            mediumImageSize = tmo.ImageSize(ex_media['sizes']['medium']['w'],
                                            ex_media['sizes']['medium']['h'], 
                                            ex_media['sizes']['medium']['resize'])
                
            monetizable = tmo.Monetizable(ex_media['additional_media_info']['monetizable']) 
            imagetypesize = tmo.ImageTypeSize(thumbImageSize, largeImageSize, smallImageSize, mediumImageSize)
                
            media_entities = ExtendedEntitiesMedia(ex_media['id'], 
                                                   ex_media['id_str'], 
                                                   ex_media['indices'], 
                                                   monetizable, 
                                                   ex_media['media_url'], 
                                                   ex_media['media_url_https'], 
                                                   ex_media['url'], 
                                                   ex_media['display_url'], 
                                                   ex_media['expanded_url'],
                                                   ex_media['type'], 
                                                   imagetypesize, 
                                                   ex_media['source_status_id'], 
                                                   ex_media['source_status_id_str'], 
                                                   ex_media['source_user_id'], 
                                                   ex_media['source_user_id_str'], 
                                                   videoinfo
                                                )
            extendedmedialist.append(media_entities)
        
        self.media = extendedmedialist
    