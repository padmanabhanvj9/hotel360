import datetime
from sqlwrapper import gensql, dbget, dbput
import random
import json


def HOTEL_RES_POST_INSERT_UpdateNewReservation(request):
    d = request.json
    PF_Mobileno = str(d.get("PF_Mobileno"))
    print(PF_Mobileno)
    RES_Arrival = str(d.get("RES_Arrival"))
    print(RES_Arrival)
    RES_Depature = str(d.get("RES_Depature"))
    sqlcount = ("select count(*) from reservation.res_reservation \
                 where pf_mobileno = '"+PF_Mobileno+"' and RES_Arrival = '"+RES_Arrival+"' and RES_Depature = '"+RES_Depature+"'")
    countdata = dbget(sqlcount)
    countdata = json.loads(countdata)
    print(countdata)
    print(countdata[0]['count'],type(countdata[0]['count']))

    if countdata[0]['count'] > 0:
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Reservation Already Exist','ReturnCode':'RAE'}, sort_keys=True, indent=4)) 

    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "Ranimangama"
    d['created_on'] = RES_Log_Date
    d['created_by'] = Emp_Firstname
    
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
    d['RES_Confnumber'] = RES_Confnumber
    d['RES_Guest_Status'] = "Reserved"
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    d['Res_id'] = Res_id
  
    sql_value = gensql('insert','reservation.res_reservation',d)
    print(d)
    data = d.get("PF_Firstname")
    number = d.get("RES_Confnumber")
    t = {}
    t['RES_Confnumber'] = number
    reservation_id = gensql('select','reservation.res_reservation','res_id',t)
    reservation_id = json.loads(reservation_id)
    print(reservation_id[0]['res_id'],type(reservation_id[0]['res_id']))
    reservation_id = reservation_id[0]['res_id']

    print(data)
    
    
    RES_Action_Type = "New Reservation"
    RES_Description = "create new reservation for " + " "+data+" " + "Confirmation Number is" + " " + number
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    s['Res_id'] = reservation_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':RES_Confnumber,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
