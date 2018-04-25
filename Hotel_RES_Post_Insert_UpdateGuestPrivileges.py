from sqlwrapper import gensql
import json
def Hotel_RES_Post_Insert_UpdateGuestPrivileges(request):
    d = request.json
    sql_value = gensql('insert','reservation.res_guest_privileges',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
def Hotel_RES_Post_Update_UpdateGuestPrivileges(request):
    d,e = {},{}
    d['privileges_key'] = request.json['privileges_key']
    e['pf_mobileno'] = request.json['pf_mobileno']
    sql_value = gensql('update','reservation.res_guest_privileges',d,e)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
def Hotel_RES_Get_Select_QueryGuestPrivileges(request):
    e = {}
    e['pf_mobileno'] = request.args['pf_mobileno']
    sql_value = gensql('select','reservation.res_guest_privileges','privileges_key',e)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
