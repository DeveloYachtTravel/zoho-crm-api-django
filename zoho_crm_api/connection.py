from django.conf import settings
from .exceptions import ZohoCRMAPIInitializationException
import os
import zcrmsdk

try:
    config = {
        "apiBaseUrl":"https://www.zohoapis.com",
        "apiVersion":"v2",
        "currentUserEmail":"oleg.yacht.travel@gmail.com",
        "sandbox":"False",
        "applicationLogFilePath":settings.get("ZOHO_CRM_API_LOGFILE",""),
        "client_id":settings["ZOHO_CRM_API_CLIENT_ID"],
        "client_secret":settings["ZOHO_CRM_API_CLIENT_SECRET"],
        "redirect_uri":settings["ZOHO_CRM_API_REDIRECT_URI"],
        "accounts_url":"https://accounts.zoho.com",
        "access_type":"online",
        'persistence_handler_class' : 'ZohoCrmPersistence',
        'persistence_handler_path': os.path.join(os.getcwd(), 'persistance.py')
    }
except KeyError as ex:
    raise ZohoCRMAPIInitializationException(1,f"Cannot find {ex.args[0]} value")

zcrmsdk.ZCRMRestClient.initialize(config)