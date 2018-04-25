from sqlwrapper import dbget
import json

def hotel_rm_post_select_queryhousekeepinglist(request):
    RS = request.json['RS']
    FS = request.json['FS']
    RMF = request.json['RM_Room_From']
    print(RMF,type(RMF),len(RMF))
    list1,list2 = [],[]
    for name,val in RS.items():
        if val == 'y':
           print(name)
           list1.append(name)
    for name,val in FS.items():
        if val == 'y':
           print('FS',name) 
           list2.append(name) 
    print(list1,list2)
    print(len(list1))
    sql = 'select * from room_management.RM_Room_List'
    print(sql)
    if len(list1) != 0:
        RS_val = ''
        for key in list1:
           if RS_val == '':
              RS_val += "'"+key+"'"
           else:
              RS_val += ','+"'"+key+"'"
        sql += "  where rm_room_status in ("+RS_val+")"
        print(sql)
    if len(list2) != 0:
        FS_val = ''
        for key in list2:
           if FS_val == '':
              FS_val += "'"+key+"'"
           else:
              FS_val += ','+"'"+key+"'"
        if len(list1)== 0:      
           sql += "  where rm_fo_status in ("+FS_val+")"
        else:
           sql += "and rm_fo_status in ("+FS_val+")" 
        print(sql)
    if len(RMF) != 0:
       if len(list1) == 0 and len(list2) == 0: 
          sql += " where rm_room between "+RMF+" and 500 "
       else:
          sql += "and rm_room between "+RMF+" and 500 "
    sql += " order by rm_room"      
    db_res = (dbget(sql))
    print(db_res)
    db_res = json.loads(db_res)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':db_res  ,'ReturnCode':'RRTS'},indent=4))

