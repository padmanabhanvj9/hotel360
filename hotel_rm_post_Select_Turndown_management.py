from sqlwrapper import gensql,dbget,dbput
import json
import datetime
def hotel_rm_post_Select_Turndown_management(request):
    turn_down = []
    b_date = json.loads(dbget("SELECT roll_business_date as b_date FROM endofday.business_date"))
    
    sql_value = json.loads(dbget("select res_reservation.res_room,res_reservation.res_guest_status,res_traces.* from reservation.res_traces \
                                 left join reservation.res_reservation on res_reservation.res_unique_id = res_traces.res_unique_id \
                                where traces_date = '"+str(b_date[0]['b_date'])+"' and res_guest_status not in ('no show, cancel')"))
    for i in sql_value:
        psql = json.loads(dbget("select rm_room_list.rm_room_type,rm_room_list.rm_room_status,rm_room_list.rm_room_class from  \
                                room_management.rm_room_list where rm_room = '"+str(i['res_room'])+"'"))
        print(psql)
        
        if len(psql) != 0: 
        
           turn_down.append({'room':i['res_room'],
                          'roomtype':psql[0]['rm_room_type'],
                          'roomstatus':psql[0]['rm_room_status'],
                          'roomclass':psql[0]['rm_room_class'],
                          'reservation_status':i['res_guest_status'],
                          'turndown_request':i['traces_trace_text'],
                          'turndown_status':i['turndown_status'],
                          'res_id':i['res_id'],
                          'res_unique_id':i['res_unique_id'],
                          'traces_id':i['traces_id']})
           
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':turn_down  ,'ReturnCode':'RRTS'},indent=4))

def hotel_rm_post_update_Turndown_management(request):
    d = request.json
    a = { k : v for k,v in d.items() if v != '' if k not in ('traces_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('traces_id')}

    print(e)
    RES_Log_Date = datetime.datetime.utcnow().date()
    print(RES_Log_Date)
    a['resloved_by'] = "Daisy"
    a['resloved_on'] = RES_Log_Date
    gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
def hotel_rm_post_select_Dropdown_Turndown_management(request):
    sql_value = json.loads(dbget("select * from room_management.turndownstatus"))
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

