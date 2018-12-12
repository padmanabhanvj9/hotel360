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

    list1 ,faclity,list2,arrival = [],{},[],[]
    date1 = datetime.datetime.strptime(d['start_date'], '%Y-%m-%d').date() 
    date2 = date1 + datetime.timedelta(days=6)

    sql_value = json.loads(dbget("select res_arrival,res_depature,res_adults,res_child,res_number_of_rooms from reservation.res_reservation \
                                      where res_arrival between   '"+str(date1)+"' and '"+str(date2)+"' \
				    and res_depature between   '"+str(date1)+"' and '"+str(date2)+"' \
				    order by res_arrival,res_depature "))
    print(sql_value)
    arrival_count = 0
    print(Counter([i['res_arrival'] for i in sql_value]))
    def arrival_and_dep_rooms(date1,name):
        #print('name',name)
        arrival = [v for k,v in Counter([i[""+name+""] for i in sql_value if i[""+name+""]==str(date1)]).items()]
        return (arrival[0] if len(arrival)!=0 else 0)

    def inhouse(date1):
        inhouse_count = sum([ i['res_adults'] for i in sql_value if datetime.datetime.strptime(i['res_arrival'], '%Y-%m-%d').date()== date1
                                                             or date1 in datetime.datetime.strptime(i['res_depature'], '%Y-%m-%d').date()])
        return(inhouse_count)
    
    while  date1 <= date2:
         list2.append({'date':str(date1),'values':{'arrival_rooms':arrival_and_dep_rooms(date1,name='res_arrival'),
                                                   'depature_rooms':arrival_and_dep_rooms(date1,name='res_depature'),
                                                   'adult_inhouse':inhouse(date1),
                                                   'child_inhouse':""}})
         date1 = date1 + datetime.timedelta(days=1)
    #print(list2)
    '''
    list1 = [{'date':k,'depature_rooms':v} for k,v in Counter([i['res_depature'] for i in sql_value]).items()]
    print(list1)
    list1_date = [i['date'] for i in list1]
    while  date1 <= date2:           
        if str(date1) not in list1_date:
           list1.append({'date':str(date1),'depature_rooms':0})      
        date1 = date1 + datetime.timedelta(days=1)
               
    final_value = sorted(list1,key = lambda x: x['date'] )
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':final_value  ,'ReturnCode':'RRTS'},indent=4))
    '''
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list2  ,'ReturnCode':'RRTS'},indent=4))
