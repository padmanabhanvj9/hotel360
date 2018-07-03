from sqlwrapper import gensql, dbget, dbput
from flask import Flask,request, jsonify
import json
import datetime
def HOTEL_RES_POST_INSERT_CancelReservation(request):
    d = request.json
    sql_value = gensql('insert','reservation.cancel_reservation',d)
    Res_id = d.get("Res_id")
    Res_unique_id = d.get("Res_unique_id")
    e,a = {},{}
    e['Res_id'] = Res_id
    e['Res_unique_id'] = Res_unique_id
    a['Res_guest_status'] = "cancel"
    sql_value = gensql('update','reservation.res_reservation',a,e)
    print(sql_value)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    res_id = e.get("Res_id")
    Emp_Id = '121'
    Emp_Firstname = "Daisy"

    select = json.loads(dbget("select * from reservation.cancel_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    cancel_id = str(select[0]['id']+1)
    print(cancel_id)
    update = dbput("update reservation.cancel_id set id = '"+str(select[0]['id']+1)+"'")
    

    
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = "Cancel Reservation"
    s['RES_Description'] = "cancellation Number is" +" "+ cancel_id
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','cancellationNumber':cancel_id,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
