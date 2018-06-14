from sqlwrapper import gensql
import json
def HOTEL_RES_GET_SELECT_QueryWaitlistReservation(request):
    d = request.json
    sql_value = gensql('select','reservation.res_waitlist','*',d)
    sql_value1 = json.loads(sql_value)
    print(sql_value1)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value1  ,'ReturnCode':'RRTS'},indent=4))

   
