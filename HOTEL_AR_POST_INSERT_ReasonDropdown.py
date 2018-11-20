from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_Account_typeDropdown(request):
    d = request.json
    
    gensql('insert','account_receivable.account_type',d)

    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))
def HOTEL_AR_POST_SELECT_Account_typeDropdown(request):
    
    result = json.loads(dbget("select * from account_receivable.account_type"))

    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))



def HOTEL_AR_POST_INSERT_REASONDropdown(request):
     d = request.json
    
     gensql('insert','account_receivable.account_reason',d)
     
     return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_AR_POST_SELECT_REASONDropdown(request):
     
     result = json.loads(dbget("select * from account_receivable.account_reason"))

     return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))


def HOTEL_AR_POST_SELECT_InvoicePaymentDropdown(request):
     
     result = json.loads(dbget("select * from account_receivable.invoice_payment_type"))

     return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
    
def HOTEL_AR_POST_SELECT_AccountTypeDropdown(request):
     
     result = json.loads(dbget("select * from account_receivable.account_type"))

     return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_INSERT_InvoicePaymentDropdown(request):
     d = request.json
    
     gensql('insert','account_receivable.invoice_payment_type',d)
     
     return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))

