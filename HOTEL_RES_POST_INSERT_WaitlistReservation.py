from sqlwrapper import gensql, dbget,dbput
import datetime
import json

def HOTEL_RES_POST_INSERT_WaitlistReservation(request):
    d = request.json
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "Ranimangama"
    d['created_on'] = RES_Log_Date
    d['created_by'] = Emp_Firstname
    select = json.loads(dbget("select * from reservation.res_id"))
    print(select,type(select),len(select))
    print(select[0]['id'])
    Res_id = (select[0]['id']+1)
    print(Res_id)
    update = dbput("update reservation.res_id set id = '"+str(select[0]['id']+1)+"'")
    d['Res_id'] = Res_id
    d['RES_Guest_Status'] = "Waitlist"
    sql_value = gensql('insert','reservation.res_reservation',d)
    print(d)
 
    name = d.get("PF_Firstname")
    res_id = d.get("Res_id")
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = "Waitlist Reservation"
    s['RES_Description'] = "Waitlist Reservation for" +" "+ name
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
    
