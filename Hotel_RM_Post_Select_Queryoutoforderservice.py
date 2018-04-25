from sqlwrapper import dbget,dbfetch
import json

def hotel_rm_post_select_queryoutoforderservice(request):
    RM_From_Date = request.json['For_Date']
    RM_Room = request.json['RM_Room']
    Room_Class = request.json['Room_Class']
    RS = request.json['RS']
    rs = ''
    for name,val in RS.items():
        if val == 'y':
           if len(rs) != 0:
               rs += ','+"'"+name+"'"
           else:
               rs += "'"+name+"'"
    print(rs,type(rs))       
    sql_room = "select rm_room from room_management.rm_room_list where rm_room_class='"+Room_Class+"' order by rm_room"
    rooms = dbfetch(sql_room)
    print(rooms,type(rooms),len(rooms))
    rm = ''
    for room in rooms:
        if len(rm) != 0:
            rm += ','+str(room)
        else:
            rm += str(room)
    print(rm)    
    sql  = 'select * from room_management.RM_Room_Mainteanance'
    sql1 = ''
    if len(RM_From_Date) != 0:
        if len(sql1) == 0: 
           sql1 += " where "
        sql1 += " RM_From_Date = '"+RM_From_Date+"' "
    print(sql1)    
    if len(RM_Room) !=0:
        if len(sql1) == 0: 
           sql1 += " where "
        else:
           sql1 += " and " 
        sql1 += " RM_Room = "+RM_Room+""
    print(sql1)    
    if len(rooms) != 0:
        if len(sql1) == 0: 
           sql1 += " where "
        else:
           sql1 += " and " 
        sql1 += " RM_Room in ("+rm+")"        
    print(sql1)
    if len(rs) != 0:
        if len(sql1) == 0: 
           sql1 += " where "
        else:
           sql1 += " and " 
        sql1 += " RM_Status in ("+rs+")"
    print(sql1)
    sql = sql + sql1
    result = dbget(sql)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':result  ,'ReturnCode':'RRTS'},indent=4))

    
