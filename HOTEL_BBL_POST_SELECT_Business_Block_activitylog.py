import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_BBL_POST_SELECT_Business_Block_activitylog(request):

       block_id = request.json['block_id']
       s = json.loads(dbget("select * from business_block.business_block_activity_log where block_id="+block_id+" "))
       print(s)
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))




   

