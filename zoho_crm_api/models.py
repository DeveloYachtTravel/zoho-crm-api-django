class Co_worker():
    def __init__(self):
        self.co_worker_id = None
        self.charter_folder_id = None
        self.name = None
        self.email = None
        self.books_vendor_id = None
        self.user = None
        self.bonuses = None
        self.number_of_bonuses = 0
        self.bonuses_bills = None

    def to_json(self):
        data = {}
        data['id'] = self.co_worker_id
        data['User_charters_folder'] = self.charter_folder_id
        data['Name'] = self.name
        data['Email'] = self.email
        data['User_Name'] = self.user
        data['books_vendor_id'] = self.books_vendor_id
        data['Bonuses'] = self.bonuses
        data['Bonuses_Bills'] = self.bonuses_bills
        return data


class Contact():
    def __init__(self):
        self.contact_id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.second_phone = None
        self.third_phone = None
        self.email = None
        self.second_email = None
        self.third_email = None
        self.moodle_id = None
        self.moodle_last_access = None
        self.moodle_percent = None
        self.telegram_user_id = None
        self.telegram_link = None
        self.telegram_level = None
        self.workdrive_link = None
        self.workdrive_folder_id = None

    def to_json(self):
        data = {}
        data['id'] = self.contact_id
        data['First_Name'] = self.first_name
        data['Last_Name'] = self.last_name
        data['Phone'] = self.phone
        data['Other_Phone'] = self.second_phone
        data['Third_phone'] = self.third_phone
        data['Email'] = self.email
        data['Second_Email'] = self.second_email
        data['Third_Email'] = self.third_email
        data['moodle_id'] = self.moodle_id
        if self.moodle_last_access:
            data['Moodle_last_access'] = self.moodle_last_access.strftime("%Y-%m-%dT%H:%M:%S") 
        data['Moodle_progress_percent'] = self.moodle_percent
        data['telegram_user_id'] = self.telegram_user_id
        data['Telegram_link'] = self.telegram_link
        data['telegram_user_level'] = self.telegram_level
        data['Workdrive_link'] = self.workdrive_link
        data['workdrive_folder_id'] = self.workdrive_folder_id
        return data


class Crew_member():
    def __init__(self):
        self.crew_member_id = None
        self.contact = None
        self.name = None
        self.passport_name = None
        self.passport_surname = None
        self.passport_db = None
        self.passport_numb = None
        self.passport_nationality = None
        self.passport_valid_till = None
        self.passport_sex = None
        self.passport_place_of_birth = None

    def to_json(self):
        data = {}
        data['id'] = self.crew_member_id
        data['Contact'] = self.contact
        data['Name'] = self.name
        data['Name1'] = self.passport_name
        data['Nationality'] = self.passport_nationality
        data['Passp_numb'] = self.passport_numb
        data['Place_of_Birth'] = self.passport_place_of_birth
        data['Sex'] = self.passport_sex
        data['Surname'] = self.passport_surname
        if self.passport_valid_till:
            data['Valid_till'] = self.passport_valid_till.strftime("%Y-%m-%d")
        if self.passport_db:
            data['DB'] = self.passport_db.strftime("%Y-%m-%d")
        return data


