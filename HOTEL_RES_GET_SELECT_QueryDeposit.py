from sqlwrapper import gensql
import json
from flask import Flask,request, jsonify
def HOTEL_RES_GET_SELECT_QueryDeposit():
    PF_Mobileno = request.args['PF_Mobileno']
 
    d = {}
  
    d['PF_Mobileno'] = PF_Mobileno
    
    sql_value = gensql('select','reservation.res_deposit','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))


