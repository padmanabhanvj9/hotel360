from sqlwrapper import gensql,dbget,dbput
import json
def Hotel_RES_Post_Insert_UpdateGuestPrivileges(request):
    s,mylist= {},[]
    d = request.json
    
    for data in d['privileges_key_id']:
      s['res_id'] = d['res_id']
      s['privileges_key_id'] = data
      sql_value = gensql('insert','reservation.res_guest_privileges',s)
    
    print(type(d['privileges_key_id']))
    mylist = d['privileges_key_id'] 

    if 5 in mylist:
            sql = dbput("update reservation.res_guest_privileges set schedule_time = '"+str(d['schedule_time'])+"' \
                         where privileges_key_id = 5 and res_id = '"+str(d['res_id'])+"'")
    else:
        pass
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def Hotel_RES_Post_Update_UpdateGuestPrivileges(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','privileges_id','res_unique_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','privileges_id','res_unique_id')}

    print(e)
    sql_value = gensql('update','reservation.res_guest_privileges',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def Hotel_RES_Get_Select_QueryGuestPrivileges(request):
    d = request.json
    sql_value = json.loads(dbget("select privileges.privileges_desc,res_guest_privileges.* from reservation.res_guest_privileges \
                                  left join reservation.privileges on privileges.privileges_id = res_guest_privileges.privileges_key_id \
                                  where res_guest_privileges.res_id = '"+str(d['res_id'])+"'"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

def Hotel_RES_Get_Select_privileges(request):
    sql_value = json.loads(dbget("select * from reservation.res_guest_privileges"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

