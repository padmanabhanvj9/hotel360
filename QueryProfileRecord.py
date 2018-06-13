import datetime
import time
from sqlwrapper import gensql,dbget
import json

def QueryNegotiatedRate(request):
    d = request.json
    sql_value = json.loads(gensql('select','profile.pf_negotiated_rate','*',d))
    print(sql_value)
    s = []
    for i in sql_value:    
        i['editflag'] = False
        s.append(i)
    #print(s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
def QueryProfileNotes(request):
    d = request.json
    sql_value = json.loads(gensql('select','profile.pf_notes','*',d))
    print(sql_value)
    s = []
    for i in sql_value:
        i['editflag'] = False
        s.append(i)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
    
def QueryProfilePreference(request):

        d = request.json
        sql_value = json.loads(gensql('select','profile.pf_preference','*',d))
        print(sql_value)
        s = []
        for i in sql_value:
            i['editflag'] = False
            s.append(i)
        return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
    
def QueryProfileCreditcard(request):
    d = request.json
    sql_value = json.loads(gensql('select','profile.pf_creditcard','*',d))
    s = []
    for i in sql_value:
        i['editflag'] = False
        s.append(i)
    print(s)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':s  ,'ReturnCode':'RRTS'},indent=4))
def QueryProfileAcitivitylog(request):
    pf_id = request.json['pf_id']
    sql_value = json.loads(dbget("select * from profile.pf_profile_activitylog join reservation.employee on profile.pf_profile_activitylog.emp_id = reservation.employee.emp_id where pf_id='"+pf_id+"' "))
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
 
