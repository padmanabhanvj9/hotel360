from sqlwrapper import gensql,dbget
import json
import datetime

def QueryProfileHistoryRecord(request):
    d = request.json['pf_id']
    print(d)
    today = datetime.datetime.utcnow().date()
    print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and res_arrival < '"+str(today)+"' "))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

def QueryProfileStatistics(request):
    d = request.json['pf_id']
    #print(d)
    e = {}
    #today = datetime.datetime.utcnow().date()
    #print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' "))
    #print(sql_value)
    nights = 0
    rooms = 0
    for i in sql_value:
        nights += int(i['res_nights'])
        rooms += int(i['res_number_of_rooms'])
    print(nights,rooms)
    e['Room Nights'] = nights
    e['Arrival Rooms'] = rooms
    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':e  ,'ReturnCode':'RRTS'},indent=4))

def QueryProfileFutureRecord(request):
    d = request.json['pf_id']
    print(d)
    today = datetime.datetime.utcnow().date()
    print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and res_arrival > '"+str(today)+"' "))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

    
