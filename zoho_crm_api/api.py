from .conf import MODULES
from .connection import zcrmsdk

from .exceptions import *

import json

import traceback

from .parsers import Group_parser, Deal_parser, Co_worker_parser, Contact_parser, Lead_parser, Operator_parser

import requests

from zcrmsdk.CLException import ZCRMException
from zcrmsdk.Handler import EntityAPIHandler
from zcrmsdk.Handler import APIHandler, APIRequest
from zcrmsdk.Operations import ZCRMRecord, ZCRMUser
from zcrmsdk.RestClient import ZCRMRestClient, ZCRMOrganization
from zcrmsdk.Utility import CommonUtil, APIConstants


class ZOHO_CRM_API():
    def __init__(self):
        self._MAIN_URL = 'https://www.zohoapis.com/crm/v2/{module_api_name}'
        self.modules_api_names = MODULES

    def _get_module_parser(self,module):
        parsers = {
            "Leads":Lead_parser,
            "Deals":Deal_parser,
            "Groups":Group_parser,
            "Co_workers":Co_worker_parser,
            "Visits":None,
            "Contacts":Contact_parser,
            "Vendors":Operator_parser,
        }
        return parsers.get(module)

    def _create_module_record(self,module,record)->None:
        try:
            instance = ZCRMRecord(self.modules_api_names[module],None)
            entity_api_handler = EntityAPIHandler(instance)
            entity_api_handler.set_record_properties(record.to_json())
            record = entity_api_handler.zcrmrecord
            record.create()
            return record.entity_id
        except ZCRMException as ex:
            raise ZohoCRMAPIException(ex.status_code,ex.message,module)

    def _get_module_record(self,module,record_id)->ZCRMRecord:
        parser = self._get_module_parser(self.modules_api_names[module])
        try:
            return parser().parse(zcrmsdk.ZCRMModule(self.modules_api_names[module])\
                    .get_record(record_id).response_json)
        except ZCRMException as ex:
            raise ZohoCRMAPI_NoRecord_Exception(404,f"Cannot find record in {module} module. Details: {ex.error_message}",module,id)

    def _update_module_record(self,module,record,record_id)->None:
        try:
            instance = ZCRMRecord(self.modules_api_names[module],record_id)
            entity_api_handler = EntityAPIHandler(instance)
            entity_api_handler.set_record_properties(record.to_json())
            record = entity_api_handler.zcrmrecord
            record.update()
        except ZCRMException as ex:
            raise ZohoCRMAPIException(ex.status_code,ex.message,module,id)

    def get_deal(self,id:str):
        return self._get_module_record("Deals",id)

    def create_deal(self,deal):
        return self._create_module_record("Deals",deal)

    def update_deal(self,deal):
        self._update_module_record("Deals",deal,deal.deal_id)

    def get_group(self,id:str):
        return self._get_module_record("Groups",id)

    def create_group(self,group):
        return self._create_module_record("Groups",group)

    def update_group(self,group):
        self._update_module_record("Groups",group,group.group_id)

    def get_co_worker(self,id:str):
        return self._get_module_record("Co-workers",id)

    def create_co_worker(self,co_worker):
        return self._create_module_record("Co-workers",co_worker)

    def update_co_worker(self,co_worker):
        self._update_module_record("Co-workers",co_worker,co_worker.co_worker_id)   

    def get_lead(self,id:str):
        return self._get_module_record("Leads",id)

    def convert_lead(self,lead,potential_record=None,assign_to_user=None,contact=None):
        try:
            lead_instance = ZCRMRecord(self.modules_api_names["Leads"],lead.lead_id)
            entity_api_handler = EntityAPIHandler(lead_instance)
            entity_api_handler.set_record_properties(lead.to_json())
            record = entity_api_handler.zcrmrecord

            return self._convert_record(record, potential_record=potential_record, 
                                    assign_to_user=assign_to_user,contact=contact)
        except ZCRMException as ex:
            raise ZohoCRMAPIException(ex.error_code,ex.error_message,"Leads",error_details=ex.error_details)

    def _convert_record(self,record,potential_record,assign_to_user,contact):
        try:
            handler_ins=APIHandler()
            handler_ins.request_url_path=record.module_api_name+"/"+str(record.entity_id)+"/actions/convert"
            handler_ins.request_method=APIConstants.REQUEST_METHOD_POST
            handler_ins.request_api_key=APIConstants.DATA
            input_json=dict()
            if assign_to_user is not None:
                input_json['assign_to']=assign_to_user.id
            if potential_record is not None:
                input_json['Deals']=potential_record.to_json()
            if contact is not None:
                input_json['Contacts']=contact.contact_id
            if(assign_to_user is not None or potential_record is not None or contact is not None):
                inputJsonArr=list()
                inputJsonArr.append(input_json)
                reqBodyJson=dict()
                reqBodyJson[APIConstants.DATA]=inputJsonArr
                handler_ins.request_body=reqBodyJson
            api_response=APIRequest(handler_ins).get_api_response()
            converted_dict=dict()
            convertedIdsJson=api_response.response_json[APIConstants.DATA][0]
            if APIConstants.CONTACTS in convertedIdsJson and convertedIdsJson[APIConstants.CONTACTS] is not None:
                converted_dict[APIConstants.CONTACTS]=convertedIdsJson[APIConstants.CONTACTS]
            if APIConstants.ACCOUNTS in convertedIdsJson and convertedIdsJson[APIConstants.ACCOUNTS] is not None:
                converted_dict[APIConstants.ACCOUNTS]=convertedIdsJson[APIConstants.ACCOUNTS]
            if APIConstants.DEALS in convertedIdsJson and convertedIdsJson[APIConstants.DEALS] is not None:
                converted_dict[APIConstants.DEALS]=convertedIdsJson[APIConstants.DEALS]
            
            return converted_dict
        except ZCRMException as ex:
            ex.message = 'Error occurred for {url}. Error Code: {code} Response error_content: {error_content}. Error Details::{error_details}'
            raise ex
        except Exception as ex:
            CommonUtil.raise_exception(handler_ins.request_url_path,ex.__str__(),traceback.format_stack())

    def create_lead(self,lead):
        return self._create_module_record("Leads",lead)

    def update_lead(self,lead):
        self._update_module_record("Leads",lead,lead.lead_id)  

    def get_contact(self,id:str):
        return self._get_module_record("Contacts",id)     

    def create_contact(self,contact):
        return self._create_module_record("Contacts",contact)

    def update_contact(self,contact):
        self._update_module_record("Contacts",contact,contact.contact_id)

    # Searching

    def search_by_criteria(self,module,criteria,page=1,per_page=200):
        try:
            module = self.modules_api_names[module]
            parser = self._get_module_parser(module)
            response = zcrmsdk.ZCRMModule(module).\
                search_records_by_criteria(criteria,page=page,per_page=per_page).response_json['data']
            return [parser().parse(record) for record in response]
        except ZCRMException as ex:
            raise ZohoCRMAPIException(ex.error_code,ex.error_message,module,error_details=ex.error_details)

    def search_by_phone(self,module,phone,page=1,per_page=200):
        module = self.modules_api_names[module]
        parser = self._get_module_parser(module)
        try:
            response = zcrmsdk.ZCRMModule(module).\
                search_records_by_phone(phone,page=page,per_page=per_page).response_json['data']
            return [parser().parse(record) for record in response]
        except ZCRMException as ex:
            return []

    def search_by_email(self,module,email,page=1,per_page=200):
        module = self.modules_api_names[module]
        parser = self._get_module_parser(module)
        try:
            response = zcrmsdk.ZCRMModule(module).\
                search_records_by_email(email,page=page,per_page=per_page).response_json['data']
            return [parser().parse(record) for record in response]      
        except ZCRMException as ex:  
            return []

    def search_leads_by_criteria(self,criteria,page=1,per_page=200):
        return self.search_by_criteria("Leads",criteria,page,per_page)

    def search_contacts_by_criteria(self,criteria,page=1,per_page=200):
        return self.search_by_criteria("Contacts",criteria,page,per_page)

    def search_deals_by_criteria(self,criteria,page=1,per_page=200):
        return self.search_by_criteria("Deals",criteria,page,per_page)

    # Related records

    def get_related_records(self,child_module,parent_module,record_id):
        try:
            record = ZCRMRecord(self.modules_api_names[parent_module], record_id)
            response_list = record.get_relatedlist_records(self.modules_api_names[child_module]).response_json
            parser = self._get_module_parser(child_module)()
            return [parser.parse(el) for el in response_list["data"]]
        except ZCRMException as ex:
            raise ZohoCRMAPIException(ex.status_code,ex.message,parent_module,record_id)  

    def get_group_deals(self,group_id:str):
        return self.get_related_records("Deals","Groups",group_id)

    def get_contact_deals(self,contact_id:str):
        return self.get_related_records("Deals","Contacts",contact_id)

    # Additional

    def get_crm_user(self,user_id):
        return ZCRMUser.get_instance(user_id, None)

    def get_group_fields(self):
        return zcrmsdk.ZCRMModule(self.modules_api_names["Groups"]).get_all_fields().response_json['fields']

    def get_deal_fields(self):
        return zcrmsdk.ZCRMModule(self.modules_api_names["Deals"]).get_all_fields().response_json['fields']

    def get_actual_products_list(self):
        for value in self.get_deal_fields():
            if value['api_name'] == 'Products_deal':
                return [ v['display_value'] for v in value['pick_list_values']]

    def get_all_visits(self):
        print(zcrmsdk.ZCRMModule("Visits").get_records())


def generate_access_token():
    from .connection import zcrmsdk
    from .django_models import AuthToken
    from .exceptions import ZohoCRMAPIInitializationException

    # if auth tokens didn't haven't been generated yet
    if AuthToken.objects.first():
        print("Auth Token exist")
        return

    oauth_client = zcrmsdk.ZohoOAuth.get_client_instance()
    grant_token=input("Please, paste grant token: ")
    oauth_tokens = oauth_client.generate_access_token(grant_token)
    print("Auth Token created")
