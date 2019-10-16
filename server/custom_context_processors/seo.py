from decouple import config
from django.conf import settings

def seo(request):

    if not settings.DEBUG:
        google_analytics_id = config('GOOGLE_ANALYTICS_ID')
        facebook_analytics_init = config('FACEBOOK_ANALYTICS_INIT')
        facebook_analytics_track = config('FACEBOOK_ANALYTICS_TRACK')
        context = {
            "analytics":{
                "GOOGLE":{
                    "id": google_analytics_id,
                },
                "FACEBOOK":{
                    "init": facebook_analytics_init,
                    "track": facebook_analytics_track
                }
            }
        }

    else:
        context = {}
    
    return context