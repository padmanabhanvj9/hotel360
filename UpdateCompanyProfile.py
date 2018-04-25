from sqlwrapper import gensql
import datetime
from flask import Flask,request, jsonify
import json
app = Flask(__name__)
def UpdateCompanyProfile(request):
    d = request.json
    sql_value = gensql('insert','profile.pf_company_profile',d)
    data = d.get("PF_Mobileno")
    data1 = d.get("PF_Firstname")
    print(data)
    PF_Log_Time = datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)
    PF_Log_Time = PF_Log_Time.time().strftime("%H:%M:%S")
    print(PF_Log_Time)
    PF_Log_Date = datetime.datetime.utcnow().date()
    print(PF_Log_Date)
    Emp_Id = '121'
    Emp_Firstname = "daisy"
    Emp_Lastname = "veroni"
    PF_Action_Type = "New Profile"
    PF_Mobileno = data
    PF_Log_Description = "Create Company Profile" + " "+data1
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
    return(json.dumps({'Status': 'Success', 'StatusCode': '200','Return': 'Record Inserted Successfully','ReturnCode':'RIS'}, sort_keys=True, indent=4))
