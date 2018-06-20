from sqlwrapper import gensql, dbget
import json
def HOTEL_FD_GET_SELECT_QueryQueueReservation():
    sql = json.loads(dbget("select * from reservation.res_reservation join   room_management.rm_queue_room on \
                            reservation.res_reservation.res_id = room_management.rm_queue_room.res_id"))
    print(sql,type(sql),len(sql))
    a,b = {},0
    print(b)
    for i in sql:
        b += i['res_number_of_rooms']
        #print(b)
        #print(i['res_room_type'],i['res_number_of_rooms'],type(i['res_number_of_rooms']))
        if i['res_room_type'] in a :
            #print(a)
            #print("if ",i['res_room_type'],i['res_number_of_rooms'])
            #print(a[""+i['res_room_type']+""])
            #print(a[""+i['res_room_type']+""]+i['res_number_of_rooms'])
            val = a[""+i['res_room_type']+""]+i['res_number_of_rooms']
            #print(val,type(val))
            del a[""+i['res_room_type']+""]
            #print(a)
            a[""+str(i['res_room_type'])+""] = val
            #print(a)
        a[""+str(i['res_room_type'])+""] = i['res_number_of_rooms']
    print("available",a)
    print("total",b)
        
      
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql,'TotalRoomsinQueue':b,'ReturnValue1':a  ,'ReturnCode':'RRTS'},indent=4))  
    #return("hi")
