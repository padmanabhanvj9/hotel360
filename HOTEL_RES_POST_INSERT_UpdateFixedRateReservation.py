from sqlwrapper import gensql,dbget
import json


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
