from sqlwrapper import gensql, dbget
import json
def HOTEL_FD_POST_SELECT_QueryQueueReservation(request):
    sql = json.loads(dbget("select  rm_room_list.rm_room_status as roomstatus,rm_room_list.rm_fo_status as frontoffice, \
                            rm_room_list.rm_room_class as roomclass,rm_queue_room.rm_qtime,rm_queue_room.rm_queue,res_reservation.* from reservation.res_reservation \
	                    join   room_management.rm_queue_room on \
                            reservation.res_reservation.res_unique_id = room_management.rm_queue_room.res_unique_id \
			    join  room_management.rm_room_list on rm_room_list.rm_room = reservation.res_reservation.res_room"))
    
    a,b,c = {},0,0
    
    for i in sql:

        b += i['res_number_of_rooms']

        if i['res_room_type'] in a :

            val = a[""+i['res_room_type']+""]+i['res_number_of_rooms']

            del a[""+i['res_room_type']+""]

            a[""+str(i['res_room_type'])+""] = val
 
        a[""+str(i['res_room_type'])+""] = i['res_number_of_rooms']

    k={}
    l=[]
    for j in a.items():
        k['room_type'] = j[0]
        #l.append(k)
        #print(l)
        k['room_type_totel'] = j[1]
        l.append(k)
        #print(l)
        #c+=1
    #print(k,type(k))
    print(l)
    #k = json.loads(str(k)) 
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'TotalRoomsinQueue':b,'overview':l,'ReturnCode':'RRTS'},indent=4))  
