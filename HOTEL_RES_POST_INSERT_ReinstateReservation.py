from sqlwrapper import gensql, dbget,dbput
from flask import Flask,request, jsonify
import json
import datetime
from ApplicationDate import application_date


def HOTEL_RES_POST_INSERT_ReinstateReservation(request):
    d = request.json
    s,e = {},{}
    
    res_id = d.get("res_id")
    res_unique_id = d.get("res_unique_id")
    initial=datetime.datetime.strptime(d['RES_Depature'], '%Y-%m-%d').date()
    depature_minus = initial - datetime.timedelta(days=1)
    booking_count = json.loads(dbget("select sum(available_count) from room_management.room_available where rm_room= '"+str(d['RES_Room_Type'])+"'\
                                  and rm_date between '"+str(d['RES_Arrival'])+"' and '"+str(depature_minus)+"'"))
    if booking_count[0]['sum'] == 0 or booking_count[0]['sum'] < int(d['RES_Number_Of_Rooms']):
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Booking is Not Available','ReturnCode':'BNA'}, sort_keys=True, indent=4)) 
    bookedcount = dbput("update room_management.room_available set available_count=available_count - \
                            '1', \
                            booked_count = booked_count + '1' where rm_room = \
                            '"+str(d['RES_Room_Type'])+"' and \
                            rm_date between '"+str(d['RES_Arrival'])+"' and '"+str(depature_minus)+"' ")
                 
    #print(res_status)
    #print(res_status[0]['res_guest_status'],type(res_status[0]['res_guest_status']))
    e['res_id'] = res_id
    e['res_unique_id'] = res_unique_id
    s['res_guest_status'] = "reserved"
    
    #s['res_confnumber'] = res_confnumber[0]['res_confnumber']
    sql_value = gensql('update','reservation.res_reservation',s,e)
    print(sql_value)

    res_id = e.get("res_id")
    Emp_Id = '121'
    Emp_Firstname = "Admin"
    conf_number = gensql('select','reservation.res_reservation','res_confnumber',e)
    conf_number = json.loads(conf_number)
    print(type(conf_number))
    print(conf_number[0]['res_confnumber'])
    confirmation_number = (conf_number[0]['res_confnumber'])
    print(confirmation_number)
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    app_datetime = application_date()
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = "Reinstate Reservation"
    s['RES_Description'] = "Reinstate Reservation & and confirmation number is" + " " +confirmation_number
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':confirmation_number,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    

