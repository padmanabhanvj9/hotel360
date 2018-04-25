

from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json

def UpdateProfileNotes(request):
    #PF_Notes_Date = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
   # PF_Notes_Date = PF_Notes_Date().strftime('%Y-%m-%dT%H:%M:%SZ')

    PF_Firstname = request.json['PF_Firstname']
    PF_Mobileno =  request.json['PF_Mobileno']
    PF_Note_Type = request.json['PF_Note_Type']
    PF_Note_Title = request.json['PF_Note_Title']
    PF_Notes_Date = request.json['PF_Notes_Date']
    PF_Note_Description = request.json['PF_Note_Description']

    
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Note_Type'] = PF_Note_Type
    d['PF_Note_Title'] = PF_Note_Title
    d['PF_Note_Description'] = PF_Note_Description
    d['PF_Notes_Date'] = PF_Notes_Date

    
    sql_value = gensql('insert','profile.pf_notes',d)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
