
from datetime import datetime
from sqlwrapper import gensql, dbget
import json
from datetime import datetime,timedelta
def Hotel_RES_Post_Insert_UpdateGuestTraces(request):
    d = request.json
    e = { k:v for k,v in  d.items() if k not in ('traces_from_date','traces_to_date') }
   
    from_date = request.json['traces_from_date']
    to_date = request.json['traces_to_date']
    print(from_date,type(from_date))
    from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
    print(type(to_date))
    trace_date = []
    while from_date <= to_date :
        trace_date.append(from_date)
        from_date = from_date+timedelta(days=1)
    print(trace_date)
    for i in trace_date:
        e['traces_date'] = i
        e['res_traces_status'] = 'Unresloved'
        e['turndown_status'] = 'Requested'
        sql_value = gensql('insert','reservation.res_traces',e)
        
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def Hotel_RES_Post_Update_UpdateGuestTraces(request):
    d = request.json
    #todaydate = datetime.datetime.utcnow().date()
    #print(todaydate)

    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','res_unique_id','traces_id')}
    #print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','res_unique_id','traces_id')}
    #print(e)
    sql_value = gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def Hotel_RES_Get_Select_QueryGuestTraces():

    sql_value = json.loads(dbget("select * from reservation.res_reservation join reservation.res_traces on \
                           reservation.res_reservation.res_unique_id = reservation.res_traces.res_unique_id") )
    #sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


