from sqlwrapper import gensql
import json

def HOTEL_RES_POST_UPDATE_UpdateFixedRateReservation(request):
    
 
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','Fixed_rate_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('Res_id','Fixed_rate_id')}

    print(e)
    sql_value = gensql('update','reservation.res_fixed_rate',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
