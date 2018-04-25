from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json

def UpdateProfilePreferencenew(request):
    
    d = request.json
    sql_value = gensql('insert','profile.pf_preference',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
