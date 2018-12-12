from sqlwrapper import gensql, dbget
import json
import datetime
from collections import Counter
def Hotel_RM_Post_SELECT_OccupancyGraph(request):
   
   
    d = request.json
    e ,list1,list2,final_value,list3= {},[],[],[],[]


    psql = json.loads(dbget(" SELECT * FROM generate_series('2018-08-01', '2018-08-30', interval '1 day') AS dates \
                                WHERE dates NOT IN (SELECT res_arrival FROM reservation.res_reservation)"))

    sql_value = json.loads(dbget("select res_arrival,res_number_of_rooms from reservation.res_reservation \
                                  where res_arrival between '2018-08-01' and   '2018-08-30' "))
    print(sql_value)
    #sql_value = json.loads(dbget("select res_arrival from reservation.res_reservation \
     #                               where res_arrival between  '2018-08-05' and   '2018-08-09' \
      #                              union all \
         #                           select res_depature from reservation.res_reservation \
           #                         where res_depature between  '2018-08-05' and   '2018-08-09'"))
    for i in sql_value:
        list1.append(i['res_arrival'])
    

    for K,V in Counter(list1).items():
        #print(K)
        list2.append({'date':K,'value':V})
    for q in psql:
        print(q['dates'])
        gen_date = datetime.datetime.strptime(q['dates'],'%Y-%m-%d %H:%M:%S+%f:00').date()
        print(gen_date)
        list2.append({'date':str(gen_date.strftime('%Y-%m-%d')),'value':0})
    final_value = sorted(list2,key=lambda i :i['date'])

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final_value  ,'ReturnCode':'RRTS'},indent=4))


def Hotel_RM_Post_SELECT_FacilityForecast(request):
    d = request.json
    list1,list2,checklist ,checklist1= [],[],[],[]
    day = datetime.timedelta(days=1)
    plusdate = datetime.timedelta(days=6)
    date1 = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date() 
    date2 = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date()
    date2 = date2 + plusdate
         
   
    sql_value = json.loads(dbget("select res_depature from reservation.res_reservation \
                                      where res_depature  between '"+str(date1)+"' and '"+str(date2)+"' "))
    
    for i in sql_value:
        list1.append(i['res_depature'])
    for K,V in Counter(list1).items():
        #print(K)
        checklist.append(K)
        list2.append({'date':K,'value':V})
    print(checklist)
   
        
    while  date1 <= date2:
            #days = date1.strftime("%A")
            #dbdate = datetime.datetime.strptime(s['date'], '%Y-%m-%d').date()
            
            if str(date1) not in checklist:
                checklist1.append(date1)
            #print(date1.strftime('%Y-%m-%d'))
            date1 = date1 + day
            #days = date1.strftime("%A")
    print(checklist1)
    for s in checklist1:
        list2.append({'date':str(s),'value':0})
    final_value = sorted(list2,key = lambda x: x['date'] )
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final_value  ,'ReturnCode':'RRTS'},indent=4))

