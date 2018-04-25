from sqlwrapper import gensql
import json


def HOTEL_RES_POST_INSERT_UpdateFixedRateReservation(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_fixed_rate',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
