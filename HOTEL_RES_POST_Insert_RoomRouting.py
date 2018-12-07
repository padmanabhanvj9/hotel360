from sqlwrapper import gensql,dbget
import json
def HOTEL_RES_POST_Insert_RoomRouting(request):
    d = request.json
    
    gensql('insert','reservation.res_room_routing',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def Hotel_RES_Get_Select_QueryRoomRouting(request):
    d = request.json
    sql_value = json.loads(dbget("select * from reservation.res_room_routing \
                                 where res_id = "+str(d['res_id'])+" and res_unique_id = "+str(d['res_unique_id'])+""))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
