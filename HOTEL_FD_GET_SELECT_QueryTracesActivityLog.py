from sqlwrapper import gensql
import json
def HOTEL_FD_GET_SELECT_QueryTracesActivityLog():
    sql_value = gensql('select','reservation.traces_activity','*')
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_FD_GET_SELECT_QueryNotes(request):
    d = request.json
    sql_value = json.loads(gensql('select','profile.pf_notes','*',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
def HOTEL_FD_GET_SELECT_Querypreference(request):
    d = request.json
    sql_value = json.loads(gensql('select','profile.pf_preference','*',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
