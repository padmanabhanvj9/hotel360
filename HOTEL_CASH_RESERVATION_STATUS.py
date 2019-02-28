from sqlwrapper import gensql, dbget, dbput
import json
import datetime

from ApplicationDate import application_date

def HOTEL_CASH_RESERVATION_STATUS(request):
    
    d = request.json
    ac_log = {}
    app_datetime = application_date()
    RES_Log_Time = app_datetime[0]
    Posting_date = app_datetime[1]
    res_id = request.json['res_id']
    res_room = request.json['res_room']
    sql_value = json.loads(dbget("select reservation.res_reservation.res_guest_status from reservation.res_reservation where res_id="+res_id+" and res_room="+res_room+" "))
    

    balance = sql_value[0]['res_guest_status']

    if balance =="due out":
        status = "Check out"
        psql_value = dbput("update room_management.rm_room_list set rm_fo_status = 'vacant', \
                           rm_reservation_status = 'not reserved',rm_fo_person= '0',rm_room_status = 'Dirty' where rm_room = '"+str(res_room)+"' ")
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' where res_id="+res_id+" and res_room="+res_room+" ")
        ac_log['Emp_Id'] = '121'
        ac_log['Emp_Firstname'] = "Admin"
        ac_log['RES_Log_Date'] = Posting_date
        ac_log['RES_Log_Time'] = app_datetime[2]
        ac_log['RES_Action_Type'] = "Checkout Reservation"
        ac_log['RES_Description'] = "Reservation should be checkout.The room number is"+" "+str(res_room)
        ac_log['Res_id'] = str(res_id)
        sql_value = gensql('insert','reservation.res_activity_log',ac_log)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully',"ReturnCode":"RUS"}, sort_keys=True, indent=4))
    else:
        return(json.dumps({'Status':'Failure','Return':'Unable to update'}, sort_keys=True, indent=4))
    
    #return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    #return(json.dumps({'Balance': balance,'status':sql4}, sort_keys=True, indent=4))

def HOTEL_CASH_UpdateReinstateRervaiton(request):
    
    d = request.json
    ac_log = {}
    app_datetime = application_date()
    RES_Log_Time = app_datetime[0]
    Posting_date = app_datetime[1]
    res_id = request.json['res_id']
    res_room = request.json['res_room']
    sql_value = json.loads(dbget("select * from reservation.res_reservation \
                                  where res_id="+res_id+" and res_room="+res_room+" "))
    print(sql_value)

    balance = sql_value[0]['res_guest_status']
    print("res_room", res_room, type(res_room))
    if balance =="Check out":
        status = "due out"
        psql_value = dbput("update room_management.rm_room_list set rm_fo_status = 'occupied', \
                            rm_reservation_status = 'reserved',rm_fo_person= '"+str(sql_value[0]['res_adults'])+"'\
                            where rm_room = '"+str(res_room)+"' ")
        print("psql", psql_value)
        sql_value = dbput("update reservation.res_reservation set res_guest_status = '"+status+"' \
                           where res_id="+res_id+" and res_room="+res_room+" ")
        ac_log['Emp_Id'] = '121'
        ac_log['Emp_Firstname'] = "Admin"
        ac_log['RES_Log_Date'] = Posting_date
        ac_log['RES_Log_Time'] = app_datetime[2]
        ac_log['RES_Action_Type'] = "Due out Reservation"
        ac_log['RES_Description'] = "Reservation should be due out.The room number is"+" "+str(res_room)
        ac_log['Res_id'] = str(res_id)
        sql_value = gensql('insert','reservation.res_activity_log',ac_log)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully',"ReturnCode":"RUS"}, sort_keys=True, indent=4))
    else:
        return(json.dumps({'Status':'Failure','Return':'Unable to update'}, sort_keys=True, indent=4))
    
    
