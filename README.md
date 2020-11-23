# zoho-crm-api-django


https://github.com/zoho/zcrm-python-sdk


## API Console

```
https://api-console.zoho.com/
```

### Installation

```
pip install git+https://github.com/DeveloYachtTravel/zoho-crm-api-django.git
```

### Config example

```python
# Mandatory
ZOHO_CRM_API_CLIENT_ID = ""
ZOHO_CRM_API_CLIENT_SECRET = ""
ZOHO_CRM_API_REDIRECT_URI = ""

# Optional
ZOHO_CRM_API_LOGFILE = ""
```

### First key generating

```python
ZCRMRestClient.initialize()
oauth_client = ZohoOAuth.get_client_instance()
grant_token="paste_grant_token_here"
oauth_tokens = oauth_client.generate_access_token(grant_token)
```