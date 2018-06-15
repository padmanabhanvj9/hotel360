from sqlwrapper import gensql, dbput
import json
def HOTEL_RES_POST_DELETE_DeleteReservation(request):
    d = request.json
    res_id = d.get("res_id")
    print(res_id)
    sql_value = dbput("delete from reservation.res_reservation where res_id = "+res_id+"")
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
