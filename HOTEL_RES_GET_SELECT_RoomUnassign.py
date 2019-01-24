from sqlwrapper import gensql, dbput, dbget
import json
import requests
from flask import Flask,request,jsonify
def HOTEL_RES_GET_SELECT_RoomUnassign(request):
    Res_id = request.json['Res_id']
    print(Res_id)
    Res_id  = Res_id.split(',')

    Res_id = str(Res_id)[1:-1]
    Res_unique_id = request.json['Res_unique_id']
    Res_unique_id  = Res_unique_id.split(',')

    Res_unique_id = str(Res_unique_id)[1:-1]
    sqlvalue = json.loads(dbget("select res_room,res_room_type,res_block_code from reservation.res_reservation where res_id in ("+Res_id+") and res_unique_id in ("+Res_unique_id+")"))
    print("sqlval",sqlvalue)
    if sqlvalue[0]['res_block_code'] is not None and sqlvalue[0]['res_block_code'] != 'PM':
        if sqlvalue[0]['res_room_type']== 'Kngn':
           sql = dbput("update business_block.current_grid set kngn = kngn -'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"' and grid_type =3")
           print(sql)
        elif sqlvalue[0]['res_room_type'] =='Kngs':
             sql = dbput("update business_block.current_grid set kngs = kngs-'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif sqlvalue[0]['res_room_type'] =='Ksbn':
             sql = dbput("update business_block.current_grid set Ksbn = Ksbn-'1'  where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql) 
        elif sqlvalue[0]['res_room_type'] == 'Ksbs':
             print("workingits fine")
             sql = dbput("update business_block.current_grid set ksbs = ksbs -'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif sqlvalue[0]['res_room_type'] =='Sjsn' :
             sql = dbput("update business_block.current_grid set sjsn = sjsn-'1'  where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif sqlvalue[0]['res_room_type'] =='Sdbn':
             sql = dbput("update business_block.current_grid set sdbn = sdbn -'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif sqlvalue[0]['res_room_type'] =='Sjss':
             sql = dbput("update business_block.current_grid set sjss = sjss -'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
        elif sqlvalue[0]['res_room_type'] =='Comp':
             sql = dbput("update business_block.current_grid set comp = comp -'1' where block_id='"+str(sqlvalue[0]['res_block_code'])+"'  and grid_type =3")
             print(sql)
    else:
        pass
    pickup = dbput("update business_block.room_revenue set room_nights_picked  = room_nights_picked + '1' where  block_id='"+str(sqlvalue[0]['res_block_code'])+"'")
    print(pickup)
    
    rooms = ''
    for  i in sqlvalue:
        if len(rooms) == 0:
            rooms += "'"+str(i['res_room'])+"'"
        else:
            rooms += ","+"'"+str(i['res_room'])+"'"
    print(rooms)        
    
    fo_status = "vacant"
    res_status = "not reserved"
    psql = dbput("update room_management.rm_room_list set rm_fo_status = '"+fo_status+"',rm_reservation_status = '"+res_status+"',rm_fo_person = '0' where rm_room in ("+rooms+")")
    print(psql)
    data = '0'
    sql = dbput("update reservation.res_reservation set res_room = "+data+" where res_id in ("+Res_id+") and res_unique_id in ("+Res_unique_id+") ")

    print(sql)

    
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':'Record Updated Successfully'  ,'ReturnCode':'RUS'},indent=4))
