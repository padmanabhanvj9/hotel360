from sqlwrapper import dbget,dbput
import json

def hotel_rm_post_select_queryroomcondition(request):
    sql = json.loads(dbget('select room_management.rm_room_list.*,room_management.rm_room_condition.rm_condition from  room_management.rm_room_condition  left join \
                            room_management.rm_room_list on room_management.rm_room_list.rm_room = \
                            room_management.rm_room_condition.rm_room'))
    #print(sql)      
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))
def  hotel_rm_post_delete_roomcondition(request):
    room = request.json['rm_room']
    sql = dbput("delete from room_management.rm_room_condition where rm_room='"+room+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))
