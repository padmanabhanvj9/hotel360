from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_SELECT_QueryGrid(request):
    d = request.json
    block_id = d.get("block_id")
    sql = json.loads(dbget("select grid.*, room_management.room_type.type \
                from business_block.grid \
                join room_management.room_type on room_management.room_type.id = business_block.grid.roomtype_id \
                where grid.block_id = '"+block_id+"'))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
   
