from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Any
import datetime, json
from utilities import deleteAttributes as da
from utilities import twitterObjectsCreation as toc

#Sample Tweets
#twitter_json = r'''{"created_at":"Fri Sep 06 00:23:23 +0000 2019","id":1169768019532374016,"id_str":"1169768019532374016","text":"RT @KelemenCari: \ud83d\ude02 These hecklers sound like a Monty Python movie!\nhttps:\/\/t.co\/BVkkm45ujt","source":"\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Web App\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":143483210,"id_str":"143483210","name":"Nolchick","screen_name":"nolchickrobin","location":"Florida, USA","url":"http:\/\/Gab.ai\/nolchickrobin","description":"God Family Country ARRT Traveler Animal Lover Trump Supporter FSU Football Fan #GoNoles","translator_type":"none","protected":false,"verified":false,"followers_count":4562,"friends_count":5010,"listed_count":59,"favourites_count":82684,"statuses_count":41638,"created_at":"Thu May 13 15:54:44 +0000 2010","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"ACDED6","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme18\/bg.gif","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme18\/bg.gif","profile_background_tile":false,"profile_link_color":"038543","profile_sidebar_border_color":"EEEEEE","profile_sidebar_fill_color":"F6F6F6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/897239685709389824\/YlfJBXn7_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/897239685709389824\/YlfJBXn7_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/143483210\/1498860952","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Thu Sep 05 20:57:00 +0000 2019","id":1169716080660627457,"id_str":"1169716080660627457","text":"\ud83d\ude02 These hecklers sound like a Monty Python movie!\nhttps:\/\/t.co\/BVkkm45ujt","source":"\u003ca href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\"\u003eTwitter Web App\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":736989573201301504,"id_str":"736989573201301504","name":"Cari Kelemen","screen_name":"KelemenCari","location":"Texas","url":"https:\/\/www.youtube.com\/c\/CariKelemen","description":"If the world stands against me, then I stand against the world.\n- Athanasius of Alexandria","translator_type":"none","protected":false,"verified":false,"followers_count":31911,"friends_count":10103,"listed_count":89,"favourites_count":44370,"statuses_count":29274,"created_at":"Sun May 29 18:36:21 +0000 2016","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"ABB8C2","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1078317308068556800\/E0Cutwhd_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1078317308068556800\/E0Cutwhd_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/736989573201301504\/1503869699","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"quote_count":6,"reply_count":27,"retweet_count":62,"favorite_count":110,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[],"entities_media":[{"id":1169619857840779264,"id_str":"1169619857840779264","indices":[50,73],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","url":"https:\/\/t.co\/BVkkm45ujt","display_url":"pic.twitter.com\/BVkkm45ujt","expanded_url":"https:\/\/twitter.com\/RaheemKassam\/status\/1169620072299675648\/video\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":632,"h":654,"resize":"fit"},"small":{"w":632,"h":654,"resize":"fit"},"medium":{"w":632,"h":654,"resize":"fit"}},"source_status_id":1169620072299675648,"source_status_id_str":"1169620072299675648","source_user_id":125128723,"source_user_id_str":"125128723"}]},"extended_entities":{"entities_media":[{"id":1169619857840779264,"id_str":"1169619857840779264","indices":[50,73],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","url":"https:\/\/t.co\/BVkkm45ujt","display_url":"pic.twitter.com\/BVkkm45ujt","expanded_url":"https:\/\/twitter.com\/RaheemKassam\/status\/1169620072299675648\/video\/1","type":"video","video_info":{"aspect_ratio":[316,327],"duration_millis":57855,"variants":[{"bitrate":2176000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/632x654\/3s4lmQ-9oNM3J37w.mp4?tag=10"},{"bitrate":832000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/360x372\/cNpa6UCBcCkCROPE.mp4?tag=10"},{"content_type":"application\/x-mpegURL","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/pl\/TAdf_8GXY3L07DMv.m3u8?tag=10"},{"bitrate":632000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/320x330\/HgK1DjHE6SdNvF3B.mp4?tag=10"}]},"sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":632,"h":654,"resize":"fit"},"small":{"w":632,"h":654,"resize":"fit"},"medium":{"w":632,"h":654,"resize":"fit"}},"source_status_id":1169620072299675648,"source_status_id_str":"1169620072299675648","source_user_id":125128723,"source_user_id_str":"125128723"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"KelemenCari","name":"Cari Kelemen","id":736989573201301504,"id_str":"736989573201301504","indices":[3,15]}],"symbols":[],"entities_media":[{"id":1169619857840779264,"id_str":"1169619857840779264","indices":[67,90],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","url":"https:\/\/t.co\/BVkkm45ujt","display_url":"pic.twitter.com\/BVkkm45ujt","expanded_url":"https:\/\/twitter.com\/RaheemKassam\/status\/1169620072299675648\/video\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":632,"h":654,"resize":"fit"},"small":{"w":632,"h":654,"resize":"fit"},"medium":{"w":632,"h":654,"resize":"fit"}},"source_status_id":1169620072299675648,"source_status_id_str":"1169620072299675648","source_user_id":125128723,"source_user_id_str":"125128723"}]},"extended_entities":{"entities_media":[{"id":1169619857840779264,"id_str":"1169619857840779264","indices":[67,90],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1169619857840779264\/pu\/img\/9ZUj6s6nDgtCMPn9.jpg","url":"https:\/\/t.co\/BVkkm45ujt","display_url":"pic.twitter.com\/BVkkm45ujt","expanded_url":"https:\/\/twitter.com\/RaheemKassam\/status\/1169620072299675648\/video\/1","type":"video","video_info":{"aspect_ratio":[316,327],"duration_millis":57855,"variants":[{"bitrate":2176000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/632x654\/3s4lmQ-9oNM3J37w.mp4?tag=10"},{"bitrate":832000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/360x372\/cNpa6UCBcCkCROPE.mp4?tag=10"},{"content_type":"application\/x-mpegURL","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/pl\/TAdf_8GXY3L07DMv.m3u8?tag=10"},{"bitrate":632000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1169619857840779264\/pu\/vid\/320x330\/HgK1DjHE6SdNvF3B.mp4?tag=10"}]},"sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":632,"h":654,"resize":"fit"},"small":{"w":632,"h":654,"resize":"fit"},"medium":{"w":632,"h":654,"resize":"fit"}},"source_status_id":1169620072299675648,"source_status_id_str":"1169620072299675648","source_user_id":125128723,"source_user_id_str":"125128723"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"en","timestamp_ms":"1567729403752"}'''
# #twitter_json = r'''{"created_at":"Thu Nov 28 18:37:24 +0000 2019","id":1200121531411644416,"id_str":"1200121531411644416","text":"2\/3\n\n\"#Trump himself, in describing the conversation, has referred only to the #ambassador\u2019s account of the call, w\u2026 https:\/\/t.co\/qEDq5Fq1Mw","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":1200121530061074434,"in_reply_to_status_id_str":"1200121530061074434","in_reply_to_user_id":16273556,"in_reply_to_user_id_str":"16273556","in_reply_to_screen_name":"MarionThorpe","user":{"id":16273556,"id_str":"16273556","name":"Dr. Marion Thorpe","screen_name":"MarionThorpe","location":"Florida","url":"https:\/\/www.facebook.com\/HealAmerica","description":"State of Florida Chief Medical Officer (former). MEDICAL DOCTOR with a passion for the US Constitution and American Dream. United We Stand: Let's Heal America!","translator_type":"none","protected":false,"verified":false,"followers_count":1623,"friends_count":1602,"listed_count":105,"favourites_count":3913,"statuses_count":24139,"created_at":"Sat Sep 13 17:10:00 +0000 2008","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"FFFFFF","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"A3A4D1","profile_sidebar_border_color":"87BC44","profile_sidebar_fill_color":"050029","profile_text_color":"F70511","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/664226293630803968\/LO4crJ73_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/664226293630803968\/LO4crJ73_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/16273556\/1454149736","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"2\/3\n\n\"#Trump himself, in describing the conversation, has referred only to the #ambassador\u2019s account of the call, which \u2014 based on #Sondland\u2019s activities \u2014 would have occurred before dawn in #Washington. \n\nAnd the #WhiteHouse has not located a record in its switchboard logs of a","display_text_range":[0,279],"entities":{"hashtags":[{"text":"Trump","indices":[6,12]},{"text":"ambassador","indices":[79,90]},{"text":"Sondland","indices":[131,140]},{"text":"Washington","indices":[191,202]},{"text":"WhiteHouse","indices":[214,225]}],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"Trump","indices":[6,12]},{"text":"ambassador","indices":[79,90]}],"urls":[{"url":"https:\/\/t.co\/qEDq5Fq1Mw","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1200121531411644416","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1574966244925"}'''
#twitter_json = r'''{"created_at":"Mon Dec 09 03:51:29 +0000 2019","id":1203884849590726656,"id_str":"1203884849590726656","text":"RT @Education4Libs: Dear libs,\n\nCan any of you please explain to me why 49 year old crackhead Hunter Biden is off limits, but 13 year old B\u2026","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":958809380798980096,"id_str":"958809380798980096","name":"Lex","screen_name":"lextran77","location":null,"url":null,"description":null,"translator_type":"none","protected":false,"verified":false,"followers_count":30,"friends_count":168,"listed_count":0,"favourites_count":13475,"statuses_count":1052,"created_at":"Wed Jan 31 21:09:04 +0000 2018","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1185000854505558018\/1QRRtEED_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1185000854505558018\/1QRRtEED_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/958809380798980096\/1571361379","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Sun Dec 08 19:17:25 +0000 2019","id":1203755480293748737,"id_str":"1203755480293748737","text":"Dear libs,\n\nCan any of you please explain to me why 49 year old crackhead Hunter Biden is off limits, but 13 year o\u2026 https:\/\/t.co\/RD1mGPc8JI","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":true,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":817661098988019712,"id_str":"817661098988019712","name":"Educating Liberals","screen_name":"Education4Libs","location":"Minnesota, USA","url":"http:\/\/educatingliberals.com","description":"Digital soldier. Shadowbanned by Twitter. #WWG1WGA \ud83c\uddfa\ud83c\uddf8 KAG products \ud83d\udc47\ud83c\udffb","translator_type":"none","protected":false,"verified":false,"followers_count":444252,"friends_count":283960,"listed_count":2042,"favourites_count":124119,"statuses_count":9003,"created_at":"Sat Jan 07 09:16:12 +0000 2017","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"F5F8FA","profile_background_image_url":"","profile_background_image_url_https":"","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1127981592696115202\/WBcMbFd-_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1127981592696115202\/WBcMbFd-_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/817661098988019712\/1563879746","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"is_quote_status":false,"extended_tweet":{"full_text":"Dear libs,\n\nCan any of you please explain to me why 49 year old crackhead Hunter Biden is off limits, but 13 year old Barron Trump is free game?\n\nSeriously, I\u2019ll wait.","display_text_range":[0,167],"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]}},"quote_count":127,"reply_count":366,"retweet_count":5319,"favorite_count":15400,"entities":{"hashtags":[],"urls":[{"url":"https:\/\/t.co\/RD1mGPc8JI","expanded_url":"https:\/\/twitter.com\/i\/web\/status\/1203755480293748737","display_url":"twitter.com\/i\/web\/status\/1\u2026","indices":[117,140]}],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en"},"is_quote_status":false,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[{"screen_name":"Education4Libs","name":"Educating Liberals","id":817661098988019712,"id_str":"817661098988019712","indices":[3,18]}],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"en","timestamp_ms":"1575863489898"}'''
#twitter_json = r'''{"created_at":"Sun May 31 15:59:52 +0000 2020","id":1267123640631468035,"id_str":"1267123640631468035","text":"\ud83d\ude05","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2837729223,"id_str":"2837729223","name":"Ferit G\u00fcle\u00e7","screen_name":"VictorOmened","location":null,"url":null,"description":"I draw editorial illustrations, comics for various magazines and draw storyboard for advertising agencies.","translator_type":"none","protected":false,"verified":false,"followers_count":139,"friends_count":580,"listed_count":0,"favourites_count":4020,"statuses_count":600,"created_at":"Mon Oct 20 00:39:35 +0000 2014","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"1DA1F2","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1187682525793136640\/sxCXQMH__normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1187682525793136640\/sxCXQMH__normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2837729223\/1572000556","default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":{"id":"5e02a0f0d91c76d2","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/5e02a0f0d91c76d2.json","place_type":"city","name":"\u0130stanbul","full_name":"\u0130stanbul, T\u00fcrkiye","country_code":"TR","country":"T\u00fcrkiye","bounding_box":{"type":"Polygon","coordinates":[[[28.632104,40.802734],[28.632104,41.239907],[29.378341,41.239907],[29.378341,40.802734]]]},"attributes":{}},"contributors":null,"quoted_status_id":1266683107329146880,"quoted_status_id_str":"1266683107329146880","quoted_status":{"created_at":"Sat May 30 10:49:21 +0000 2020","id":1266683107329146880,"id_str":"1266683107329146880","text":"Monty Python\u2019un en iyi b\u00f6l\u00fcmlerinden birinin kalitesinde ve tamamen ger\u00e7ek :\u2019) https:\/\/t.co\/PaQkVNnutH","source":"\u003ca href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\"\u003eTwitter for iPhone\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":113207648,"id_str":"113207648","name":"Ethem Onur Bilgi\u00e7","screen_name":"ethemonur","location":"istanbul","url":"http:\/\/www.ethemonur.com","description":"illustrator | graphic designer","translator_type":"none","protected":false,"verified":false,"followers_count":19481,"friends_count":1058,"listed_count":68,"favourites_count":56081,"statuses_count":14510,"created_at":"Thu Feb 11 01:59:03 +0000 2010","utc_offset":null,"time_zone":null,"geo_enabled":true,"lang":null,"contributors_enabled":false,"is_translator":false,"profile_background_color":"2E2E2E","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":true,"profile_link_color":"19CF86","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"ACBBBF","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/1085126823980253184\/4UrZigWb_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/1085126823980253184\/4UrZigWb_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/113207648\/1542701744","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":{"id":"5e02a0f0d91c76d2","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/5e02a0f0d91c76d2.json","place_type":"city","name":"\u0130stanbul","full_name":"\u0130stanbul, T\u00fcrkiye","country_code":"TR","country":"T\u00fcrkiye","bounding_box":{"type":"Polygon","coordinates":[[[28.632104,40.802734],[28.632104,41.239907],[29.378341,41.239907],[29.378341,40.802734]]]},"attributes":{}},"contributors":null,"is_quote_status":false,"quote_count":39,"reply_count":21,"retweet_count":146,"favorite_count":1666,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[],"media":[{"id":1266476675015020545,"id_str":"1266476675015020545","indices":[79,102],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1266476675015020545\/pu\/img\/YHJhsRYnprP6pcwa.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1266476675015020545\/pu\/img\/YHJhsRYnprP6pcwa.jpg","url":"https:\/\/t.co\/PaQkVNnutH","display_url":"pic.twitter.com\/PaQkVNnutH","expanded_url":"https:\/\/twitter.com\/LeventUzumcu\/status\/1266476757709881344\/video\/1","type":"photo","sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":480,"h":848,"resize":"fit"},"small":{"w":385,"h":680,"resize":"fit"},"medium":{"w":480,"h":848,"resize":"fit"}},"source_status_id":1266476757709881344,"source_status_id_str":"1266476757709881344","source_user_id":99564663,"source_user_id_str":"99564663"}]},"extended_entities":{"media":[{"id":1266476675015020545,"id_str":"1266476675015020545","indices":[79,102],"additional_media_info":{"monetizable":false},"media_url":"http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1266476675015020545\/pu\/img\/YHJhsRYnprP6pcwa.jpg","media_url_https":"https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1266476675015020545\/pu\/img\/YHJhsRYnprP6pcwa.jpg","url":"https:\/\/t.co\/PaQkVNnutH","display_url":"pic.twitter.com\/PaQkVNnutH","expanded_url":"https:\/\/twitter.com\/LeventUzumcu\/status\/1266476757709881344\/video\/1","type":"video","video_info":{"aspect_ratio":[30,53],"duration_millis":37330,"variants":[{"bitrate":632000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1266476675015020545\/pu\/vid\/320x564\/ly8ltT-dwyMeZKgV.mp4?tag=10"},{"content_type":"application\/x-mpegURL","url":"https:\/\/video.twimg.com\/ext_tw_video\/1266476675015020545\/pu\/pl\/FFKQivtvgtdhWyRh.m3u8?tag=10"},{"bitrate":832000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1266476675015020545\/pu\/vid\/360x636\/sN_Fw1Ye0Bi-xDYn.mp4?tag=10"},{"bitrate":2176000,"content_type":"video\/mp4","url":"https:\/\/video.twimg.com\/ext_tw_video\/1266476675015020545\/pu\/vid\/480x848\/3cXzgdIpNc8RAMw1.mp4?tag=10"}]},"sizes":{"thumb":{"w":150,"h":150,"resize":"crop"},"large":{"w":480,"h":848,"resize":"fit"},"small":{"w":385,"h":680,"resize":"fit"},"medium":{"w":480,"h":848,"resize":"fit"}},"source_status_id":1266476757709881344,"source_status_id_str":"1266476757709881344","source_user_id":99564663,"source_user_id_str":"99564663"}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"low","lang":"tr"},"quoted_status_permalink":{"url":"https:\/\/t.co\/IaGrUw3YKX","expanded":"https:\/\/twitter.com\/ethemonur\/status\/1266683107329146880","display":"twitter.com\/ethemonur\/stat\u2026"},"is_quote_status":true,"quote_count":0,"reply_count":0,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"urls":[],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"und","timestamp_ms":"1590940792602"}'''

@dataclass
class TwitterFeed:
    tweet_string: str
    
    def __post_init__(self):
        twitter_data = json.loads(self.tweet_string)        
        tweet = Any       
        #Tweet Object Creation
        if twitter_data is not None:
            tdkwargs = {k:v for k,v in twitter_data.items()} 
            tweet = toc.create_tweet_obj(**tdkwargs)
        else:
            tweet = None
        return tweet

if __name__ == '__main__':

    twitter_feed = TwitterFeed(twitter_json)
    print(twitter_feed)
    

    
    