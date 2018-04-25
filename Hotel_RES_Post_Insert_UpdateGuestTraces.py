from sqlwrapper import gensql
import json
def Hotel_RES_Post_Insert_UpdateGuestTraces(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_traces',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

def Hotel_RES_Post_Update_UpdateGuestTraces(request):
    d = request.json
    a = { k : v for k,v in d.items() if k != 'pf_mobileno'}
    e = { k : v for k,v in d.items() if k != '' if k == 'pf_mobileno'}
    sql_value = gensql('update','reservation.res_traces',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def Hotel_RES_Get_Select_QueryGuestTraces(request):
    e = {}
    e['pf_mobileno'] = request.args['pf_mobileno']
    sql_value = gensql('select','reservation.res_traces','*',e)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
