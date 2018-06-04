import datetime
import time
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
def QueryProfileNotes():
    PF_Firstname = request.args['PF_Firstname']
    PF_Mobileno = request.args['PF_Mobileno']
    PF_Note_Type = request.args['PF_Note_Type']
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Note_Type'] = PF_Note_Type
  
    
    sql_value = gensql('select','profile.pf_notes','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
    
def QueryProfilePreference():
    PF_Firstname = request.args['PF_Firstname']
    PF_Mobileno = request.args['PF_Mobileno']
    PF_Preference_Group = request.args['PF_Preference_Group']
    PF_Guest_Preference = request.args['PF_Guest_Preference']
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    d['PF_Preference_Group'] = PF_Preference_Group
    d['PF_Guest_Preference'] = PF_Guest_Preference
   
    sql_value = gensql('select','profile.pf_preference','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
def QueryProfileCreditcard():
    PF_Firstname = request.args['PF_Firstname']
    PF_Mobileno = request.args['PF_Mobileno']
    d = {}
    d['PF_Firstname'] = PF_Firstname
    d['PF_Mobileno'] = PF_Mobileno
    sql_value = gensql('select','profile.pf_creditcard','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
def QueryProfileAcitivitylog():
   
    Emp_Id = request.args['Emp_Id']
    PF_Mobileno = request.args['PF_Mobileno']
    d = {}
    
    d['Emp_Id'] = Emp_Id
    d['PF_Mobileno'] = PF_Mobileno
    sql_value = gensql('select','profile.pf_profile_activitylog','*',d)
    sql_value = json.loads(sql_value)
    print(sql_value)
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','ReturnValue':sql_value  ,'ReturnCode':'RRTS'},indent=4))
    
