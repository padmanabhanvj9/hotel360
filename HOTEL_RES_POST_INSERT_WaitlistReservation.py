from sqlwrapper import gensql, dbget,dbput
import datetime
import json
from ApplicationDate import application_date

def HOTEL_RES_POST_INSERT_WaitlistReservation(request):
    d = request.json
    d = { k : v for k,v in d.items() if  v != ''}
    
    Emp_Id = '121'
    Emp_Firstname = "Admin"
    app_datetime = application_date()
    d['created_on'] = app_datetime[1]
    d['created_by'] = Emp_Firstname
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    d['Res_id'] = Res_id
    d['RES_Guest_Status'] = "waitlist"
    number_of_rooms = d.get("RES_Number_Of_Rooms")
    number_of_rooms = int(number_of_rooms)
    print(number_of_rooms,type(number_of_rooms))
    for number in range(number_of_rooms):
        d['RES_Number_Of_Rooms'] = str(1)
        sql_value = gensql('insert','reservation.res_reservation',d)
        print(sql_value)
    print(d)
 
    name = d.get("PF_Firstname")
    res_id = d.get("Res_id")
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    app_datetime = application_date()
    s['RES_Log_Date'] = app_datetime[1]
    s['RES_Log_Time'] = app_datetime[2]
    s['RES_Action_Type'] = "Waitlist Reservation"
    s['RES_Description'] = "Reservation for" +" "+ name+" "+"with number of rooms"+" "+str(number_of_rooms)+" "+" is in waitlist"
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Resord Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
