

class ZohoCRMAPI_NoRecord_Exception(Exception):
    message = "Cannot find record in module {} by id {}. Message: {}"
    def __init__(self,error_code,error_message,error_module,error_record_id):
        self.error_code = error_code
        self.error_message = error_message
        self.error_module = error_module
        self.error_record_id = error_record_id

    def get_message(self):
        return self.message.format(self.error_module,self.error_record_id,self.error_message)

    def __str__(self):
        return self.message.format(self.error_module,self.error_record_id,self.error_message)


class ZohoCRMAPI_NoProject_Exception(Exception):
    message = "No project in deal by id {}. Message: {}"
    def __init__(self,error_code,error_message,error_record_id):
        self.error_code = error_code
        self.error_message = error_message
        self.error_record_id = error_record_id

    def get_message(self):
        return self.message.format(self.error_message,self.error_record_id)

    def __str__(self):
        return self.message.format(self.error_message,self.error_record_id)


class ZohoCRMAPI_ProjectCreate_Exception(Exception):
    message = "Cannot create project. Message: {}"
    def __init__(self,error_code,error_message):
        self.error_code = error_code
        self.error_message = error_message

    def get_message(self):
        return self.message.format(self.error_message)

    def __str__(self):
        return self.message.format(self.error_message)


class ZohoCRMAPIException(Exception):
    def __init__(self,error_code,error_message,error_module,error_record_id=None):
        self.error_code = error_code
        self.error_message = error_message
        self.error_module = error_module
        self.error_record_id = error_record_id

    def get_message(self):
        message = f"Crm API exception. Code:{self.error_code}. Message:{self.error_message}. Module: {self.error_module}."
        if self.error_record_id:
            message += f" Record id:{self.error_record_id}"
        return message
        
    def __str__(self):
        return self.get_message()


class ZohoCRMAPIInitializationException(Exception):
    def __init__(self,error_code,error_message):
        self.error_code = error_code
        self.error_message = error_message

    def get_message(self):
        message = f"Code:{self.error_code}. Message:{self.error_message}."
        return message
        
    def __str__(self):
        return self.get_message()