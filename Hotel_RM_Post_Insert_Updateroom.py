from sqlwrapper import gensql,dbget,dbput
import json
import datetime

def hotel_rm_post_insert_updateroomlist(request):
    d = request.json
    print(gensql('insert','room_management.RM_Room_List',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def hotel_rm_post_insert_updateroomcondition(request):
    d = request.json
    print(gensql('insert','room_management.RM_Room_Condition',d))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def hotel_rm_post_insert_updateoutoforderservice(request):
    if request.json.get('From_Room') and request.json.get('To_Room'):
        d = request.json
        print(d)
        e = { k : v for k,v in d.items() if k not in ('From_Room','To_Room')}
        from_room = request.json['From_Room']
        to_room = request.json['To_Room']
        from_room = int(from_room)
        to_room = int(to_room)  
        stri = []
        for i in range(from_room,to_room+1):
            stri.append(i)
        print(stri)
        for j in stri:
            e['RM_Room'] = j
            print(gensql('insert','room_management.rm_room_mainteanance_acitivity_log',e))
            sql= dbput("update room_management.rm_room_list set rm_room_status = '"+d['rm_status']+"' \
                   where rm_room = '"+str(e['RM_Room'])+"'")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))    
    else:
        d = request.json
        print(gensql('insert','room_management.rm_room_mainteanance_acitivity_log',d))
        sql= dbput("update room_management.rm_room_list set rm_room_status = '"+d['rm_status']+"' \
                   where rm_room = '"+d['rm_room']+"'")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def hotel_rm_post_insert_updateroommaintenance(request):
    d = request.json
    room = request.json['rm_room']
    d['mainteanance_user'] = 'SUPERVISOR'
    print(d)
    e = { k : v for k,v in d.items() if k  in ('rm_room')}
    f = { k : v for k,v in d.items() if k not  in ('rm_room')}
    #d['rm_resolvedon'] = 'unresolved'
    sql = json.loads(dbget("select * from room_management.rm_room_mainteanance_acitivity_log where rm_room = '"+room+"' "))
    print(sql,type(sql),len(sql))
    if len(sql) != 0 :
        d['rm_last_change'] = sql[0]['rm_resolvedon']
        d['rm_resolvedon'] =  ''
        d['rm_resolvedby'] = ''        
        print(gensql('update','room_management.rm_room_mainteanance_acitivity_log',d,e))
        sql= dbput("update room_management.rm_room_list set rm_room_status = '"+d['rm_status']+"' \
                   where rm_room = '"+d['rm_room']+"'")
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

    else:    
        print(gensql('insert','room_management.RM_Room_Mainteanance_Acitivity_Log',d))
        sql= dbput("update room_management.rm_room_list set rm_room_status = '"+d['rm_status']+"' \
                   where rm_room = '"+d['rm_room']+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def hotel_rm_post_update_resolveroommaintenance(request):
    e = request.json
    print(e)
    d ,s= {},{}
    d['rm_resolvedon'] =  datetime.datetime.utcnow().date()
    d['rm_resolvedby'] = 'SUPERVISOR'

    sql = json.loads(dbget("select * from room_management.rm_room_mainteanance_acitivity_log where rm_room = '"+e['rm_room']+"' "))
    print(sql,type(sql))

    print(gensql('update','room_management.rm_room_mainteanance_acitivity_log',d,e))
    sql= dbput("update room_management.rm_room_list set rm_room_status = '"+sql[0]['rm_return_as']+"' \
                   where rm_room = '"+e['rm_room']+"'")
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
