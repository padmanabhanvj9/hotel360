from sqlwrapper import dbget
import json

def hotel_rm_post_select_queryroomlist(request):
    sql = 'select * from room_management.RM_Room_List order by rm_room'
    print(sql)      
    db_res = (dbget(sql))
    print(db_res)
    db_res = json.loads(db_res)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':db_res  ,'ReturnCode':'RRTS'},indent=4))

