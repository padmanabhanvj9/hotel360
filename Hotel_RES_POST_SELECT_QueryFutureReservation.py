from sqlwrapper import gensql
import json

from datetime import datetime
def ProfileFutureReservation(request):
    d = request.json
    currentMonth = datetime.now().month
    print(currentMonth)
    
    sql_value = gensql('select','reservation.res_reservation','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
