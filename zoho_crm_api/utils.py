from .conf import MODULES

from zcrmsdk.Handler import APIHandler
from zcrmsdk.CLException import ZCRMException
from zcrmsdk.Utility import APIConstants
from zcrmsdk.Request import APIRequest


class BlueprintAPI():
    def __init__(self):
        self._MAIN_URL = '{module_api_name}/{record_id}/actions/blueprint'
        self.modules_api_names = MODULES

    def get_record_blueprint(self,module,id):
        handler_ins=APIHandler()
        handler_ins.request_url_path=self._MAIN_URL.format(module_api_name=self.modules_api_names[module],
                                                            record_id=id)
        handler_ins.request_method=APIConstants.REQUEST_METHOD_GET
        handler_ins.request_api_key=APIConstants.DATA
        apiResponse=APIRequest(handler_ins).get_api_response()
        return apiResponse.response_json

    def update_record_blueprint(self,module,id,transition_id,additional_data={}):
        handler_ins=APIHandler()
        handler_ins.request_url_path=self._MAIN_URL.format(module_api_name=self.modules_api_names[module],
                                                            record_id=id)
        handler_ins.request_method=APIConstants.REQUEST_METHOD_PUT
        handler_ins.request_api_key=APIConstants.DATA
        handler_ins.request_body={"blueprint":[{"transition_id":transition_id,"data":additional_data}]}
        apiResponse=APIRequest(handler_ins).get_api_response()
        return apiResponse.response_json

