from sqlwrapper import gensql
import json
def HOTEL_RES_POST_INSERT_ReservationCreditcard(request):
    d = request.json
    sql_value = gensql('insert','profile.pf_creditcard',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def Hotel_RES_Post_Update_UpdateReservationCreditcard(request):
    d = request.json
    print(d)
    a = { k : v for k,v in d.items() if v != '' if k not in ('res_id','pf_id')}
    print(a)
    e = { k : v for k,v in d.items() if k != '' if k in ('res_id','pf_id')}
    print(e)
    sql_value = gensql('update','profile.pf_creditcard',a,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))

def Hotel_RES_Get_Select_QueryReservationCreditcard(request):
    e = {}
    e['res_id'] = request.json['res_id']
    e['pf_id'] = request.json['pf_id']
    sql_value = gensql('select','profile.pf_creditcard','*',e)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
