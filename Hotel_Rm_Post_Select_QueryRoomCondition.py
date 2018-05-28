from sqlwrapper import dbget
import json

def hotel_rm_post_select_queryroomcondition(request):
    sql = 'select rm_room,rm_room_type,rm_room_status,rm_fo_status,rm_features,rm_room_condition from room_management.rm_room_list order by rm_room'
    print(sql)      
    db_res = (dbget(sql))
    print(db_res)
    db_res = json.loads(db_res)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':db_res  ,'ReturnCode':'RRTS'},indent=4))

