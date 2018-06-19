from sqlwrapper import gensql
import json
def HOTEL_FD_GET_SELECT_QueryTracesActivityLog():
    sql_value = gensql('select','reservation.traces_activity','*')
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
