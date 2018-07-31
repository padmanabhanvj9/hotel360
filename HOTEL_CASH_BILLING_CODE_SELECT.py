import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_CASH_BILLING_CODE_SELECT(request):
    s = json.loads(dbget("select * from cashiering.billing_code"))
    print(s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))

