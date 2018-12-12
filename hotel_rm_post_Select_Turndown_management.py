from sqlwrapper import gensql,dbget,dbput
import json
import datetime
def hotel_rm_post_Select_Turndown_management(request):
    turn_down ,e= [],{}
    today_date = datetime.datetime.utcnow().date()
    sql_value = json.loads(dbget("select res_reservation.res_room,res_reservation.res_guest_status,res_traces.* from reservation.res_traces \
                                 left join reservation.res_reservation on res_reservation.res_unique_id = res_traces.res_unique_id \
                                where traces_date = '"+str(today_date)+"' and res_guest_status not in ('no show, cancel')"))
    for i in sql_value:
        psql = json.loads(dbget("select rm_room_list.rm_room_type,rm_room_list.rm_room_status,rm_room_list.rm_room_class from  \
                                room_management.rm_room_list where rm_room = '"+str(i['res_room'])+"'"))
        print(psql)
        
        e['rm_room'] = i['res_room']
        e['traces_request'] = i['traces_trace_text']
        e['turn_down_status'] = 'Requested'
        gensql('insert','room_management.turndown_status',e)
        sql1 = json.loads(dbget('select turndown_status.turn_down_status from '))
        turn_down.append({'room':i['res_room'],
                          'roomtype':psql[0]['rm_room_type'],
                          'roomstatus':psql[0]['rm_room_status'],
                          'roomclass':psql[0]['rm_room_class'],
                          'reservation_status':i['res_guest_status'],
                          'turndown_request':i['traces_trace_text'],
                          'turndown_status':'Requested'})
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':turn_down  ,'ReturnCode':'RRTS'},indent=4))
