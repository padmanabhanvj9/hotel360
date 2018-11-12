from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_SELECT_AccountPostHistory(request):
    invoice_no = request.json['invoice_no']
    result = json.loads(dbget("select employee.emp_firstname,account_posting_history.* \
                               from account_receivable.account_posting_history \
                               left join reservation.employee on employee.emp_id = account_posting_history.acc_user_id \
                               where invoice_id = '"+str(invoice_no)+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_SELECT_AccountPayHistory(request):
    
    invoice_no = request.json['account_no']

    result = json.loads(dbget("select payment_code.payment_code,payment_code.payment_type,account_pay_history.* \
                              from account_receivable.account_pay_history \
                              left join cashiering.payment_code on payment_code.payment_code_id = account_pay_history.payment_type_id \
                              where account_pay_history.account_no = '"+str(invoice_no)+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
