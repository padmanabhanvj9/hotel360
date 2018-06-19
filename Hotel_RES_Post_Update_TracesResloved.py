import datetime
#from datetime import datetime,timedelta
from sqlwrapper import gensql, dbget
import json
def Hotel_RES_Post_Update_TracesResloved(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','traces_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','traces_id')}
    print(e)
    a['traces_status'] = "resloved"
    sql_value = gensql('update','reservation.res_traces',a,e)
    res_id = e.get("res_id")
    traces_id = e.get("traces_id")
    sql = dbget("select traces_dept_code from reservation.res_traces where res_id = '"+res_id+"' and traces_id = '"+traces_id+"'")
    sql = json.loads(sql)
    department = sql[0]['traces_dept_code']
    print(department)
    psql = dbget("select pf_firstname from reservation.res_reservation where res_id = '"+res_id+"'")
    psql = json.loads(psql)
    name = psql[0]['pf_firstname']
    print(name)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    
    s = {}
    s['pf_firstname'] = name
    s['emp_id'] = "121"
    s['traces_log_time'] = RES_Log_Time
    s['traces_log_date'] = RES_Log_Date
    s['traces_department'] = department
    s['traces_resloved_on'] = RES_Log_Date
    s['traces_resloved_by'] = "Aravinth"
    sql_value = gensql('insert','reservation.traces_activity',s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

   
