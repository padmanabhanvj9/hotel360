from sqlwrapper import gensql, dbget
import json
def HOTEL_FD_GET_SELECT_QueryQueueReservation(request):
    sql = json.loads(dbget("select * from reservation.res_reservation join   room_management.rm_queue_room on \
                            reservation.res_reservation.res_id = room_management.rm_queue_room.res_id"))
    #print(sql,type(sql),len(sql))
    a,b,c = {},0,0
    #print(b)
    for i in sql:

        b += i['res_number_of_rooms']

        if i['res_room_type'] in a :

            val = a[""+i['res_room_type']+""]+i['res_number_of_rooms']

            del a[""+i['res_room_type']+""]

            a[""+str(i['res_room_type'])+""] = val
 
        a[""+str(i['res_room_type'])+""] = i['res_number_of_rooms']

    #print("available",a,type(a))
    k={}
    for j in a.items():
        #print(j,type(j))
        #print(j[0])
        #print(j[1])
        k['room_type'+str(c)] = j[0]
        k['room_type_totel'+str(c)] = j[1]
        c+=1
    print(k,type(k))
        #print(j.keys())
        #print(j.values())
    #print("total",b)    
      
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'TotalRoomsinQueue':k,'ReturnCode':'RRTS'},indent=4))  
    #return("hi")
