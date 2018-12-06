from sqlwrapper import gensql,dbget
import json
import datetime
from HOTEL_REM_POST_SELECT_UpdateRatecodeSetup import HOTEL_REM_POST_SELECT_SelectRatesetupAll

def HOTEL_RES_POST_SELECT_QueryPackageOptions(request):
    
    
     s = request.json
     rate_code,room_type_id = [],[]
     #query = requests.post("https://hotel360.herokuapp.com/HOTEL_REM_POST_SELECT_SelectRatesetupAll")
     data = json.loads(HOTEL_REM_POST_SELECT_SelectRatesetupAll(request))
     #print(data)
     #print(type(data['Rate_header']))
     value = data['Rate_header']
     result = [d for d in value if d['begin_sell_date'] >= s['res_arrival'] and d['end_sell_date'] <= s['res_depature']]
     print(type(result))
     for row in result:
          room_type_id.append(row['rooms_id'])
     print(room_type_id)
     roomtype = data['Rate_details_room_types']
     finalresult = [z for z in roomtype if z['rooms_id'] in room_type_id]
     
     print(finalresult)
        
     '''
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
       
       '''
 
     return(json.dumps({"Return": finalresult,"Status": "Success","StatusCode": "200"},indent=4))
    
