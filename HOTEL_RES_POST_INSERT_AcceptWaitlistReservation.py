from sqlwrapper import gensql, dbget,dbput
import datetime
import json
import random
def HOTEL_RES_POST_INSERT_AcceptWaitlistReservation(request):
    d = request.json

    id = d.get("Res_id")
    pf_id = d.get("pf_id")
    mobileno = dbget("select pf_mobileno from reservation.res_reservation \
                      where res_id = '"+id+"' and pf_id = '"+pf_id+"'")
    mobileno = json.loads(mobileno)
    print(mobileno[0]['pf_mobileno'],type(mobileno[0]['pf_mobileno']))
    
    mobile = mobileno[0]['pf_mobileno']
    mobile = str(mobile)
    mobile = mobile[0:3]
    mobile = str(mobile)
    random_no = (random.randint(1000000000,9999999999))
    random_no = str(random_no)
    random_no = random_no[0:4]
    print(random_no)
    conf = mobile + random_no
    print(mobile)
    RES_Confnumber = "PMS" + conf
    print(RES_Confnumber)
    t = {}
    t['RES_Confnumber'] = RES_Confnumber
    t['RES_Guest_Status'] = "Reserved"
    e = {}
    e['Res_id'] = id
    e['pf_id'] = pf_id
  
    sql_value = gensql('update','reservation.res_reservation',t,e)
    print(d)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    conf_number = t.get("RES_Confnumber")
    res_id = e.get("Res_id")
    Emp_Id = '121'
    Emp_Firstname = "Ranimangama"
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = "New Reservation"
    s['RES_Description'] = "Accept Waitlist Reservation & confirmation number is" +" "+ conf_number
    s['Res_id'] = res_id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':conf_number,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    

