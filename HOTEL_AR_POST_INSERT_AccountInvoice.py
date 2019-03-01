from sqlwrapper import gensql, dbget,dbput
from ApplicationDate import application_date
import datetime
import json
#fetch_date = application_date()
#print(fetch_date)
def HOTEL_AR_POST_INSERT_AccountInvoice(request):
    app_datetime = application_date()
    d = request.json
    Posting_date = app_datetime[1]
    select = json.loads(dbget("select * from account_receivable.invoice_no"))
    print(select,type(select),len(select))

    invoice_id = (select[0]['invoice_num']+1)
    print(invoice_id)
    update = dbput("update account_receivable.invoice_no set invoice_num = '"+str(select[0]['invoice_num']+1)+"'")
    d['invoice_no'] = invoice_id
    d['invoice_date'] = Posting_date
    d['invoice_amount'] = '0'
    d['open_amount'] = '0'
    d['acc_invoice_satus'] = 'UnCompress'
    gensql('insert','account_receivable.accout_inivoice',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200","invoice_num":invoice_id},indent=4))
def HOTEL_AR_POST_INSERT_Billingpost(request):
    app_datetime = application_date()
    Posting_date = app_datetime[1]
    result = request.json
    s ,amount= {},0
    d = result['bills']
    #print(d)
    sqlcount = json.loads(dbget("select account_balance, count(*) from account_receivable.account_setup where account_setup.account_number  = '"+str(d[0]['account_no'])+"' group by account_balance"))
    print(sqlcount)
    folio_no = json.loads(dbget("select account_setup.credit_limit, folio_no.* from account_receivable.folio_no,account_receivable.account_setup \
                              where account_setup.account_number = '"+str(d[0]['account_no'])+"'"))
    print(folio_no)
    for i in d:
        amount += int(i['Posting_amount'])
   # print(amount,amount + sqlcount[0]['sum'])
    if sqlcount[0]['count'] != 0:
      if folio_no[0]['credit_limit'] >= amount + sqlcount[0]['account_balance'] :
        for i in d:
        
                 i['Posting_date'] = Posting_date
                 i['folio_no'] = folio_no[0]['folio_num']+1
                 gensql('insert','account_receivable.account_billing_post',i)
                
                 psql = dbput("update account_receivable.accout_inivoice  \
                               set invoice_amount =invoice_amount+ '"+str(i['Posting_amount'])+"', open_amount =  open_amount+'"+str(i['Posting_amount'])+"' \
                               where invoice_no='"+str(i['invoice_no'])+"'")
                 print(psql)
                 
        folio_num = folio_no[0]['folio_num']+1
        dbput("update account_receivable.folio_no set folio_num = '"+str(folio_num)+"' ")
        #print(i['account_no'])
        acc = json.loads(dbget("select open_amount from account_receivable.accout_inivoice \
                                 where account_number = '"+str(i['account_no'])+"' and acc_invoice_satus not in ('Compress')"))

        print(acc)
       
            
     
        sumof =sum(item['open_amount'] for item in acc if item['open_amount'] is not None)
        acc_bala = dbput("update account_receivable.account_setup set account_balance = '"+str(sumof)+"' \
                                      where account_number = '"+str(i['account_no'])+"'")
        print(acc_bala)
        app_datetime = application_date()
        s['invoice_id'] = i['invoice_no']
        s['acc_action'] = "posting charges"
        s['acc_post_date'] = app_datetime[1]
        s['acc_posting_time'] = app_datetime[0]
        s['acc_user_id']  = i['emp_id']
        history = gensql('insert','account_receivable.account_posting_history',s)
        
        return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                           "Status": "Success","StatusCode": "200"},indent=4))
      else:
         return(json.dumps({"Return": "Record Invalid","ReturnCode": "RIV",
                           "Status": "Success","StatusCode": "200"},indent=4))
   
        
