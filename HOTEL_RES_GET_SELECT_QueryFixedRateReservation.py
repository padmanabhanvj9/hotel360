from sqlwrapper import gensql
import json
from flask import Flask,request,jsonify
def HOTEL_RES_GET_SELECT_QueryFixedRateReservation(request):
    
    Res_id = request.json['Res_id']
    d = {}
    d['Res_id'] = Res_id  
    sql_value = gensql('select','reservation.res_fixed_rate','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   

