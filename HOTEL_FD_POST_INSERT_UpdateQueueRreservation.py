import datetime
from sqlwrapper import gensql,dbget,dbput
import json
def HOTEL_FD_POST_INSERT_UpdateQueueRreservation(request):
    
    d = request.json
    res_id = d.get("Res_id")
    rm_room = d.get("rm_room")
    print(rm_room,type(rm_room))
    rm_room  = rm_room.split(',')
    print(rm_room,type(rm_room))
    rm_room = str(rm_room)[1:-1]
    print(rm_room)
    RES_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    RES_Log_Time = RES_Log_Time.time().strftime("%H:%M:%S")
    print(RES_Log_Time)
    RM_Queue_Date = datetime.datetime.utcnow().date()
    print(RM_Queue_Date)
    RM_Queue_Date = str(RM_Queue_Date)
    
    psql = dbget("select rm_room_type,rm_room_status,rm_fo_status,rm_room_class from room_management.rm_room_list \
                          where rm_room in ("+rm_room+")")
    print(psql,type(psql))
    psql = json.loads(psql)
    print(psql)
    room_type = psql[0]['rm_room_type']
    print(room_type)
    room_status = psql[0]['rm_room_status']
    fo_status = psql[0]['rm_fo_status']
    room_class = psql[0]['rm_room_class']
    
    sql = dbget("select count(*)from room_management.rm_queue_room")
    sql = json.loads(sql)
    i = str(sql[0]['count'])
    print(sql[0]['count'])
    print(i,type(i))
    
    for number in i: 
         print(number,type(number))
         number = int(number)
         number += 1
    print(number)
    s={}
    s['rm_queue'] = number
    s['res_id'] = res_id
    s['rm_qtime'] = RES_Log_Time
    s['rm_room_type'] = room_type
    s['rm_room_class'] = room_class
    s['rm_fo_status'] = fo_status
    s['rm_room_status'] = room_status
    sql = gensql('insert','room_management.rm_queue_room',s)
    print(sql)

    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
