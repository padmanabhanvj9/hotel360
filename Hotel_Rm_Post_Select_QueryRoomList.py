from sqlwrapper import dbget
import json

def hotel_rm_post_select_queryroomlist(request):
    sql = 'select * from room_management.RM_Room_List order by rm_room'
    print(sql)      
    db_res = json.loads(dbget(sql))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':db_res  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_insert_roomcount(request):
   d = request.json
   gensql('insert','room_management.room_available',d)
   return(json.dumps({"Return": "Record Inserted Successfully","ReturnCode": "RIS",
                      "Status": "Success","StatusCode": "200"},indent=4))
