from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
def Hotel_RES_POST_Select_QueryReservationActivitylog(request):
    Res_id = request.json['Res_id']
    d = {}
    
    d['Res_id'] = Res_id
    sql_value = gensql('select','reservation.res_activity_log','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
