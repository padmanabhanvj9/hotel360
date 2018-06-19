from sqlwrapper import dbget,dbfetch
import json

def hotel_rm_post_select_queryoutoforderservice(request):
    sql = json.loads(dbget("select * from room_management.rm_room_oo"))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))
    
