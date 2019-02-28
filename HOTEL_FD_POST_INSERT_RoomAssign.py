from ApplicationDate import application_date
from sqlwrapper import gensql, dbget, dbput
import json
import datetime
def HOTEL_FD_POST_UPDATE_RoomAssign(request):
    d = request.json
    res_id = d.get("Res_id")
    room = d.get("Res_room")
    unique_id = d.get("Res_unique_id")
    a,e = {},{}
    e = { k : v for k,v in d.items() if v != '' if k not in ('Res_id','Res_unique_id')}
    print(a)
    a = { k : v for k,v in d.items() if k != '' if k in ('Res_id','Res_unique_id')}
    print(e)
    app_datetime = application_date()
    Today_date = app_datetime[1]
    #Today_date = str(Today_date)
    
    arrival = dbget("select res_arrival,res_room_type,res_block_code from reservation.res_reservation where res_id = '"+res_id+"' and res_unique_id = '"+unique_id+"' ")
    arrival = json.loads(arrival)
    print(arrival)
    arrival_date = arrival[0]['res_arrival']
    if arrival[0]['res_block_code'] is not None and arrival[0]['res_block_code'] != 'PM':
        if arrival[0]['res_room_type']== 'Kngn':
           sql = dbput("update business_block.current_grid set kngn = kngn +'1' where block_id='"+str(arrival[0]['res_block_code'])+"' and grid_type =3")
           print(sql)
        elif arrival[0]['res_room_type'] =='Kngs':
             sql = dbput("update business_block.current_grid set kngs = kngs+'1' where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif arrival[0]['res_room_type'] =='Ksbn':
             sql = dbput("update business_block.current_grid set Ksbn = Ksbn+'1'  where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql) 
        elif arrival[0]['res_room_type'] == 'Ksbs':
             print("workingits fine")
             sql = dbput("update business_block.current_grid set ksbs = ksbs +'1' where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif arrival[0]['res_room_type'] =='Sjsn' :
             sql = dbput("update business_block.current_grid set sjsn = sjsn+'1'  where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif arrival[0]['res_room_type'] =='Sdbn':
             sql = dbput("update business_block.current_grid set sdbn = sdbn +'1' where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif arrival[0]['res_room_type'] =='Sjss':
             sql = dbput("update business_block.current_grid set sjss = sjss +'1' where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif arrival[0]['res_room_type'] =='Comp':
             sql = dbput("update business_block.current_grid set comp = comp +'1' where block_id='"+str(arrival[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        pickup = dbput("update business_block.room_revenue set room_nights_picked  = room_nights_picked + '1'  where block_id='"+str(arrival[0]['res_block_code'])+"'")
        print(pickup)
    else:
        pass
    arrival = datetime.datetime.strptime(arrival[0]['res_arrival'],'%Y-%m-%d').date()
    totday_date = datetime.datetime.strptime(Today_date,'%Y-%m-%d').date()
    yesterday= totday_date - datetime.timedelta(days=1)
    print(yesterday)
    if totday_date == arrival:
        e['res_guest_status'] = "arrival"
        
        sql_value = gensql('update','reservation.res_reservation',e,a)
        room = e.get("Res_room")
        print(room)
        res_status = "reserved"
        sqlvalue = dbput("update room_management.rm_room_list set rm_reservation_status = '"+res_status+"' where rm_room in ("+room+")")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    elif yesterday ==  totday_date:
        e['res_guest_status'] = "due in"
    
        sql_value = gensql('update','reservation.res_reservation',e,a)
        room = e.get("Res_room")
        res_status = "reserved"
        sqlvalue = dbput("update room_management.rm_room_list set rm_reservation_status = '"+res_status+"' where rm_room in ("+room+")")
       
        print(sql_value)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
    else:
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Assign Not Available','ReturnCode':'RANA'}, sort_keys=True, indent=4))

        
    #if Today_date == arrival_date:
     #   e['res_guest_status'] = "arrival"
  
       
    
