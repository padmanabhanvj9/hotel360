from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def QueryNegotiatedRate():
    PF_Firstname = request.args['PF_Firstname']
    PF_Mobileno = request.args['PF_Mobileno']
    PF_Rate_Code = request.args['PF_Rate_Code']
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Rate_Code'] = PF_Rate_Code
    sql_value = gensql('select','profile.pf_negotiated_rate','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))

