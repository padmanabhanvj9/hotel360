from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_SELECT_QueryRoomRevenue(request):
    d = request.json
    block_id = d.get("block_id")
    sql = json.loads(dbget("select * from business_block.room_revenue where block_id = '"+block_id+"'"))

    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
   
