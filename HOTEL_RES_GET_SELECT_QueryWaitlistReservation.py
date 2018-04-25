from sqlwrapper import gensql
import json
from flask import Flask,request,jsonify

def HOTEL_RES_GET_SELECT_QueryWaitlistReservation():
   
    PF_Mobileno = request.args['PF_Mobileno']
    RES_Id = request.args['RES_Id']
    d = {}
  
    d['PF_Mobileno'] = PF_Mobileno
    d['RES_Id'] = RES_Id
    sql_value = gensql('select','reservation.res_waitlist','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

   
