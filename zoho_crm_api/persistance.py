from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from zoho_crm_api.django_models import AuthToken
from zcrmsdk.OAuthClient import AbstractZohoOAuthPersistence
from zcrmsdk.OAuthClient import ZohoOAuthTokens


class ZohoCrmPersistence(AbstractZohoOAuthPersistence):
    '''
    https://www.zoho.com/crm/developer/docs/python-sdk/config.html
    '''
    def get_oauthtokens(self,user_email):
        try:
            auth_token = AuthToken.objects.get(pk=user_email)
            return ZohoOAuthTokens(auth_token.refreshtoken,auth_token.accesstoken,
                                    auth_token.expirytime,auth_token.useridentifier)
        except AuthToken.DoesNotExist:
            raise Exception(f'No rows found for {user_email} user')

    def save_oauthtokens(self,oauthtokens):
        self.delete_oauthtokens(oauthtokens.userEmail)
        auth_token = AuthToken(useridentifier=oauthtokens.userEmail,
                                accesstoken=oauthtokens.accessToken,
                                refreshtoken=oauthtokens.refreshToken,
                                expirytime=oauthtokens.expiryTime)
        auth_token.save()
        
    def delete_oauthtokens(self,user_email):
        AuthToken.objects.filter(pk=user_email).delete()