import datetime
#from datetime import datetime,timedelta
from sqlwrapper import gensql, dbget,dbput
import json
from collections import Counter
def Hotel_RES_Post_Update_TracesResloved(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','res_unique_id','traces_id')}
    #print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','res_unique_id','traces_id')}
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    a['resloved_by'] = "Daisy"
    a['resloved_on'] = RES_Log_Date
    a['res_traces_status'] = 'Resloved'
    a['turndown_status'] = 'Completed'
    sql_value = gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

   
def Hotel_RES_Post_Delete_RemoveTraces(request):
    d = request.json
    sql_value = dbput("delete from reservation.res_traces \
                      where traces_id = '"+str(d['traces_id'])+"' and res_id = '"+str(d['res_id'])+"'")
    return(json.dumps({'Status':'Success','Statuscode':'200','Return':'Record Deleted Successfully','Returncode':'RDS'},indent=4))

def Hotel_RES_Post_Select_PropertyCalendar(request):
    
    d = request.json
    e ,list1,list2,final_value,list3= {},[],[],[],[]
    
    sql_value = json.loads(dbget("select res_arrival from reservation.res_reservation "))
    for i in sql_value:
        list1.append(i['res_arrival'])
    
    #psql = json.loads(dbget("select res_room_type from reservation.res_reservation \
     #                           where res_arrival between '2018-07-01' and '2018-08-09'"))
    #list3.append(psql)
    #print(list3)
    #print(Counter(list1))
    #listofvalue = Counter(list1)
    #print(Counter(list1).keys())
    #print(Counter(list1).values())
    for K,V in Counter(list1).items():
        #print(K)
        list2.append({'date':K,'value':V})
    final_value = sorted(list2,key=lambda i :i['date'])
    psql = json.loads(dbget("select count(res_room_type) from reservation.res_reservation"))
    print(psql)
    return(json.dumps({'Status':'Success','Statuscode':'200','Return':'Record Retrieved successfully','Returnvalue':final_value},indent=4))
