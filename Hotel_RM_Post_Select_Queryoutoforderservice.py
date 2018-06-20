from sqlwrapper import dbget,dbput
import json

def hotel_rm_post_select_queryoutoforderservice(request):
    sql = json.loads(dbget("select * from room_management.rm_room_oo"))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_delete_deleteoutoforderservice(request):
    room = request.json['rm_room']
    sql = dbput("delete from room_management.rm_room_oo where rm_room='"+room+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

