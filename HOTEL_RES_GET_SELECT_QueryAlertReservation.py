from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def HOTEL_RES_GET_SELECT_QueryAlertReservation():
    
    PF_Mobileno = request.args['PF_Mobileno']
    RES_Id = request.args['RES_Id']
    d = {}
  
    d['PF_Mobileno'] = PF_Mobileno
    d['RES_Id'] = RES_Id
    sql_value = gensql('select','reservation.res_alert','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
