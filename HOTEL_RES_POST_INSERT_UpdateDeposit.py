from sqlwrapper import gensql
import json
def HOTEL_RES_POST_INSERT_UpdateDeposit(request):
    d = request.json
    sql_value = ('insert','reservation.res_deposit',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

	
def HOTEL_RES_POST_SELECT_QueryDeposit(request):
    d = request.json
    sql_value = gensql('select','reservation.res_deposit','*',d)
    sql_value1 = json.loads(sql_value)
    print(sql_value1)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value1  ,'ReturnCode':'RRTS'},indent=4))

   
