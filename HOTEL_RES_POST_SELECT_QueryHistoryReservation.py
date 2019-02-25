from sqlwrapper import dbget
import json
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_SelectRatesetupAll
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_GetRatecodeSetup
from datetime import datetime, timedelta
import requests
from ApplicationDate import application_date


def HOTEL_RES_POST_select_Paticularreservation(request):
    d = request.json
    result = json.loads(dbget("select * from reservation.res_reservation \
         where res_id = '"+str(d['res_id'])+"' and res_unique_id = '"+str(d['res_unique_id'])+"' "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
def QueryHistoryReservation(request):
    #N = 365
    app_datetime = application_date()
    current_date = app_datetime[1]
    print(current_date)

    pf_id = request.json['pf_id']
    sql_value = "select * from reservation.res_reservation where pf_id = '"+pf_id+"' and res_arrival <  '"+current_date+"' order by res_arrival desc"
    result = dbget(sql_value)
    #sql_value = gensql('select','reservation.res_reservation','*' 'ORDER BY res_arrival DESC')
    result = json.loads(result)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))

def get_rate(s):
    if s == 4:
        return('four_adult_rate')
    elif s == 3:
        return('three_adult_rate')
    elif s == 2:
        return('two_adult_rate')
    elif s == 1:
        return('one_adult_rate')
        
def HOTEL_RES_POST_SELECT_RateQuery(request):
    
     s = request.json
     rate_code ,ratecode_rooms_id,ratecode_packages_id,result= [],[],[],[]
     if s['com_pf_id'] == '': 
        data = json.loads(HOTEL_REM_POST_SELECT_SelectRatesetupAll(request))
     else:
         print("profile_id", s['com_pf_id'])
         pf_ids = json.loads(dbget("select ratecode.ratecode_id,pf_negotiated_rate.pf_rate_code \
                                    from profile.pf_negotiated_rate join revenue_management.ratecode \
                                    on pf_negotiated_rate.pf_rate_code = ratecode.rate_code\
                                    where pf_negotiated_rate.pf_id='"+s['com_pf_id']+"'"))
         
         print("pf_ids: ", pf_ids, type(pf_ids))
         if len(pf_ids) == 0:
             return(json.dumps({"Return":"Negotiated Code is not present for this pfofile","Return_code":"RNP"
                                ,"Status": "Success","StatusCode": "200"},indent=4))
         ids = str([''+str(pf['ratecode_id'])+'' for pf in pf_ids])[1:-1]
         print(ids, type(ids))
         data = json.loads(HOTEL_REM_POST_SELECT_GetRatecodeSetup(ids))
         
     print("data",data)
     
     list_roomtypes = [ r['r_type'] for r in json.loads(dbget("SELECT type as r_type \
                                                               FROM room_management.room_type"))]
     print("list_roomtypes",list_roomtypes)
     records = data['records']
     new_records = []
     #result = [d for d in value[0]['rate_details'] if d['start_date'] <= s['arrival_date'] and d['end_date'] >= s['departure_date']]
     for record in records:
             new_record = {}
             new_record['rate_code'] = record['rate_code']
             #new_records.append(new_record)
             for detail in record['rate_details']:
                 
                if detail['start_date'] >= s['arrival_date'] or detail['end_date'] <= s['departure_date']:
                    
                    new_record['rates'] = [dict(rm, rate=detail['advanced_details'][get_rate(s['adults'])]) for rm in detail['rooms']]

                    new_rooms = [] 
                    for r_type in new_record['rates']:
                            new_rooms.append(r_type['roomstype'])
                            
                    for list1 in list_roomtypes:
                        if list1 in new_rooms:
                            pass
                        else:
                            new_record['rates'].append({'roomstype':list1,'rate':0})
                          
             new_records.append(new_record)
             
     for i in new_records:
       if 'rates' in i:
            print('success')
            i['rates'] = sorted(i['rates'],key = lambda x: x['roomstype'] )          
     return(json.dumps({"Return": new_records,"Status": "Success","StatusCode": "200"},indent=4))
