from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateProfileCreditcard(request):
    PF_Firstname = request.json['PF_Firstname']
    PF_Mobileno = request.json['PF_Mobileno']
    PF_Sequence = request.json['PF_Sequence']
    PF_Creditcard_No = request.json['PF_Creditcard_No']
    PF_Card_Type = request.json['PF_Card_Type']
    PF_Expiration_Date = request.json['PF_Expiration_Date']

    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Sequence'] = PF_Sequence
    d['PF_Creditcard_No'] = PF_Creditcard_No
    d['PF_Card_Type']  = PF_Card_Type
    d['PF_Expiration_Date'] = PF_Expiration_Date
    sql_value = gensql('insert','profile.pf_creditcard',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))


   
