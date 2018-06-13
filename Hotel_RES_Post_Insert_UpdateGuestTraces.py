from sqlwrapper import gensql
import json
def Hotel_RES_Post_Insert_UpdateGuestTraces(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_traces',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def Hotel_RES_Post_Update_UpdateGuestTraces(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','traces_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','traces_id')}
    print(e)
    sql_value = gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def Hotel_RES_Get_Select_QueryGuestTraces(request):
    e = {}
    e['res_id'] = request.json['res_id']
    sql_value = gensql('select','reservation.res_traces','*',e)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
