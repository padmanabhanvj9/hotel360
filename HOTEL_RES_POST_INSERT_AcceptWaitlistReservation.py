from sqlwrapper import gensql, dbget,dbput
import datetime
import json
import random
def HOTEL_RES_POST_INSERT_AcceptWaitlistReservation(request):
    d = request.json

    id = d.get("Res_id")
    pf_id = d.get("pf_id")
    res_unique_id = d.get("Res_unique_id")
    res_unique_id  = res_unique_id.split(',')
    res_unique_id = str(res_unique_id)[1:-1]
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

    res_confnumber = RES_Confnumber
    res_guest_status = "reserved"
    sql_value = dbput("update reservation.res_reservation set res_Confnumber = '"+res_confnumber+"',res_guest_status = '"+res_guest_status+"' \
                       where res_id = '"+id+"' and pf_id = '"+pf_id+"' and res_unique_id in("+res_unique_id+") ")
    print(d)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
  
    Emp_Id = '121'
    Emp_Firstname = "Ranimangama"
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = "New Reservation"
    s['RES_Description'] = "Reservation for "+id+" "+"is changed from waitlist to reserved status and the confirmation number is "+ res_confnumber
    s['Res_id'] = id
    
    sql_value = gensql('insert','reservation.res_activity_log',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ConfirmationNumber':res_confnumber,'ReturnCode':'RIS'}, sort_keys=True, indent=4))
    

