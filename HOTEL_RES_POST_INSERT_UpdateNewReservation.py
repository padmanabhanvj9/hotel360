import datetime
from sqlwrapper import gensql

import json


def HOTEL_RES_POST_INSERT_UpdateNewReservation(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_reservation',d)
    #print(d)
    data = d.get("PF_Firstname")
    print(data)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "daisy"
    
    RES_Action_Type = "new reservation"
    RES_Description = "create new reservation for " + " "+data
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    