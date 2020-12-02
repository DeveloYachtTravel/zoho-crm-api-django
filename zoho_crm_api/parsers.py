from .models import *
from datetime import datetime

def parse_datetime(date):
        if type(date) == str:
            date_time_obj = datetime.strptime(date[:19], '%Y-%m-%dT%H:%M:%S')
            return date_time_obj
        else:
            return date 

def parse_date(date):
        if type(date) == str:
            date_time_obj = datetime.strptime(date, '%Y-%m-%d')
            return date_time_obj
        else:
            return date 

class Co_worker_parser():
    def parse(self,worker_data):
        if worker_data.get("data"):
            worker_data = worker_data.get('data')[0]
        co_worker = Co_worker()
        co_worker.co_worker_id = worker_data.get('id',None)
        co_worker.name = worker_data.get('Name',None)
        co_worker.email = worker_data.get('Email',None)
        co_worker.user = worker_data.get('User_Name',None)
        co_worker.books_vendor_id = worker_data.get('books_vendor_id',None)
        co_worker.charter_folder_id = worker_data.get('User_charters_folder',None)
        co_worker.bonuses = worker_data.get('Bonuses',None)
        co_worker.number_of_bonuses = len(worker_data.get('Bonuses',[]))
        co_worker.bonuses_bills = worker_data.get('Bonuses_Bills',None)
        return co_worker


class Contact_parser():
    def parse(self,contact_data):
        if contact_data.get("data"):
            contact_data = contact_data.get('data')[0]
        contact = Contact()
        contact.contact_id = contact_data.get('id',None)
        contact.first_name = contact_data.get('First_Name',None)
        contact.last_name = contact_data.get('Last_Name',None)
        contact.phone = contact_data.get('Phone',None)
        contact.second_phone = contact_data.get('Other_Phone',None)
        contact.third_phone = contact_data.get('Third_phone',None)
        contact.email = contact_data.get('Email',None)
        contact.second_email = contact_data.get('Second_Email',None)
        contact.third_email = contact_data.get('Third_Email',None)
        contact.moodle_id = contact_data.get('moodle_id',None)
        contact.moodle_last_access = parse_datetime(contact_data.get('Moodle_last_access',None))
        contact.moodle_percent = contact_data.get('Moodle_progress_percent',None)
        contact.telegram_user_id = contact_data.get('telegram_user_id',None)
        contact.telegram_link = contact_data.get('Telegram_link',None)
        contact.telegram_level = contact_data.get('telegram_user_level',None)
        contact.workdrive_link = contact_data.get('Workdrive_link',None)
        contact.workdrive_folder_id = contact_data.get('workdrive_folder_id',None)
        return contact


class Crew_member_parser():
    def parse(self,crew_member_data):
        crew_member = Crew_member()
        crew_member.crew_member_id = crew_member_data.get('id',None)
        crew_member.contact = crew_member_data.get('Contact',None)
        crew_member.name = crew_member_data.get('Name',None)
        crew_member.passport_name = crew_member_data.get('Name1',None)
        crew_member.passport_nationality = crew_member_data.get('Nationality',None)
        crew_member.passport_numb = crew_member_data.get('Passp_numb',None)
        crew_member.passport_place_of_birth = crew_member_data.get('Place_of_Birth',None)
        crew_member.passport_sex = crew_member_data.get('Sex',None)
        crew_member.passport_surname = crew_member_data.get('Surname',None)
        crew_member.passport_valid_till = parse_datetime(crew_member_data.get('Valid_till',None))
        crew_member.passport_db = parse_datetime(crew_member_data.get('DB',None))
        return crew_member


