from sqlwrapper import gensql,dbget
import json
import datetime
def HOTEL_RES_POST_INSERT_UpdateFixedRateReservation(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != ''}
    print(a)
    sql_value = gensql('insert','reservation.res_fixed_rate',a)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
	
def HOTEL_RES_POST_SELECT_QueryFixedRateReservation(request):
 try:
    d = request.json
    
    sql_value = json.loads(dbget("select * from reservation.res_fixed_rate \
                                  where res_id = '"+str(d['res_id'])+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
 except:
     return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':"No Record Available"  ,'ReturnCode':'RRTS'},indent=4))


def HOTEL_RES_POST_SELECT_QueryRateInfo(request):
    
    d = request.json
    e,list1,Total = {},[],0
    sql = json.loads(dbget("select res_arrival,res_depature,res_rate_code,res_rate from reservation.res_reservation \
                                where res_id = '"+str(d['res_id'])+"' and res_unique_id = '"+str(d['res_unique_id'])+"'"))
    print(sql)
    data1 = sql[0]['res_arrival']
    data2 = sql[0]['res_depature']
    date1 = datetime.datetime.strptime(data1, '%Y-%m-%d').date() 
    date2 = datetime.datetime.strptime(data2, '%Y-%m-%d').date() 
    day = datetime.timedelta(days=1)
    while date1 <= date2:
         print(date1.strftime('%Y-%m-%d'))
         
         
         Total += sql[0]['res_rate']
         days = date1.strftime("%A")
         list1.append({'Days':days,'Date':str(date1),'RateCode':sql[0]['res_rate_code'],'RoomRevenue':sql[0]['res_rate']})
         date1 = date1 + day
    print(list1,Total)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':list1 ,'StayTotal':Total,'ReturnCode':'RRTS'},indent=4))
