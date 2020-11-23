# zoho-crm-api-django


https://github.com/zoho/zcrm-python-sdk


## API Console

```
https://api-console.zoho.com/
```

## INSTALLATION

```
pip install git+https://github.com/DeveloYachtTravel/zoho-crm-api-django.git
```

## Config example

```python
ZOHO_CRM_CONFIG = {
    "apiBaseUrl":"https://www.zohoapis.com",
    "apiVersion":"v2",
    "currentUserEmail":"oleg.yacht.travel@gmail.com",
    "sandbox":"False",
    "applicationLogFilePath":"",
    "client_id":"",
    "client_secret":"",
    "redirect_uri":"",
    "accounts_url":"https://accounts.zoho.com",
    "access_type":"online",
    
    'persistence_handler_class' : 'Custom',
    'persistence_handler_path': '/Users/Zoho/Desktop/PythonSDK/CustomPersistance.py'
}

# Mandatory
ZOHO_CRM_API_CLIENT_ID = ""
ZOHO_CRM_API_CLIENT_SECRET = ""
ZOHO_CRM_API_REDIRECT_URI = ""

# Optional
ZOHO_CRM_API_LOGFILE = ""
```