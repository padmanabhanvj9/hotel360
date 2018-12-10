from sqlwrapper import dbget,dbput
import json


def hotel_rm_post_select_queryroommaintenance(request):
    sql = json.loads(dbget("select * from room_management.rm_room_mainteanance_acitivity_log join \
                            room_management.rm_room_list on \
                            room_management.rm_room_mainteanance_acitivity_log.rm_room = \
                            room_management.rm_room_list.rm_room "))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))


def hotel_rm_post_select_OutoforderRoomsonly(request):
    sql = json.loads(dbget("select rm_room from room_management.rm_room_list where rm_room_list.rm_room_status in ('Out Of Order','Out Of Service') "))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_delete_deleteroommaintenance(request):
    room = request.json['rm_room']
    sql = dbput("delete from room_management.rm_room_mainteanance_acitivity_log where rm_room='"+room+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

