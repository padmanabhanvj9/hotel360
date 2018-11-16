from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_ARTransfer(request):
    
   From_account = request.json['From_account']
   Invoice_no = request.json['Invoice_no']
   To_aacount = request.json['To_aacount']

   sql = json.loads(dbget("select open_amount from \
                           account_receivable.accout_inivoice \
                           where account_number = '"+str(From_account)+"' and invoice_no = '"+str(Invoice_no)+"'"))
   print(sql)
   print(sql[0]['open_amount'],type(sql[0]['open_amount']))
   
   acc_set = dbput("update account_receivable.account_setup \
                   set account_balance = account_balance+"+str(sql[0]['open_amount'])+" \
                   where account_number = '"+str(To_aacount)+"'")
   print(acc_set)
   sql = dbput("update account_receivable.accout_inivoice \
                set account_number = '"+str(To_aacount)+"' \
                where account_number = '"+From_account+"' and invoice_no = '"+str(Invoice_no)+"' ")

   
   psql = dbput("update account_receivable.account_billing_post \
                set account_no = '"+str(To_aacount)+"' \
                where account_no = '"+str(From_account)+"' and invoice_no = '"+str(Invoice_no)+"'")
   
    
   return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))
