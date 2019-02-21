from sqlwrapper import gensql,dbget,dbput
import json
import datetime
def HOTEL_RES_POST_INSERT_UpdateDeposit(request):
    
    s,a = {},{}
    d = request.json
    status = json.loads(dbget("SELECT res_guest_status FROM reservation.res_reservation \
                               where res_unique_id='"+d['Res_unique_id']+"' and res_id='"+d['res_id']+"'"))

    if status[0]['res_guest_status'] in ('checkin','checkout','due out'):
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Can not Deposit. Reservation checked-in','ReturnCode':'CND'}, sort_keys=True, indent=4))
    a = {k : v for k,v in d.items() if v != '' }
    print(d['res_id'],type(d['res_id']))
    sql_value = gensql('insert','reservation.res_deposit',a)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    #RES_Log_Date = datetime.datetime.utcnow().date()
    if d['RES_Deposit_Amount']  == '':
        pass
    else:
        s = {}
        s['Emp_Id'] = "121"
        s['Emp_Firstname'] = "Ranimangama"
        s['RES_Log_Date'] = datetime.datetime.utcnow().date()
        s['RES_Log_Time'] = RES_Log_Time
        s['RES_Action_Type'] = "Deposit amount is"+"  "+d['RES_Deposit_Amount']
        s['RES_Description'] = 'deposit amount is paid'
        s['Res_id'] = d['res_id']
        s['Res_unique_id'] = d['Res_unique_id']
        sql_value = gensql('insert','reservation.res_activity_log',s)


    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

	
def HOTEL_RES_POST_SELECT_QueryDeposit(request):
    d = request.json
    sql_value = gensql('select','reservation.res_deposit','*',d)
    sql_value1 = json.loads(sql_value)
    print(sql_value1)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value1  ,'ReturnCode':'RRTS'},indent=4))

   
