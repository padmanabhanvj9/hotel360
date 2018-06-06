from sqlwrapper import gensql
import json


def QueryReservationSearch():
   
    sql_value = gensql('select','reservation.res_reservation','*')
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
