from sqlwrapper import gensql, dbget
import json
from collections import Counter
def HOTEL_FD_POST_SELECT_QueryQueueReservation(request):
    roomtype,l = [],[]
    sql = json.loads(dbget("select  rm_room_list.rm_room_status as roomstatus,rm_room_list.rm_fo_status as frontoffice, \
                            rm_room_list.rm_room_class as roomclass,rm_queue_room.rm_qtime,rm_queue_room.rm_queue,res_reservation.* from reservation.res_reservation \
	                    join   room_management.rm_queue_room on \
                            reservation.res_reservation.res_unique_id = room_management.rm_queue_room.res_unique_id \
			    join  room_management.rm_room_list on rm_room_list.rm_room = reservation.res_reservation.res_room"))
    
    a,b,c ,queue= {},0,0,0
 #   list1 = [{'roomtype':k,'value':v} for k,v in Counter([i['res_room_type'] for i in sql).items()]
    for i in sql:
       roomtype.append(i['res_room_type'])
    print(roomtype)
    print(Counter(roomtype))
   
   
    print(a)
    for keys,values in Counter(roomtype).items():
        print(keys,values)
        queue += values
        l.append({'room_type':keys,'room_type_totel':values})
       
    print(queue)
  
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'TotalRoomsinQueue':queue,'overview':l,'ReturnCode':'RRTS'},indent=4))  
