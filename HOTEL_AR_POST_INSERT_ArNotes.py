from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_AR_POST_INSERT_ArNotes(request):
    d = request.json
    print(d)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)

    d['modified_on'] =  RES_Log_Time
  
    gensql('insert','account_receivable.ar_notes',d)
    
    return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                       "Status": "Success","StatusCode": "200"},indent=4))


def HOTEL_AR_POST_UPDATE_ArNotes(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('account_number')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('account_number')}
    print(e)
    gensql('update','account_receivable.ar_notes',a,e)
    return(json.dumps({"Return": "Record Updated Successfully","ReturnCode": "RUS",
                       "Status": "Success","StatusCode": "200"},indent=4))

def HOTEL_AR_POST_SELECT_ArNotes(request):
    result = json.loads(dbget('select employee.emp_firstname, ar_notes.* from account_receivable.ar_notes \
                                left join reservation.employee on employee.emp_id = ar_notes.modified_by'))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                       'ReturnValue': result  ,'ReturnCode':'RRTS'},indent=4))

def HOTEL_AR_POST_DELETE_ArNotes(request):    
   account_number = request.json['account_number']
   print(account_number)
   dbput(("delete from account_receivable.ar_notes where account_number = '"+account_number+"' "))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200',
                      'Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
