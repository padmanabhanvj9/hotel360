from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
def Hotel_RES_Get_Select_QueryReservationActivitylog():
    Emp_Id = request.args['Emp_Id']
    d = {}
    
    d['Emp_Id'] = Emp_Id
    sql_value = gensql('select','reservation.res_activity_log','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
