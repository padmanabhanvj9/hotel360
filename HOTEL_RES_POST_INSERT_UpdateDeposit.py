from sqlwrapper import gensql
import json
def HOTEL_RES_POST_INSERT_UpdateDeposit(request):
    d = request.json
    sql_value = ('insert','reservation.res_deposit',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Credited Successfully','ReturnCode':'CS'}, sort_keys=True, indent=4))

	
