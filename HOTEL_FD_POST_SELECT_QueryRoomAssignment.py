from sqlwrapper import gensql, dbget
import json
def HOTEL_FD_POST_SELECT_QueryRoomAssignment():
    
    sql_value = dbget("select rm_room_list.rm_hk_status,rm_room_list.rm_room_status,pf_individual_profile.pf_individual_vip,res_reservation.* from reservation.res_reservation \
              left join room_management.rm_room_list on reservation.res_reservation.res_room = room_management.rm_room_list.rm_room \
			  left join profile.pf_individual_profile on profile.pf_individual_profile.pf_id = reservation.res_reservation.pf_id where res_room_type not in ('PM')")

    sql_value1 = json.loads(sql_value)
    #print(sql_value1)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value1  ,'ReturnCode':'RRTS'},indent=4))

                      
