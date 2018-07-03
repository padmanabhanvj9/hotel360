from sqlwrapper import gensql, dbget
from flask import Flask,request, jsonify
import json
import datetime
def HOTEL_RES_POST_INSERT_ReinstateReservation(request):
    d = request.json
    s,e = {},{}
    
    res_id = d.get("res_id")
    res_unique_id = d.get("res_unique_id")

    #print(res_status)
    #print(res_status[0]['res_guest_status'],type(res_status[0]['res_guest_status']))
    e['res_id'] = res_id
    e['res_unique_id'] = res_unique_id
    s['res_guest_status'] = "reserved"
    
    #s['res_confnumber'] = res_confnumber[0]['res_confnumber']
    sql_value = gensql('update','reservation.res_reservation',s,e)
    print(sql_value)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    res_id = e.get("res_id")
    Emp_Id = '121'
    Emp_Firstname = "Daisy"
    conf_number = gensql('select','reservation.res_reservation','res_confnumber',e)
    conf_number = json.loads(conf_number)
    print(type(conf_number))
    print(conf_number[0]['res_confnumber'])
    confirmation_number = (conf_number[0]['res_confnumber'])
    print(confirmation_number)
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = "Reinstate Reservation"
    s['RES_Description'] = "Reinstate Reservation & and confirmation number is" + " " +confirmation_number
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':confirmation_number,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    

