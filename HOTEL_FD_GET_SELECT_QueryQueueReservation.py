from sqlwrapper import gensql
import json
def HOTEL_FD_GET_SELECT_QueryQueueReservation():
    sql_value = gensql('select','room_management.rm_queue_room','*')
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