class Deal_parser():
    def parse(self,deal_data):
        if deal_data.get("data"):
            deal_data = deal_data.get('data')[0]
        deal = Deal()
        deal.deal_name = deal_data.get('Deal_Name',None)
        deal.deal_id = deal_data.get('id',None)
        deal.contact_name = deal_data.get('Contact_Name',None)
        deal.product_type = deal_data.get('Product_type',None)
        deal.corporate_client = deal_data.get('Account_Name',None)
        deal.stage = deal_data.get('Stage',None)
        deal.products = deal_data.get('Products_deal',None)
        deal.amount = deal_data.get('Amount',None)
        deal.currency_amount = deal_data.get('Currency_amount',None)
        deal.lead_source = deal_data.get('Lead_Sources',None)
        if isinstance(deal_data.get('Group'),dict):
            deal.group = deal_data.get('Group').get("id")
        elif isinstance(deal_data.get('Group'),str):
            deal.group = deal_data.get('Group')
        else:
            deal.group = None
        deal.start_date = parse_datetime(deal_data.get('Start_date',None))
        deal.finish_date = parse_datetime(deal_data.get('finish_time',None))
        deal.check_in = parse_date(deal_data.get('Chek_in_date',None))
        deal.check_out = parse_date(deal_data.get('Check_out_date',None))
        deal.license_date = parse_date(deal_data.get('License_date',None))
        deal.client_price_fact = deal_data.get('Client_price_real',None)
        deal.client_price_contract = deal_data.get('Client_price_contr',None)
        deal.net_price = deal_data.get('net_price',None)
        deal.yacht = deal_data.get('Yacht')
        deal.yacht_name = deal_data.get('Yacht_Name',None)
        deal.model = deal_data.get('Model',None)
        deal.year = deal_data.get('Year',None)
        deal.operator = deal_data.get('Operator')
        deal.country = deal_data.get('Country1',None)
        deal.start_base = deal_data.get('Start_base',None)
        deal.finish_base = deal_data.get('Finish_base',None)
        deal.pier = deal_data.get('pier',None)
        deal.base_manager = deal_data.get('base_manager',None)
        deal.manager_phone = deal_data.get('manager_phone',None)
        deal.agency_commision_fact = deal_data.get('Agency_commission_fact',None)
        deal.agency_commision_contract = deal_data.get('Agency_commission',None)
        deal.margin = deal_data.get('Margin',None)
        deal.paid_total = deal_data.get('Paid_total',None)
        deal.otkat = deal_data.get('Refund_amount',None)
        deal.discount = deal_data.get('Discount',None)
        deal.books_project_url = deal_data.get('Project_URL',None)
        deal.instructor = deal_data.get('Instructor',None)
        deal.instructot_condition = deal_data.get('Instructor_condition',None)
        deal.add_vhf_license = deal_data.get('Inshore_VHF',None)
        deal.deal_owner = deal_data.get('Owner')
        deal.books_bill_id = deal_data.get('books_bill_id',None)
        deal.books_invoice_id = deal_data.get('books_invoice_id',None)
        deal.books_bonus_bill_id = deal_data.get('books_bonus_bill_id',None)
        deal.books_license_instructor_bill_id = deal_data.get('books_license_instructor_bill_id',None)
        deal.crew_members = deal_data.get('Crew',None)
        deal.workdrive_client_url = deal_data.get('workdrive_client_url',None)
        deal.workdrive_local_url = deal_data.get('workdrive_local_url',None)
        deal.workdrive_folder_id = deal_data.get('Workdrive_folder_id',None)
        deal.workdrive_folder_password = deal_data.get('Workdrive_password',None)
        deal.workdrive_passport_folder_url = deal_data.get('Workdrive_passports_folder',None)
        deal.crew_list_place_birth = deal_data.get('Add_place_of_birth_to_crew_list',None)
        deal.crew_list_sex = deal_data.get('Add_sex_to_crew_list',None)
        deal.practice_result = deal_data.get('Instructor_result',None)
        deal.instructor_comment = deal_data.get('Instructor_comment',None)
        deal.currency = deal_data.get('Currency',None)

        deal.first_payment_date = parse_date(deal_data.get('Date_of_1st_payment',None))
        deal.first_payment_amount = deal_data.get('Amount_of_1st_payment',None)
        deal.first_transfer_amount = deal_data.get('Amount_of_1st_transfer',None)
        deal.second_payment_date = parse_date(deal_data.get('Date_of_2nd_payment',None))
        deal.second_payment_amount = deal_data.get('Amount_of_2nd_payment',None)
        deal.second_transfer_amount = deal_data.get('Amount_of_2nd_transfer',None)
        deal.third_payment_date = parse_date(deal_data.get('Date_of_3rd_payments',None))
        deal.third_payment_amount = deal_data.get('Amount_of_3rd_payment',None)
        deal.third_transfer_amount = deal_data.get('Amount_of_3rd_transfer',None)
        deal.commission_summ = deal_data.get('Commission_summ',None)
        deal.skipper_deal_id = deal_data.get('skipper_deal_id',None)

        deal.skipper_income = deal_data.get('Skipper_income',None)
        deal.skipper_outcome = deal_data.get('Skipper_outcome',None)
        deal.skipper_vendor_id = deal_data.get('skipper_vendor_id',None)
        return deal
   

