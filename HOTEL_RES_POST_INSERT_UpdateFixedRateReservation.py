from sqlwrapper import gensql
import json


def HOTEL_RES_POST_INSERT_UpdateFixedRateReservation(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != ''}
    print(a)
    sql_value = gensql('insert','reservation.res_fixed_rate',a)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
	
