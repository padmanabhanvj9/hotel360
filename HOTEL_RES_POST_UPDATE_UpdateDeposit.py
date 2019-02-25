from sqlwrapper import gensql
import json
import datetime
from ApplicationDate import application_date


def HOTEL_RES_POST_UPDATE_UpdateDeposit(request):
    s = {}
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','Res_unique_id','deposit_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('Res_id','Res_unique_id','deposit_id')}

    print(e)
    sql_value = gensql('update','reservation.res_deposit',a,e)
    
    s = {}
    s['Emp_Id'] = "121"
    s['Emp_Firstname'] = "Admin"
    app_datetime = application_date()
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = "Deposit amount is"+"  "+d['RES_Deposit_Amount']
    s['RES_Description'] = 'deposit amount is paid'
    s['Res_id'] = d['Res_id']
    s['Res_unique_id'] = d['Res_unique_id']
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
