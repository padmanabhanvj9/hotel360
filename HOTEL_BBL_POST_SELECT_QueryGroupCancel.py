import json
from sqlwrapper import gensql,dbget
import datetime

def HOTEL_BBL_POST_SELECT_QueryGroupCancel(request):

       block_id = request.json['block_id']
       s = json.loads(dbget("select business_block.group_cancel.*, reservation.cancel_reason.reason from business_block.group_cancel left join reservation.cancel_reason \
                            on business_block.group_cancel.reason_id = reservation.cancel_reason.id where business_block.group_cancel.block_id = '"+block_id+"'"))
       print(s)
       return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))




   

