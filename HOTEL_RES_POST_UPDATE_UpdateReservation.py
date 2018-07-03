
from sqlwrapper import gensql, dbget, dbput

import json
import datetime

def HOTEL_RES_POST_UPDATE_UpdateReservation(request):
    RM_Queue_Date = datetime.datetime.utcnow().date()
    print(RM_Queue_Date)
    RM_Queue_Date = str(RM_Queue_Date)

    a = request.json
    print(a)
    
    d = { k : v for k,v in a.items() if v != '' if k not in ('res_id','pf_id','res_unique_id')}
    print(a)
    e = { k : v for k,v in a.items() if k != '' if k in ('res_id','pf_id','res_unique_id')}
    print(e)
    
    '''data = e.get('PF_Mobileno')
    print(data)
    sql_value = dbget("select count(*) from room_management.rm_queue_room where pf_mobileno = "+data+"")
    print(sql_value)
    
    s = ['PF_Firstname','PF_Mobileno','RM_Queue_Date']
    sql_value = gensql('select','room_management.rm_queue_room',s,e)
    sql_value = json.loads(sql_value)
    print(sql_value)
   

    if sql_value !=0:
         sql = ("delete from room_management.rm_queue_room where  PF_Mobileno = "+data+" and rm_queue_date = '"+RM_Queue_Date+"'")
         print(sql)             
         dbput(sql)
         return updatereservation(d,e)
    else:
        return updatereservation(d,e)'''
    return updatereservation(d,e)

def updatereservation(d,e):
    sql_value = gensql('update','reservation.res_reservation',d,e)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "Daisy"
    res_id = e.get("res_id")
    RES_Action_Type = "Update Reservation"
    values = d.values()
    print(values)
    RES_Description = ''
    for i in values:
       if  RES_Description == '':
           RES_Description +=  i 
       else:
           RES_Description +=  "|" + i
    print(RES_Description)
    
   
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
   
    s['RES_Log_Date'] = RES_Log_Date
    s['RES_Log_Time'] = RES_Log_Time
    s['RES_Action_Type'] = RES_Action_Type
    s['RES_Description'] = RES_Description
    s['Res_id'] = res_id
    sql_value = gensql('insert','reservation.res_activity_log',s)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
