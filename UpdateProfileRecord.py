import datetime

from sqlwrapper import gensql
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateProfileRecordIndividual():

    d,e = {},{}
    res = request.json
    print(res)
    for name,val in res.items():
 
       if name == 'PF_Firstname' or name == 'PF_Mobileno':
          e[name] = ""+val+""
       else :
           d[name] = ""+val+""
    print(e,d)
    sql_value = gensql('update','profile.pf_individual_profile',d,e)
    
    
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "aravindh"
    Emp_Lastname = "sowri"
    PF_Action_Type = "Update Profile"
    print(d)
    values = d.values()
    print(values)
    data = e.get('PF_Mobileno')
    print(data)
    PF_Mobileno = data
    PF_Log_Description = ''
    for i in values:
       PF_Log_Description +=  i +" | "
    print(PF_Log_Description)
    
       
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    s['Emp_Lastname'] = Emp_Lastname
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = PF_Action_Type
    s['PF_Log_Description'] = PF_Log_Description
    s['PF_Mobileno'] = PF_Mobileno
 
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)


    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
def UpdateProfileRecordCompany():
    
    d,e = {},{}
    res = request.json
    print(res)
    for name,val in res.items():
 
       if name == 'PF_Firstname' or name == 'PF_Mobileno':
          e[name] = ""+val+""
       else :
           d[name] = ""+val+""
    print(e,d)
    sql_value = gensql('update','profile.pf_company_profile',d,e)
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "aravindh"
    Emp_Lastname = "sowri"
    PF_Action_Type = "Update Profile"
    print(d)
    values = d.values()
    print(values)
    data = e.get('PF_Mobileno')
    print(data)
    PF_Mobileno = data
    PF_Log_Description = ''
    for i in values:
       PF_Log_Description +=  i +" | "
    print(PF_Log_Description)
    s = {}
    s['Emp_Id'] = Emp_Id
    s['Emp_Firstname'] = Emp_Firstname
    s['Emp_Lastname'] = Emp_Lastname
    s['PF_Log_Date'] = PF_Log_Date
    s['PF_Log_Time'] = PF_Log_Time
    s['PF_Action_Type'] = PF_Action_Type
    s['PF_Log_Description'] = PF_Log_Description
    s['PF_Mobileno'] = PF_Mobileno
    #print(s)
    
    sql_value = gensql('insert','profile.pf_profile_activitylog',s)


    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Updated Successfully','ReturnCode':'RUS'}, sort_keys=True, indent=4))
