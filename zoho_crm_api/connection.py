from django.conf import settings
from .django_models import AuthToken
from .exceptions import ZohoCRMAPIInitializationException
import os
import zcrmsdk

try:
    config = {
        "apiBaseUrl":"https://www.zohoapis.com",
        "apiVersion":"v2",
        "currentUserEmail":"oleg.yacht.travel@gmail.com",
        "sandbox":"False",
        "applicationLogFilePath":getattr(settings,"ZOHO_CRM_API_LOGFILE",""),
        "client_id":getattr(settings,"ZOHO_CRM_API_CLIENT_ID"),
        "client_secret":getattr(settings,"ZOHO_CRM_API_CLIENT_SECRET"),
        "redirect_uri":getattr(settings,"ZOHO_CRM_API_REDIRECT_URI"),
        "accounts_url":"https://accounts.zoho.com",
        "access_type":"online",
        'persistence_handler_class' : 'ZohoCrmPersistence',
        'persistence_handler_path': os.path.join(os.getcwd(), 'persistance.py')
    }
except AttributeError as ex:
    raise ZohoCRMAPIInitializationException(1,f"Cannot find {ex.args[0]} value")

# if auth tokens didn't haven't been generated yet
if not AuthToken.objects.all():
    from zcrmsdk.RestClient import ZCRMRestClient

    ZCRMRestClient.initialize()
    oauth_client = ZohoOAuth.get_client_instance()
    grant_token=input("Please, paster grant token: ")
    oauth_tokens = oauth_client.generate_access_token(grant_token)

zcrmsdk.ZCRMRestClient.initialize(config)