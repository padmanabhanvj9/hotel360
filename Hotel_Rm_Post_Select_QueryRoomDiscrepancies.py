from sqlwrapper import gensql,dbfetch,dbget
import json

def hotel_rm_post_select_queryroomdiscrepancies(request):

    sql = json.loads(dbget('select * from  room_management.rm_room_list \
           join room_management.rm_room_discrepancy on \
           room_management.rm_room_list.rm_room = room_management.rm_room_discrepancy.rm_room'))
    print(sql)      
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'ReturnCode':'RRTS'},indent=4))
