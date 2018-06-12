from sqlwrapper import gensql
import json

def HOTEL_RES_GET_SELECT_QueryDepositrule(request):
    Res_id = request.json['Res_id']
 
    d = {}
  
    d['Res_id'] = Res_id
    
    sql_value = gensql('select','reservation.res_deposit','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


