from sqlwrapper import gensql, dbget
import json


def HOTEL_CAH_POST_SELECT_QUERYINHOUSERECORD(request):

    sql_value = json.loads(dbget("SELECT * FROM reservation.res_reservation where res_guest_status in ('checkin','due in') "))
    #print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
