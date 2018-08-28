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

    data1 = json.loads(dbget("select roomtype_id,available_rooms,room_type.type from business_block.grid join \
                             room_management.room_type on grid.roomtype_id = room_type.id where block_id="+d+" "))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return_value':data1,'Return': 'Record Retrieved Successfully','ReturnCode':'RRS'}, sort_keys=True, indent=4))

def HOTEL_BBL_POST_UPDATE_UpdateRoomingList_Roomtype(request):
     #block_id = request.json['block_id']
    d = request.json
    x,a,e,y = {},{},{},{}
    x = d['data']
    for i in x:
        y = { k : v for k,v in i.items() if v != '' if k not in ('type')}
        
        a = { k : v for k,v in y.items() if v != '' if k not in ('block_id','roomtype_id')}
        print(a)
        e = { k : v for k,v in y.items() if k != '' if k in ('block_id','roomtype_id')}
        print(e)
            
        
        sql = gensql('update','business_block.grid',a,e)
        print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def HOTEL_BBL_POST_SELECT_SelectRoomtype(request):
    block_id =request.json['block_id']
    s = []
    p = 0
    sql = json.loads(dbget("select roomtype_id from business_block.grid where block_id='"+block_id+"'"))
    print(sql)
    for i in sql:
        print(i['roomtype_id'])
        psql = json.loads(dbget("select * from room_management.room_type where  room_type.id = '"+str(i['roomtype_id'])+"'"))
        print(psql)
        #room_type = psql
        s.append(psql[0])
       # print(room_type)
    print(s)   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Retrieved Successfully','ReturnCode':'RRS','ReturnValue':s}, sort_keys=True, indent=4))
def HOTEL_BBL_POST_SELECT_gridservice(request):
    block_id =request.json['block_id']
    roomtype_id = request.json['roomtype_id']
    sql = json.loads(dbget("select * from business_block.grid where block_id = '"+block_id+"' and roomtype_id = '"+roomtype_id+"'"))

    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Retrieved Successfully','ReturnCode':'RRS','ReturnValue':sql}, sort_keys=True, indent=4))
