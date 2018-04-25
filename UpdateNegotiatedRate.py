from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateNegotiatedRate(request):
    PF_Firstname = request.json['PF_Firstname']
    PF_Mobileno = request.json['PF_Mobileno']
    PF_Negotiated_Sequence = request.json['PF_Negotiated_Sequence']
    PF_Rate_Code =  request.json['PF_Rate_Code']
    PF_Start_Sell_Date = request.json['PF_Start_Sell_Date']
    PF_End_Sell_Date = request.json['PF_End_Sell_Date']
    d = {}
    d['PF_Firstname']  = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Negotiated_Sequence'] = PF_Negotiated_Sequence
    d['PF_Rate_Code'] = PF_Rate_Code
    d['PF_Start_Sell_Date'] = PF_Start_Sell_Date
    d['PF_End_Sell_Date'] = PF_End_Sell_Date
    sql_value = gensql('insert','profile.pf_negotiated_rate',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))

