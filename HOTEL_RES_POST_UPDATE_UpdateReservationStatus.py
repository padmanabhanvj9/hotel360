from sqlwrapper import gensql
import json
def HOTEL_RES_POST_UPDATE_UpdateReservationStatus(request):
    d,e ={},{}
    res = request.json
    for key,val in res.items():
        if key == 'PF_Mobileno' or key == 'RES_Id':
            e[key] = ""+val+""
        else:
            d[key] = ""+val+""
    print(e,d)
    sql_value = gensql('update','reservation.res_reservation',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
    
    
