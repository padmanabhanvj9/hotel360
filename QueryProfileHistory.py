from sqlwrapper import gensql,dbget
import json
import datetime

def QueryProfileHistoryRecord(request):
    d = request.json['pf_id']
    print(d)
    today = datetime.datetime.utcnow().date()
    print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and res_arrival < '"+str(today)+"' "))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

def QueryProfileStatistics(request):
    d = request.json['pf_id']
    status,status_room,no_show_rooms =[],[],[]

    last_no_show_rooms,last_status,last_status_room = [],[],[]
    #print(d)
    e ,s= {},{}
    today = datetime.datetime.utcnow().date()
    print(today)
    print((today.year)-1)

    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and \
                                  res_arrival between '"+str(today.year)+"-01-01' and '"+str(today.year)+"-12-31' "))
    #print(sql_value)

    current_year = getprofilestatistics(sql_value)


    #Last yyear record###########################################################
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and \
                                  res_arrival between '"+str((today.year)-1)+"-01-01' and '"+str((today.year)-1)+"-12-31' "))
    last_year = getprofilestatistics(sql_value)


    return(json.dumps({'Status': 'Success', 'StatusCode': '200','currentyear':current_year,'lastyear':last_year,'ReturnCode':'RRTS'},indent=4))
def getprofilestatistics(sql_value):
    e ,s= {},{}
    status,status_room,no_show_rooms =[],[],[]
    nights,rooms,rate = 0,0,0
    for i in sql_value:
        arrival = datetime.datetime.strptime(i['res_arrival'],'%Y-%m-%d').date()

        nights += int(i['res_nights'])
        rooms += int(i['res_number_of_rooms'])
        if i['res_rate'] is not None:
           
           rate += i['res_rate']

        status.append(i['res_guest_status'])
        if i['res_guest_status'] in 'cancel':
            status_room.append(i['res_number_of_rooms'])
            if i['res_guest_status'] in 'no show':
              no_show_rooms.append(i['res_number_of_rooms'])
    #print(status)
    #print(nights,rooms,status_room)
    e['Room_Nights'] = nights
    e['Arrival_Rooms'] = rooms
    e['Cancel_Res'] = status.count("cancel")
    e['Room_Revenue'] = rate
    e['No_Show_Res'] = status.count("no show")
    e['Cancel_Rooms'] = sum(i for i in status_room)
    e['No_Show_Rooms'] = sum(i for i in no_show_rooms)
    return(e)

def QueryProfileFutureRecord(request):
    d = request.json['pf_id']
    print(d)
    today = datetime.datetime.utcnow().date()
    print(today)
    sql_value = json.loads(dbget("select * from reservation.res_reservation where pf_id = '"+d+"' and res_arrival > '"+str(today)+"' "))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