class Deal():
    def __init__(self):
        self.deal_name = None
        self.deal_id = None
        self.contact_name = None
        self.product = None
        self.product_type = None
        self.stage = None
        self.products = None
        self.amount = None
        self.currency_amount = None
        self.corporate_client = None
        self.group = None
        self.start_date = None
        self.finish_date = None
        self.check_in = None
        self.check_out = None
        self.region = None
        self.client_price_contract = None
        self.client_price_fact = None
        self.yacht = None
        self.yacht_name = None
        self.model = None
        self.year = None
        self.operator = None
        self.country = None
        self.start_base = None
        self.finish_base = None
        self.pier = None
        self.base_manager = None
        self.manager_phone = None
        self.net_price = None
        self.agency_commision_contract = None
        self.agency_commision_fact = None
        self.margin = None
        self.paid_total = None
        self.otkat = None
        self.books_project_url = None
        self.license_date = None
        self.instructor = None
        self.practice_result = None
        self.instructor_comment = None
        self.instructot_condition = None
        self.workdrive_client_url = None
        self.workdrive_local_url = None
        self.workdrive_folder_id = None
        self.workdrive_folder_password = None
        self.workdrive_passport_folder_url = None
        self.books_bill_id = None
        self.books_invoice_id = None
        self.books_bonus_bill_id = None
        self.books_license_instructor_bill_id = None
        self.discount = 0
        self.crew_list_place_birth = None
        self.crew_list_sex = None
        self.crew_members = None
        self.add_vhf_license = None
        self.deal_owner = None
        self.currency = None
        self.first_payment_amount = None
        self.first_payment_date = None
        self.first_transfer_amount = None
        self.second_payment_amount = None
        self.second_payment_date = None
        self.second_transfer_amount = None
        self.third_payment_amount = None
        self.third_payment_date = None
        self.third_transfer_amount = None
        self.commission_summ = None
        self.skipper_deal_id = None
        self.skipper_income = None
        self.skipper_outcome = None
        self.skipper_vendor_id = None

    def to_json(self):
        from datetime import datetime
        deal_data = {}
        deal_data['id'] = self.deal_id
        deal_data['Deal_Name'] = self.deal_name
        deal_data['Contact_Name'] = self.contact_name
        deal_data['Product_type'] = self.product_type
        deal_data['Stage'] = self.stage
        deal_data['Products_deal'] = self.products
        deal_data['Amount'] = self.amount
        deal_data['Currency_amount'] = self.currency_amount
        deal_data['Discount'] = self.discount
        deal_data['Group'] = self.group
        if self.start_date:
            deal_data['Start_date'] = datetime.strftime(self.start_date,
                                                        "%Y-%m-%dT%H:%M:%S")
        if self.finish_date:
            deal_data['finish_time'] = datetime.strftime(self.finish_date,
                                                        "%Y-%m-%dT%H:%M:%S")
        if self.check_in:
            deal_data['Chek_in_date'] = self.check_in.strftime("%Y-%m-%d")
        if self.check_out:
            deal_data['Check_out_date'] = self.check_out.strftime("%Y-%m-%d")
        if self.license_date:
            deal_data['License_date'] = self.license_date.strftime("%Y-%m-%d")
        deal_data['Client_price_real'] = self.client_price_fact
        deal_data['Client_price_contr'] = self.client_price_contract
        deal_data['net_price'] = self.net_price
        deal_data['Yacht'] = self.yacht
        deal_data['Yacht_Name'] = self.yacht_name
        deal_data['Model'] = self.model
        deal_data['Year'] = self.year
        deal_data['Operator'] = self.operator
        deal_data['Country1'] = self.country
        deal_data['Start_base'] = self.start_base
        deal_data['Finish_base'] = self.finish_base
        deal_data['pier'] = self.pier
        deal_data['base_manager'] = self.base_manager
        deal_data['manager_phone'] = self.manager_phone
        deal_data['Agency_commission_fact'] = self.agency_commision_fact
        deal_data['Agency_commission'] = self.agency_commision_contract
        deal_data['Margin'] = self.margin
        deal_data['Paid_total'] = self.paid_total
        deal_data['Refund_amount'] = self.otkat
        deal_data['Project_URL'] = self.books_project_url
        deal_data['Inshore_VHF'] = self.add_vhf_license
        deal_data['Instructor'] = self.instructor
        deal_data['Instructor_condition'] = self.instructot_condition
        deal_data['Owner'] = self.deal_owner
        deal_data['workdrive_client_url'] = self.workdrive_client_url
        deal_data['workdrive_local_url'] = self.workdrive_local_url
        deal_data['Workdrive_folder_id'] = self.workdrive_folder_id
        deal_data['Workdrive_password'] = self.workdrive_folder_password
        deal_data['Workdrive_passports_folder'] = self.workdrive_passport_folder_url
        deal_data['Add_place_of_birth_to_crew_list'] = self.crew_list_place_birth
        deal_data['Add_sex_to_crew_list'] = self.crew_list_sex
        deal_data['Instructor_result'] = self.practice_result
        deal_data['Instructor_comment'] = self.instructor_comment
        deal_data['books_bill_id'] = self.books_bill_id
        deal_data['books_invoice_id'] = self.books_invoice_id
        deal_data['books_bonus_bill_id'] = self.books_bonus_bill_id
        deal_data['books_license_instructor_bill_id'] = self.books_license_instructor_bill_id

        if self.first_payment_date:
            deal_data['Date_of_1st_payment'] = self.first_payment_date.strftime("%Y-%m-%d")
        deal_data['Amount_of_1st_payment'] =self.first_payment_amount
        deal_data['Amount_of_1st_transfer'] = self.first_transfer_amount
        if self.second_payment_date:
            deal_data['Date_of_2nd_payment'] = self.second_payment_date.strftime("%Y-%m-%d")
        deal_data['Amount_of_2nd_payment'] = self.second_payment_amount
        deal_data['Amount_of_2nd_transfer'] = self.second_transfer_amount
        if self.third_payment_date:
            deal_data['Date_of_3rd_payments'] = self.third_payment_date.strftime("%Y-%m-%d")
        deal_data['Amount_of_3rd_payment'] = self.third_payment_amount
        deal_data['Amount_of_3rd_transfer'] = self.third_transfer_amount
        deal_data['Commission_summ'] = self.commission_summ
        deal_data['skipper_deal_id'] = self.skipper_deal_id
        deal_data['Skipper_income'] = self.skipper_income
        deal_data['Skipper_outcome'] = self.skipper_outcome
        deal_data['skipper_vendor_id'] = self.skipper_vendor_id
        return deal_data