def HOTEL_AR_POST_SELECT_Billingpost(request):
    acc_no = request.json['account_no']
    invoice_no = request.json['invoice_no']
    result = json.loads(dbget("select package_code.package_code_id as posting_code,package_code.package_code as posting_code_description,account_billing_post.* from account_receivable.account_billing_post \
                                 left join packages.package_code on package_code.package_code_id = account_billing_post.post_code_id \
                                 where account_billing_post.account_no = '"+str(acc_no)+"' and account_billing_post.invoice_no = '"+str(invoice_no)+"' "))
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_SELECT_AccountInvoice(request):
    acc_no = request.json['account_no']
    result = json.loads(dbget("select account_setup.account_balance,market.marketgroup_description,res_source.sourcedescription,room_class.class,accout_inivoice.* from account_receivable.accout_inivoice \
                                left join reservation.market on market.id = accout_inivoice.market_id \
                                left join reservation.res_source on res_source.id = accout_inivoice.source_id \
                                left join room_management.room_class on room_class.id = accout_inivoice.room_class_id \
                                left join account_receivable.account_setup on account_setup.account_number  = accout_inivoice.account_number \
                                where accout_inivoice.account_number ='"+str(acc_no)+"'" ))

    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_AR_POST_UPDATE_AdjustBillingpost(request):
    d = request.json
    print(d)
    app_datetime = application_date()
    Posting_date = app_datetime[1]
    z= {}
    s = {}
    amount = json.loads(dbget("select posting_amount from account_receivable.account_billing_post \
                             where account_bill='"+str(d['account_bill'])+"' and account_no = '"+str(d['account_no'])+"'"))
    a = { k : v for k,v in d.items() if v != '' if k not in ('account_bill','invoice_no')}
    print(a)
    if a['adjust_type'] == 1:
        z['posting_amount'] = amount[0]['posting_amount'] + a['adjust_amount'] 
    elif a['adjust_type'] == 2:
        print("else")
        z['posting_amount'] = amount[0]['posting_amount'] *  a['adjust_amount'] / 100
    e = { k : v for k,v in d.items() if k != '' if k in ('account_bill','invoice_no')}
    print(e)
    print("adjust",z)
    gensql('update','account_receivable.account_billing_post',z,e)
    app_datetime = application_date()
    s['invoice_id'] = e['invoice_no']
    s['acc_action'] = a['reason_text']
    s['acc_posting_reason'] = a['reason_code']
    s['acc_post_date'] = Posting_date
    s['acc_posting_time'] = app_datetime[0]
    s['acc_user_id']  = d['emp_id']
    history = gensql('insert','account_receivable.account_posting_history',s)
    sql = json.loads(dbget("select sum(posting_amount) from account_receivable.account_billing_post where account_no = '"+str(d['account_no'])+"' \
                                                 and invoice_no = '"+d['invoice_no']+"'"))
    psql = dbput("update account_receivable.accout_inivoice  \
                   set invoice_amount = '"+str(sql[0]['sum'])+"', open_amount = '"+str(sql[0]['sum'])+"' \
                    where invoice_no='"+str(d['invoice_no'])+"'")
    acc = json.loads(dbget("select open_amount from account_receivable.accout_inivoice \
                            where account_number = '"+str(d['account_no'])+"' and acc_invoice_satus not in ('Compress')"))

    print(acc)
     
    sumof =sum(item['open_amount'] for item in acc if item['open_amount'] is not None)
    acc_bala = dbput("update account_receivable.account_setup set account_balance = '"+str(sumof)+"' \
                      where account_number = '"+str(d['account_no'])+"'")

    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))
def HOTEL_AR_POST_INSERT_Billingpayment(request):
    d = request.json
    #Posting_date = application_date([1])
    s = {}
    setup = json.loads(dbget("select account_balance from account_receivable.account_setup where account_number = '"+d['account_no']+"'"))
    setupamount = setup[0]['account_balance'] - d['posting_amount']
    print(setupamount)
    account_invoie = json.loads(dbget("select open_amount from account_receivable.accout_inivoice where account_number = '"+d['account_no']+"' and acc_invoice_satus not in ('Compress')"))
    acc_inv = account_invoie[0]['open_amount'] - d['posting_amount']
    print(acc_inv)
    app_datetime = application_date()
    d['posting_date'] = app_datetime[1]
    d['posting_status'] = "Apply Payment"
    gensql('insert','account_receivable.invoice_payment',d)
    sql = dbput("update account_receivable.account_setup set account_balance = '"+str(setupamount)+"' where account_number = '"+d['account_no']+"'")
    psql = dbput("update account_receivable.accout_inivoice set open_amount = '"+str(acc_inv)+"' where account_number = '"+d['account_no']+"'")
    s['account_no'] = d['account_no']
    s['payment_type_id'] = d['payment_code_id']
    s['post_date'] = app_datetime[1]
    s['payment_amount'] = d['posting_amount']
   
    gensql('insert','account_receivable.account_pay_history',s)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_AR_POST_UPDATE_AccountInvoice():
    
    print("sdjfksdh")
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('account_number')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('account_number')}
    print(e)
    gensql('update','account_receivable.accout_inivoice',a,e)
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))


#summmmaaaaaaaaaaaaaaaaaaaaaaaa
def HOTEL_AR_POST_DELETE_AccountInvoice(request):    
   account_number = request.json['account_number']
   print(account_number)
   Invoice_no = request.json['invoice_no']
   dbput(("delete from account_receivable.accout_inivoice where account_number = '"+account_number+"' and invoice_no = '"+Invoice_no+"'"))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                      'Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))


def HOTEL_AR_POST_INSERT_PostAccountInvoice(request):
    d  = request.json
    gensql('insert','account_receivable.bill_post',d)
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))
