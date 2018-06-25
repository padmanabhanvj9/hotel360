from sqlwrapper import dbget,dbput,gensql
import json

def hotel_rm_post_select_queryoutoforderservice(request):
    sql = json.loads(dbget("select * from room_management.rm_room_oo"))
    print(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_delete_deleteoutoforderservice(request):
    room = request.json['rm_room']
    sql = dbput("delete from room_management.rm_room_oo where rm_room='"+room+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Deleted Successfully','ReturnCode':'RDS'}, sort_keys=True, indent=4))

def  hotel_rm_post_update_updateoutoforderservice(request):
   dict1 = request.json
   print(dict1)
   e = { k : v for k,v in dict1.items() if k in ('RM_Room')}
   print(e)
   d = { k : v for k,v in dict1.items() if k not in ('RM_Room')}
   print(d)
   print(gensql('update','room_management.rm_room_oo',d,e))
   return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))



