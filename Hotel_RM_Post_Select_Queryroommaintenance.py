from sqlwrapper import dbget,dbfetch
import json

def hotel_rm_post_select_queryroommaintenance(request):
    RM_Room = request.json['RM_Room']
    RM_Room_Class = request.json['RM_Room_Class']
    Show = request.json['Show']
    sql = "select * from room_management.RM_Room_Mainteanance_Acitivity_Log"
    sql1 = ''
    if len(RM_Room) != 0:
        sql1 += " where "
        sql1 += " rm_room = "+RM_Room+""
    if len(RM_Room_Class) != 0:
        sql_room = "select rm_room from room_management.rm_room_list where RM_Room_Class ='"+RM_Room_Class+"' order by rm_room"
        rooms = dbfetch(sql_room)
        print(rooms)
        rm = ''
        for room in rooms:
            if len(rm) != 0:
               rm += ','+str(room)
            else:
               rm += str(room)
        print(rm)
        if len(rm) != 0:
           if len(sql1) == 0: 
              sql1 += " where "
           else:
              sql1 += " and " 
           sql1 += " RM_Room in ("+rm+")"
    print(sql1)

    if len(Show) != 0 and Show != 'all':
        #if Show == 'all':
         #   pass    
        if len(sql1) == 0: 
              sql1 += " where "
        else:
              sql1 += " and "
        if Show == 'resolved':
            sql1 += "rm_resolvedon not in ('unresolved')"
        if Show == 'unresolved':
            sql1 += "rm_resolvedon in ('unresolved')"
        
    print(sql1)          
    print(sql)
    sql = sql+sql1
    a = dbget(sql)
    print(a)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':a  ,'ReturnCode':'RRTS'},indent=4))

