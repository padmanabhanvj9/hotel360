from sqlwrapper import dbget
import json
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_SelectRatesetupAll
from datetime import datetime, timedelta
import requests
#@app.route("/ProfileFutureReservationRecord",methods=['POST'])
def HOTEL_RES_POST_select_Paticularreservation(request):
    d = request.json
    result = json.loads(dbget("select * from reservation.res_reservation \
         where res_id = '"+str(d['res_id'])+"' and res_unique_id = '"+str(d['res_unique_id'])+"' "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
def QueryHistoryReservation(request):
    #N = 365
    current_date = datetime.utcnow().date()
    current_date = str(current_date)
    print(current_date)
    #date_N_days_ago = current_date + timedelta(days=1)
    #date_N_days_ago = date_N_days_ago.date()

    #date_N_days_ago = str(date_N_days_ago)
    #print (date_N_days_ago)
    pf_id = request.json['pf_id']
    sql_value = "select * from reservation.res_reservation where pf_id = '"+pf_id+"' and res_arrival <  '"+current_date+"' order by res_arrival desc"
    result = dbget(sql_value)
    #sql_value = gensql('select','reservation.res_reservation','*' 'ORDER BY res_arrival DESC')
    result = json.loads(result)
    print(result)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_RES_POST_SELECT_RateQuery(request):
     s = request.json
     rate_code = []
     #query = requests.post("https://hotel360.herokuapp.com/HOTEL_REM_POST_SELECT_SelectRatesetupAll")
     data = json.loads(HOTEL_REM_POST_SELECT_SelectRatesetupAll(request))
     #print(data)
     #print(type(data['Rate_header']))
     rate_details = data['Rate_details']
     
     value = data['Rate_header']
     result = [d for d in value if d['begin_sell_date'] >= s['arrival_date'] and d['end_sell_date'] <= s['departure_date']]
     #print(type(result))
     #print(result)
     for results in result:
       #print("results['rooms_id']",results['rooms_id'])
       a, b = [],[]
       for roomtype in data['Rate_details_room_types']:
           for package in data['Rate_header_packages']:

             if roomtype['rooms_id'] == results['rooms_id']:

               a.append(roomtype)
             if package['packages_id'] == results['packages_id']:
                b.append(package)
           results['packages_id'] = b
       results['rooms_id'] = a

     print("rate", rate_details)
     
     for room_details in result:
        rooms = room_details['rooms_id']
        if len(rooms) == 0:
            pass
        else:
            for room in rooms:
               for rate in rate_details:
                  #if room['rooms_id'] == rate['rooms_id']: 
                     if s['adults'] == 4:
                        room['room_rate'] = rate['four_adult_amount']       
                     elif s['adults'] == 3:
                        room['room_rate'] = rate['three_adult_amount']
                     elif s['adults'] == 2:
                         room['room_rate'] = rate['two_adult_amount']
                     elif s['adults'] == 1:
                         room['room_rate'] = rate['one_adult_amount']
                 
     return(json.dumps({"Return": result,"Status": "Success","StatusCode": "200"},indent=4))
