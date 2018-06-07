import datetime
from sqlwrapper import gensql
import random
import json


def HOTEL_RES_POST_INSERT_UpdateNewReservation(request):
    d = request.json
    random_no = (random.randint(1000000000,9999999999))
   
    random_no = str(random_no)
    random_no = random_no[0:4]
    print(random_no)
    mobile = d.get("PF_Mobileno")
    mobile = mobile[0:3]
    mobile = str(mobile)
    conf = mobile + random_no
    print(mobile)
    RES_Confnumber = "PMS" + conf
    print(RES_Confnumber)
    #RES_Confnumber = int(RES_Confnumber)
    d['RES_Confnumber'] = RES_Confnumber
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
    Emp_Firstname = "Ranimangama"
    
    RES_Action_Type = "New Reservation"
    RES_Description = "create new reservation for " + " "+data
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','Confirmation Number':RES_Confnumber,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
