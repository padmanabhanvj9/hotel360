from sqlwrapper import gensql, dbget
import json
import datetime
def HOTEL_FD_POST_UPDATE_RoomAssign(request):
    d = request.json
    res_id = d.get("Res_id")
    room = d.get("Res_room")
    a,e = {},{}
    e = { k : v for k,v in d.items() if v != '' if k not in ('Res_id')}
    print(a)
    a = { k : v for k,v in d.items() if k != '' if k in ('Res_id')}
    print(e)
    Today_date = datetime.datetime.utcnow().date()
    Today_date = str(Today_date)
    
  
    arrival = dbget("select res_arrival from reservation.res_reservation where res_id = '"+res_id+"'")
    arrival = json.loads(arrival)
    print(arrival)
    arrival_date = arrival[0]['res_arrival']
    print(arrival_date,type(arrival_date))

    #print(arrival[0]['res_arrival'])
    if Today_date == arrival_date:
        e['res_guest_status'] = "arrival"
        
        sql_value = gensql('update','reservation.res_reservation',e,a)
    else:
        e['res_guest_status'] = "due in"
    
        sql_value = gensql('update','reservation.res_reservation',e,a)
   
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Room Assigned Successfully','ReturnCode':'RAS'}, sort_keys=True, indent=4))
