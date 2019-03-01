from sqlwrapper import gensql, dbget, dbput
from flask import Flask,request, jsonify
import json
import datetime
from ApplicationDate import application_date

def HOTEL_RES_POST_INSERT_CancelReservation(request):
    d = request.json
    z = {k : v for k,v in d.items() if k not in ('Res_Arrival','Res_Depature','Res_Room_Type')}
    sql_value = gensql('insert','reservation.cancel_reservation',z)
    Res_id = d.get("Res_id")
    Res_unique_id = d.get("Res_unique_id")
    e,a = {},{}
    e['Res_id'] = Res_id
    e['Res_unique_id'] = Res_unique_id
    a['Res_guest_status'] = "cancel"
    sql_value = gensql('update','reservation.res_reservation',a,e)
    print(sql_value)
    initial=datetime.datetime.strptime(d['Res_Depature'], '%Y-%m-%d').date()
    depature_minus = initial - datetime.timedelta(days=1)
    
    bookedcount = dbput("update room_management.room_available set available_count=available_count + '1',\
                            booked_count = booked_count - '1' where rm_room = \
                            '"+str(d['Res_Room_Type'])+"' and \
                            rm_date between '"+str(d['Res_Arrival'])+"' and '"+str(depature_minus)+"' ")
    
    res_id = e.get("Res_id")
    Emp_Id = '121'
    Emp_Firstname = "Admin"

    
    select = json.loads(dbget("select * from reservation.cancel_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    cancel_id = str(select[0]['id']+1)
    print(cancel_id)
    update = dbput("update reservation.cancel_id set id = '"+str(select[0]['id']+1)+"'")
    
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    app_datetime = application_date()
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = "Cancel Reservation"
    s['RES_Description'] = "cancellation Number is" +" "+ cancel_id
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','cancellationNumber':cancel_id,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
