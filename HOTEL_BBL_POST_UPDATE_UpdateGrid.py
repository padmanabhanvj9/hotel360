from sqlwrapper import gensql,dbget
import json
def HOTEL_BBL_POST_UPDATE_UpdateGrid(request):
    d = request.json
    a,e = {},{}
    a = { k : v for k,v in d.items() if v != '' if k not in ('block_id','grid_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('block_id','grid_id')}
    print(e)
     
    sql = gensql('update','business_block.grid',a,e)
    print(sql)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
   
def HOTEL_BBL_POST_SELECT_SelectRoomingList_Roomtype(request):
    d = request.json['block_id']

    data1 = json.loads(dbget("select roomtype_id,total_rooms,room_type.type from business_block.grid join \
                             room_management.room_type on grid.roomtype_id = room_type.id where block_id="+d+" "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return_value':data1,'Return': 'Record Retrieved Successfully','ReturnCode':'RRS'}, sort_keys=True, indent=4))
