from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json

def HOTEL_RES_GET_SELECT_QueryAlertReservation(request):
    
    
    Res_id = request.json['Res_id']
    d = {}
  
  
    d['Res_id'] = Res_id
    sql_value = gensql('select','reservation.res_alert','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