class Envelope_parser():
    def parse(self,envelope_data):
        envelope = Envelope()
        envelope.envelope_id = envelope_data.get('id',None)
        envelope.envelope_name = envelope_data.get('Name',None)
        envelope.verificated = envelope_data.get('Verificated',None)
        envelope.created_at = parse_datetime(envelope_data.get('Created_at',None))
        return envelope


class Group_parser():        
    def parse(self,group_data):
        if group_data.get("data"):
            group_data = group_data.get('data')[0]
        group = Group()
        group.agency_commission = group_data.get('Agency_commission',None)
        group.base_manager = group_data.get('base_manager',None)
        group.country = group_data.get('Country',None)
        group.currency = group_data.get('Currency',None)
        group.finish_date_time = parse_datetime(group_data.get('finish_time',None))
        group.group_id = group_data.get('id',None)
        group.group_name = group_data.get('Name',None)
        group.instructor = group_data.get('Instructor',None)
        group.managers_phone = group_data.get('manager_phone',None)
        group.model = group_data.get('Model',None)
        group.net_price = group_data.get('Yacht_netto_price',None)
        group.operator = group_data.get('Operator',None)
        group.participant_fact = group_data.get('participants_fact',None)
        group.participant_plan = group_data.get('field8',None)
        group.pier = group_data.get('pier',None)
        group.price = group_data.get('Price',None)
        group.product_type = group_data.get('Product_type',None)
        group.products = group_data.get('Products',None)
        group.skipper_fee_bill = group_data.get('skipper_fee_bill',None)
        group.net_price_bill = group_data.get('net_price_bill',None)
        group.skipper_fee = group_data.get('Skipper_fee','')
        group.start_base = group_data.get('Start_base',None)
        group.start_date_time = parse_datetime(group_data.get('Start_date',None))
        group.status = group_data.get('Status',None)
        group.yacht = group_data.get('Yacht',None)
        group.yacht_name = group_data.get('Yacht_Name',None)
        group.yacht_year = group_data.get('Yacht_Year',None)
        group.project_id = group_data.get('Project_ID',None)
        group.automobile_bill_id = group_data.get('automobile_bill_id',None)
        group.catering_bill_id = group_data.get('catering_bill_id',None)
        group.instructor_bill_id = group_data.get('instructor_bill_id',None)
        group.workdrive_client_url = group_data.get('Workdrive_client_folder_url',None)
        group.workdrive_local_url = group_data.get('Workdrive_folder_url',None)
        group.workdrive_folder_id = group_data.get('Workdrive_folder_id',None)
        group.workdrive_folder_password = group_data.get('Workdrive_password',None)
        group.income_fact = group_data.get('income_fact',None)
        group.skipper = group_data.get('Skipper',None)
        group.crew_members = group_data.get('Crew_list',None)
        group.automobile_expense = group_data.get('Automobile_expense','')
        group.catering_and_stationery = group_data.get('Catering_and_stationery_for_s','')
        group.instructor_fee = group_data.get('Instructor_s_fee','')
        group.additional_bills = group_data.get('additional_bills','')
        group.additional_expenses = group_data.get('additional_expenses1','')
        group.bonus_bill_id = group_data.get('bonus_bill_id',None)
        return group


