from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_AccountTraces(request):
    d = request.json
    f = { k : v for k,v in d.items() if v != ''}
   
    gensql('insert','account_receivable.account_traces',f)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))


def HOTEL_AR_POST_UPDATE_AccountTraces(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if k not in ('account_number')}
    print(a)
    e = { k : v for k,v in d.items() if k in ('account_number')}
    print(e)
    gensql('update','account_receivable.account_traces',a,e)
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_AR_POST_SELECT_AccountTraces(request):
    account_number = request.json['account_number']
    result = json.loads(dbget("select employee.emp_firstname, account_traces.* from account_receivable.account_traces \
                            left join reservation.employee on employee.emp_id = account_traces.created_by \
                            where account_traces.account_number = '"+str(account_number)+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_DELETE_AccountTraces(request):    
   account_traces_id = request.json['traces_id']
   print(account_traces_id)
   dbput(("delete from account_receivable.account_traces where account_traces_id = '"+account_traces_id+"' "))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                      'Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
