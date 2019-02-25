from sqlwrapper import gensql, dbget, dbput
import json
import datetime
from ApplicationDate import application_date

def HOTEL_RES_POST_UPDATE_UpdateReservation(request):
    
    a = request.json
    print(a)
    
    d = { k : v for k,v in a.items() if v != '' if k not in ('res_id','pf_id','res_unique_id')}
    print(a)
    e = { k : v for k,v in a.items() if k != '' if k in ('res_id','pf_id','res_unique_id')}
    print(e)
    

    return updatereservation(d,e)

def updatereservation(d,e):
    sql_value = gensql('update','reservation.res_reservation',d,e)
    
    Emp_Id = '121'
    Emp_Firstname = "Admin"
    res_id = e.get("res_id")
    RES_Action_Type = "Update Reservation"
    values = d.values()
    print(values)
    RES_Description = ''
    for i in values:
       if  RES_Description == '':
           RES_Description +=  i 
       else:
           RES_Description +=  "|" + i
    print(RES_Description)
    
   
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    s['Res_id'] = res_id
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
