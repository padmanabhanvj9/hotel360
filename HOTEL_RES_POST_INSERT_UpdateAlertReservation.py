from sqlwrapper import gensql
import json
def HOTEL_RES_POST_INSERT_UpdateAlertReservation(request):
    
    d = request.json
    sql_value = gensql('insert','reservation.res_alert',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
