from sqlwrapper import gensql
import json
def HOTEL_RES_POST_UPDATE_UpdateReservationAlert(request):
   
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','Alert_id','Res_unique_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('Res_id','Alert_id','Res_unique_id')}


    print(e,d)
    sql_value = gensql('update','reservation.res_alert',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
