# zoho-crm-api-django

### Build on

>https://github.com/zoho/zcrm-python-sdk


## Zoho CRM API Console

>https://api-console.zoho.com/


### Installation

```
pip install git+https://github.com/DeveloYachtTravel/zoho-crm-api-django.git
```

Setting Up
----------


### Django settings

```python
# Mandatory
ZOHO_CRM_API_CLIENT_ID = ""
ZOHO_CRM_API_CLIENT_SECRET = ""
ZOHO_CRM_API_REDIRECT_URI = ""

# Optional
ZOHO_CRM_API_LOGFILE = ""
```

### Migrating 

>python manage.py migrate zoho_crm_api

### First key generating

>python manage.py shell

```python
from zoho_crm_api.api import generate_access_token
generate_access_token()
Please, paste grant token: ****************************
Auth Token created
```