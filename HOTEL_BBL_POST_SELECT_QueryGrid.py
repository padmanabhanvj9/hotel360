from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_SELECT_QueryGrid(request):
    d = request.json
    block_id = d.get("block_id")
    sql = json.loads(dbget("select grid.block_id,grid.grid_id,grid.count_one,grid.count_two,grid.count_three,roomtype_one,room_management.room_type.type typeone ,roomtype_two ,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.grid.roomtype_two) as typetwo,roomtype_three,(select room_management.room_type.type from room_management.room_type where room_management.room_type.id = business_block.grid.roomtype_three) as typethree \
                from business_block.grid \
                join room_management.room_type on room_management.room_type.id = business_block.grid.roomtype_one \
                where grid.block_id = '"+block_id+"' "))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
   