class Envelope():
    def __init__(self):
        self.envelope_id = None
        self.envelope_name = None
        self.verificated = None
        self.created_at = None

    def to_json(self):
        from datetime import datetime
        envelope_data = {}
        envelope_data['Name'] = self.envelope_name
        envelope_data['Verificated'] = self.verificated
        if self.created_at:
            envelope_data['Created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S") 
        return envelope_data


class Group():
    def __init__(self):
        self.group_name = None
        self.group_id = None
        self.products = None
        self.status = None
        self.product_type = None
        self.start_date_time = None
        self.finish_date_time = None
        self.price = None
        self.instructor = None
        self.country = None
        self.currency = None
        self.start_base = None
        self.yacht = None
        self.yacht_name = None
        self.model = None
        self.yacht_year = None
        self.operator = None
        self.net_price = None
        self.skipper_fee = None
        self.agency_commission = None
        self.income_fact = None
        self.base_manager = None
        self.managers_phone = None
        self.pier = None
        self.participant_fact = 0
        self.participant_plan = 0
        self.project_id = None
        self.catering_and_stationery = None
        self.automobile_expense = None
        self.instructor_fee = None
        self.automobile_bill_id = None
        self.catering_bill_id = None
        self.instructor_bill_id = None
        self.skipper_fee_bill = None
        self.net_price_bill = None
        self.workdrive_client_url = None
        self.workdrive_local_url = None
        self.workdrive_folder_id = None
        self.workdrive_folder_password = None
        self.skipper = None
        self.crew_members = None
        self.additional_bills = None
        self.additional_expenses = None
        self.bonus_bill_id = None

    def to_json(self,safety=False):
        group_data = {}
        group_data['id'] = self.group_id
        group_data['Name'] = self.group_name
        group_data['Products'] = self.products
        group_data['Status'] = self.status
        group_data['Product_type'] = self.product_type
        if self.start_date_time:
            group_data['Start_date'] =  self.start_date_time.strftime("%Y-%m-%dT%H:%M:%S") 
        if self.finish_date_time:
            group_data['finish_time'] = self.finish_date_time.strftime("%Y-%m-%dT%H:%M:%S")   
        group_data['Price'] = self.price
        group_data['Instructor'] = self.instructor
        group_data['Skipper'] = self.skipper
        if not safety:
            group_data['Country'] = self.country
            group_data['Currency'] = self.currency
            group_data['Start_base'] = self.start_base
            group_data['Yacht'] = self.yacht
            group_data['Yacht_Name'] = self.yacht_name
            group_data['Model'] = self.model
            group_data['Yacht_Year'] = self.yacht_year
            group_data['Operator'] = self.operator
            group_data['Yacht_netto_price'] = self.net_price
            group_data['Skipper_fee'] = self.skipper_fee
            group_data['skipper_fee_bill'] = self.skipper_fee_bill
            group_data['net_price_bill'] = self.net_price_bill
            group_data['Agency_commission'] = self.agency_commission
            group_data['income_fact'] = self.income_fact
            group_data['base_manager'] = self.base_manager
            group_data['manager_phone'] = self.managers_phone
            group_data['pier'] = self.pier
            group_data['participants_fact'] = self.participant_fact
            group_data['field8'] = self.participant_plan
            group_data['Project_ID'] = self.project_id
            group_data['Instructor_s_fee'] = self.instructor_fee
            group_data['Catering_and_stationery_for_s'] = self.catering_and_stationery
            group_data['Automobile_expense'] = self.automobile_expense
            group_data['automobile_bill_id'] = self.automobile_bill_id
            group_data['catering_bill_id'] = self.catering_bill_id
            group_data['instructor_bill_id'] = self.instructor_bill_id
            group_data['Workdrive_client_folder_url'] = self.workdrive_client_url
            group_data['Workdrive_folder_url'] = self.workdrive_local_url
            group_data['Workdrive_folder_id'] = self.workdrive_folder_id
            group_data['Workdrive_password'] = self.workdrive_folder_password
            group_data['additional_bills'] = self.additional_bills
            group_data['additional_expenses1'] = self.additional_expenses
            group_data['bonus_bill_id'] = self.bonus_bill_id
        return group_data


class Lead():
    def __init__(self):
        self.lead_id = None
        self.first_name = None
        self.last_name = None
        self.phone = None
        self.second_phone = None
        self.third_phone = None
        self.email = None
        self.second_email = None
        self.third_email = None
        self.referrer = None
        self.city = None
        self.moodle_id = None
        self.moodle_percent = None
        self.moodle_last_access = None
        self.country = None
        self.products = None
        self.product_type = None
        self.communication_channel = None
        self.owner = None

    def to_json(self):
        data = {}
        data['id'] = self.lead_id
        data['First_Name'] = self.first_name
        data['Last_Name'] = self.last_name
        data['Phone'] = self.phone
        data['Email'] = self.email
        data['Second_email'] = self.second_email
        data['Third_Email'] = self.third_email
        data['Referrer'] = self.referrer 
        data['moodle_id'] = self.moodle_id
        if self.moodle_last_access:
            data['Moodle_last_access'] = self.moodle_last_access.strftime("%Y-%m-%dT%H:%M:%S") 
        data['Moodle_progress_percent'] = self.moodle_percent
        data['City'] = self.city
        data['Product_type'] = self.product_type
        data['Products1'] = self.products
        data['Country'] = self.country
        data['Second_phone'] = self.second_phone
        data['Other_phone'] = self.third_phone
        data['comun_ch'] = self.communication_channel
        data['Owner'] = self.owner
        return data


class Operator():
    def __init__(self):
        self.operator_id = None
        self.operator_name = None
        self.telegram_link = None
        self.telegram_user_id = None
        self.telegram_level = None

    def to_json(self):
        data = {}
        data['id'] = self.operator_id
        data['Vendor_Name'] = self.operator_name
        data['telegram_user_level'] = self.telegram_level
        data['Telegram_link'] = self.telegram_link
        data['telegram_user_id'] = self.telegram_user_id
        return data


class Event():
    def __init__(self):
        self.deal = None
        self.contact = None
        self.event_time = None
        self.event_name = None
        self.photo_url = None
        self.message = None
        self.keyboard = None

    def to_json(self):
        from datetime import datetime
        data = {}
        data['Deal_related'] = self.deal        
        data['Contact'] = self.contact
        if self.event_time and isinstance(self.event_time,datetime):
            data['Event_time'] = datetime.strftime(self.event_time,"%Y-%m-%dT%H:%M:%S")
        data['Event_name'] = self.event_name
        data['Photo_url'] = self.photo_url
        data['Message_text'] = self.message
        data['Keyboard'] = self.keyboard
        return data


class Transaction():
    def __init__(self):
        self.transaction_id = None
        self.transaction_name = None
        self.manager = None
        self.type = None
        self.account = None
        self.currency = None
        self.euro_amount = None
        self.currency_amount = None
        self.expense_account = None
        self.exchange_rate = 1
        self.envelope = None
        self.deal_id = None
        self.comment = None
        self.approved = False
        self.created_at = None

    def to_json(self):
        from datetime import datetime
        transaction_data = {}
        transaction_data['Name'] = self.transaction_name
        transaction_data['Manager'] = self.manager
        transaction_data['Type'] = self.type
        transaction_data['Account'] = self.account
        transaction_data['Selected_currency'] = self.currency
        transaction_data['Euro_amount'] = self.euro_amount
        transaction_data['Currency_amount'] = self.currency_amount
        transaction_data['Expense_account'] = self.expense_account
        if self.exchange_rate != 1:
            transaction_data['Exchange_Rate'] = self.expense_account
        transaction_data['Envelope'] = self.envelope
        if self.created_at:
            transaction_data['Created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S") 
        transaction_data['Comment'] = self.comment
        transaction_data['Approved'] = self.approved
        transaction_data['deal_id'] = self.deal_id
        return transaction_data