class Lead_parser():
    def parse(self,lead_data):
        if lead_data.get("data"):
            lead_data = lead_data.get('data')[0]
        lead = Lead()
        lead.lead_id = lead_data.get('id',None)
        lead.first_name = lead_data.get('First_Name',None)
        lead.last_name = lead_data.get('Last_Name',None)
        lead.phone = lead_data.get('Phone',None)
        lead.second_phone = lead_data.get('Second_phone',None)
        lead.third_phone = lead_data.get('Other_phone',None)
        lead.email = lead_data.get('Email',None)
        lead.second_email = lead_data.get('Second_email',None)
        lead.third_email = lead_data.get('Third_Email',None)
        lead.referrer = lead_data.get('Referrer',None)
        lead.moodle_id = lead_data.get('moodle_id',None)
        lead.moodle_last_access = parse_datetime(lead_data.get('Moodle_last_access',None))
        lead.moodle_percent = lead_data.get('Moodle_progress_percent',None)
        lead.city = lead_data.get('City',None)
        lead.country = lead_data.get('Country',None)
        lead.product_type = lead_data.get('Product_type',None)
        lead.products = lead_data.get('Products1',None)
        lead.communication_channel = lead_data.get('comun_ch',None)
        lead.owner = lead_data.get('Owner',None)
        lead.request_url = lead_data.get('Request_url',None)
        return lead


class Operator_parser():
    def parse(self,operator_data):
        operator = Operator()
        operator.operator_id = operator_data.get('id',None)
        operator.operator_name = operator_data.get('Vendor_Name',None)
        operator.telegram_user_id = operator_data.get('telegram_user_id',None)
        operator.telegram_link = operator_data.get('Telegram_link',None)
        operator.telegram_level = operator_data.get('telegram_user_level',None)
        return operator


class Tg_event_parser():
    def parse(self,event_data):
        event = Event()
        event.event_name = event_data.get('Event_name',None)
        event.deal = event_data.get('Deal_related',None)
        event.contact = event_data.get('Contact',None)
        event.event_time = parse_datetime(event_data.get('Event_time',None))
        event.photo_url = event_data.get('Photo_url',None)
        event.message = event_data.get('Message_text',None)
        event.keyboard = event_data.get('Keyboard',None)
        return event


class Transaction_parser():
    def parse(self,transaction_data):
        from json import loads
        transaction = Transaction()
        transaction.transaction_id = transaction_data.get('id',None)
        transaction.transaction_name = transaction_data.get('Name',None)
        transaction.manager = transaction_data.get('Manager',None)
        transaction.type = transaction_data.get('Type',None)
        transaction.currency = transaction_data.get('Selected_currency',None)
        transaction.euro_amount = transaction_data.get('Euro_amount',None)
        transaction.currency_amount = transaction_data.get('Currency_amount',None)
        transaction.exchange_rate = transaction_data.get('Exchange_Rate',None)
        transaction.envelope = transaction_data.get('Envelope',None)
        transaction.deal_id = transaction_data.get('deal_id',None)
        transaction.approved = transaction_data.get('Approved',None)
        transaction.comment = transaction_data.get('Comment',None)
        transaction.created_at = parse_datetime(transaction_data.get('Created_at',None))

        if transaction_data.get('Account',None):
            transaction.account = loads(transaction_data.get('Account',None))
        else:
            transaction.account = transaction_data.get('Account',None)
        if transaction_data.get('Expense_account',None):
            transaction.expense_account = loads(transaction_data.get('Expense_account',None))
        else:
            transaction.expense_account = transaction_data.get('Expense_account',None)
        return transaction