from sqlwrapper import gensql

import json

def HOTEL_RES_POST_UPDATE_UpdateWaitlistReservation(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('RES_Id','waitllist')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('RES_Id','waitllist')}
    print(e)
    
    sql_value = gensql('update','reservation.res_waitlist',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

