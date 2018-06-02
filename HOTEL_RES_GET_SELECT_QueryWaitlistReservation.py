from sqlwrapper import gensql
import json
from flask import Flask,request,jsonify

def HOTEL_RES_GET_SELECT_QueryWaitlistReservation():
   
    sql_value = gensql('select','reservation.res_waitlist','*')
    sql_value1 = json.loads(sql_value)
    print(sql_value1)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value1  ,'ReturnCode':'RRTS'},indent=4))

   
